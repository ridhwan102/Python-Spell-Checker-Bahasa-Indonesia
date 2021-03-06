from flask import Flask, render_template, request
from tkinter import filedialog
import re
import time

def dld(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    
    if lenstr1 == 0:
        return lenstr2
    if lenstr2 == 0:
        return lenstr1

    #pembuatan sel pertama
    if s1[0] == s2[0]:
            d[(0,0)] = 0
    else:
        d[(0,0)] = 1

    #pembuatan baris pertama
    for i in range(1,lenstr1):
        if s1[i] == s2[0]:
            d[(i,0)] = i
        else:
            d[(i,0)] = min(
                            i+1,
                            d[(i-1,0)]+1)
            
    #pembuatan kolom pertama
    for j in range(1,lenstr2):
        if s1[0] == s2[j]:
            d[(0,j)] = j
        else:
            d[(0,j)] = min(
                            j+1,
                            d[(0,j-1)]+1)

    #pembuatan baris dan kolom kedua sampe akhir
    for i in range(1, lenstr1):
        for j in range(1, lenstr2):
            cost = 1
            if s1[i] == s2[j]:
                cost = 0
                
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost) # substitution

            #tambahan fungsi transposisi 1
            if i==1 and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = j

            #tambahan fungsi transposisi 2
            if j==1 and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = i

            #transposition
            if i>1 and j>1 and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost)
    return d[lenstr1-1,lenstr2-1]

def tokenize(text):
    result = text.lower() #lower the text even unicode given
    result = re.sub(r'[^a-z0-9 -]', ' ', result, flags = re.IGNORECASE|re.MULTILINE)
    result = re.sub(r'( +)', ' ', result, flags = re.IGNORECASE|re.MULTILINE)

    return result.strip()

app = Flask(__name__)
@app.route("/")
def main():
    kalimat = {'Silakan':1,'ketik':2,'di':3,'sini':4}
    hasil = {'-':'-'}
    return render_template('index.html',kalimat=kalimat,hasil=hasil)

@app.route("/periksa",methods=['POST'])
def periksa():
    #ini ngambil text buat jadi kamus
    kamus = []
    with open ("../kamus.txt",'r') as f:
        kamusmasuk = f.read()
        kamus=kamusmasuk.split('\n')

    kalimat = request.form['inputan'].split(' ')
    start = time.time()
    kalimatakhir={}
    kata = ""
    for x in kalimat:
        z=tokenize(x)
        if z in kamus:
            kata = x
        else:
            kata = "*"+x
        kalimatakhir[kata]=1

    hasilakhir={}
    sarankata={}
    for z in kalimat:
        x=tokenize(z)
        if x not in kamus:
            salah = x
            hasilakhir = {y for y in kamus if [dld(x,y),y][0] == 1}
            if (len(hasilakhir)!=0):
                sarankata[x]=hasilakhir
            else:
                sarankata[x]="-"
    #hasilakhir=[]
    
    end = time.time()
    return render_template('index.html', waktu = end-start, hasil = sarankata, kalimat = kalimatakhir)

@app.route("/buka_file",methods=['POST'])
def buka_file():
    kalimatakhir={}
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    if filename != '':
        with open (filename,'r') as k:
                kalimatmasuk = k.read()
                kalimat=kalimatmasuk.split(' ')
   
        for x in kalimat:
            kalimatakhir[x]=1
    else:
        kalimatakhir={'Silahkan':1,'ketik':2,'di':3,'sini':4}

    hasil = {'-':'-'}
    return render_template('index.html', kalimat = kalimatakhir,hasil=hasil)

if __name__ == "__main__":
    app.run(debug = True)
    TEMPLATES_AUTO_RELOAD=True
