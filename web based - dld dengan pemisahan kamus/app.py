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
    for i in range(-1,lenstr1):
        d[(i,-1)] = i+1
    for j in range(-1,lenstr2):
        d[(-1,j)] = j+1
    
    for i in range(lenstr1):
        for j in range(lenstr2):
            cost = 1
            if s1[i] == s2[j]:
                cost = 0
                
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost) # substitution
                          
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
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
    kamus2 = []
    kamus3 = []
    kamus4 = []
    kamus5 = []
    kamus6 = []
    kamus7 = []
    kamus8 = []
    kamus9 = []
    kamus10 = []
    kamus11 = []
    kamus12 = []
    kamus13 = []
    kamus14 = []
    kamus15 = []
    kamus16 = []
    kamus17 = []
    kamus18 = []
    kamus19 = []
    kamus20 = []
    
    with open ("../kamus.txt",'r') as f:
        kamusmasuk = f.read()
        kamus=kamusmasuk.split('\n')
        
    kamus2 = [x for x in kamus if len(x) == 2]
    kamus3 = [x for x in kamus if len(x) == 3]
    kamus4 = [x for x in kamus if len(x) == 4]
    kamus5 = [x for x in kamus if len(x) == 5]
    kamus6 = [x for x in kamus if len(x) == 6]
    kamus7 = [x for x in kamus if len(x) == 7]
    kamus8 = [x for x in kamus if len(x) == 8]
    kamus9 = [x for x in kamus if len(x) == 9]
    kamus10 = [x for x in kamus if len(x) == 10]
    kamus11 = [x for x in kamus if len(x) == 11]
    kamus12 = [x for x in kamus if len(x) == 12]
    kamus13 = [x for x in kamus if len(x) == 13]
    kamus14 = [x for x in kamus if len(x) == 14]
    kamus15 = [x for x in kamus if len(x) == 15]
    kamus16 = [x for x in kamus if len(x) == 16]
    kamus17 = [x for x in kamus if len(x) == 17]
    kamus18 = [x for x in kamus if len(x) == 18]
    kamus19 = [x for x in kamus if len(x) == 19]
    kamus20 = [x for x in kamus if len(x) == 20]
    
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
    
    sarankata={}
    for z in kalimat:
        hasilakhir1={}
        hasilakhir2={}
        hasilakhir3={}
        x=tokenize(z)
        if x not in kamus:
            salah = x
            if len(salah) == 2:
                    hasilakhir1 = {y for y in kamus2 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus3 if [dld(x,y),y][0] == 1}
            if len(salah) == 3:
                    hasilakhir1 = {y for y in kamus2 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus3 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus4 if [dld(x,y),y][0] == 1}
            if len(salah) == 4:
                    hasilakhir1 = {y for y in kamus3 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus4 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus5 if [dld(x,y),y][0] == 1}
            if len(salah) == 5:
                    hasilakhir1 = {y for y in kamus4 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus5 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus6 if [dld(x,y),y][0] == 1}
            if len(salah) == 6:
                    hasilakhir1 = {y for y in kamus5 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus6 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus7 if [dld(x,y),y][0] == 1}
            if len(salah) == 7:
                    hasilakhir1 = {y for y in kamus6 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus7 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus8 if [dld(x,y),y][0] == 1}
            if len(salah) == 8:
                    hasilakhir1 = {y for y in kamus7 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus8 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus9 if [dld(x,y),y][0] == 1}
            if len(salah) == 9:
                    hasilakhir1 = {y for y in kamus8 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus9 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus10 if [dld(x,y),y][0] == 1}
            if len(salah) == 10:
                    hasilakhir1 = {y for y in kamus9 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus10 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus11 if [dld(x,y),y][0] == 1}
            if len(salah) == 11:
                    hasilakhir1 = {y for y in kamus10 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus11 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus12 if [dld(x,y),y][0] == 1}
            if len(salah) == 12:
                    hasilakhir1 = {y for y in kamus11 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus12 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus13 if [dld(x,y),y][0] == 1}
            if len(salah) == 13:
                    hasilakhir1 = {y for y in kamus12 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus13 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus14 if [dld(x,y),y][0] == 1}
            if len(salah) == 14:
                    hasilakhir1 = {y for y in kamus13 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus14 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus15 if [dld(x,y),y][0] == 1}
            if len(salah) == 15:
                    hasilakhir1 = {y for y in kamus14 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus15 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus16 if [dld(x,y),y][0] == 1}
            if len(salah) == 16:
                    hasilakhir1 = {y for y in kamus15 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus16 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus17 if [dld(x,y),y][0] == 1}
            if len(salah) == 17:
                    hasilakhir1 = {y for y in kamus16 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus17 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus18 if [dld(x,y),y][0] == 1}
            if len(salah) == 18:
                    hasilakhir1 = {y for y in kamus17 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus18 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus19 if [dld(x,y),y][0] == 1}
            if len(salah) == 19:
                    hasilakhir1 = {y for y in kamus18 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus19 if [dld(x,y),y][0] == 1}
                    hasilakhir3 = {y for y in kamus20 if [dld(x,y),y][0] == 1}
            if len(salah) == 20:
                    hasilakhir1 = {y for y in kamus19 if [dld(x,y),y][0] == 1}
                    hasilakhir2 = {y for y in kamus20 if [dld(x,y),y][0] == 1}
                    
            hasilakhir2.update(hasilakhir3)
            hasilakhir1.update(hasilakhir2)
            if (len(hasilakhir1)!=0):
                sarankata[x]=hasilakhir1
            else:
                sarankata[x]="-"
    
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
