from flask import Flask, render_template, request
from tkinter import filedialog
import re
import time

tabel_qwerty = {
    'a':['q','w','s','z','x'],
    'b':['v','f','g','h','n'],
    'c':['x','d','f','v'],
    'd':['s','e','r','f','c','x'],
    'e':['w','s','d','r','f'],
    'f':['d','e','r','t','g','v','c'],
    'g':['f','r','t','y','h','b','v'],
    'h':['g','t','y','u','j','n','b'],
    'i':['u','j','k','o','l'],
    'j':['h','y','u','i','k','m','n'],
    'k':['j','m','u','i','o','l'],
    'l':['k','i','o','p'],
    'm':['n','j','k'],
    'n':['b','h','j','m'],
    'o':['i','k','l','p'],
    'p':['o','l'],
    'q':['w','a','s'],
    'r':['e','d','f','g','t'],
    's':['a','q','w','e','d','x','z'],
    't':['r','f','g','h','y'],
    'u':['y','h','j','k','i'],
    'v':['c','f','g','b'],
    'w':['q','a','s','e'],
    'x':['z','a','s','d','c'],
    'y':['t','g','h','j','u'],
    'z':['a','s','x']
    }

def qwerty(a,b):
    if len(a)== len(b):
        huruf = []
        jarak =0
        for i in range(0,len(a)):
            if b[i] in tabel_qwerty[a[i]]:
                jarak += 1
        return jarak
    else:
        return 0

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
    kalimat = {'Silahkan':1,'ketik':2,'di':3,'sini':4}
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
            hasilakhir = {y for y in kamus if [dld(x,y),y][0] == 1 if qwerty(y,x)>0}

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
