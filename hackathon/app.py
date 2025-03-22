from flask import Flask, render_template,request
import random

# Flask uygulamasını başlatıyoruz
app = Flask(__name__)


indiesarkilar=["This Is The Day/THE THE","Otherwise/Morcheeba"]
turkceindiesarkilar=["Hala Cok Güzelsin/Flört","Aslında Alkol Hala Damarımda/Palmiyeler"]
turkcerocksarkilar=["Fırtınam/Hayko Cepkin","Acının İlacı/Adamlar"]
rocksarkilar=["Crazy On You/Heart","A Horse With No Name/America","MoonShield/In Flames","7/Artic Monkeys"]
turkcepunksarkilar=["Bira ve Kahve/Grizu"]
punksarkilar=["Fake French/Le Tigre","Phanta/Le Tigre","Call Me/Blondie","Rapture/Blondie"]
turkcerapsarkilar=["Anahtar/Nefret","İstanbul/Nefret","Aklımın Odaları/Kolera","Göğe Bakmak İçin/Saian"]
rapsarkilar=["No Face/Drake","Sky/Playboi Carti","No More ?'s/Eazy-E"]
popsarkilar=["This Is The Day/THE THE","Otherwise/Morcheeba"]
# Ana sayfa için route
@app.route('/')
def home():
    return render_template('index.html', sonuc=None)
@app.route('/oneriSayfasi')
def oneriSayfasi():
    return render_template('oneriSayfasi.html')
@app.route('/uzucuSayfasi')
def uzucuSayfasi():
    return render_template('uzucuSayfasi.html')

# Sonuç sayfası: Formu gönderince buraya gelir
@app.route('/oneriSayfasi', methods=['POST'])
def sonuc():
    # Formdan gelen verileri alıyoruz
    sarki_bilgi = request.form.get('sarki_bilgi')
    tur_bilgi = request.form.get('tur_bilgi')
    dil_bilgi = request.form.get('dil_bilgi')

    # Cevaplara göre değerlendirme yapıyoruz
    sonuc_mesaji = f"Size Uygun şarkı: {tur_bilgi}. "

    # Cevaplara göre değerlendirme
    if sarki_bilgi in indiesarkilar:
        indiesarkilar.remove(sarki_bilgi)

    elif sarki_bilgi in turkceindiesarkilar:
        turkceindiesarkilar.remove(sarki_bilgi)

    elif sarki_bilgi in turkcerocksarkilar:
        turkcerocksarkilar.remove(sarki_bilgi)

    elif sarki_bilgi in rocksarkilar:
        rocksarkilar.remove(sarki_bilgi)

    elif sarki_bilgi in turkcepunksarkilar:
        turkcepunksarkilar.remove(sarki_bilgi)

    elif sarki_bilgi in punksarkilar:
        punksarkilar.remove(sarki_bilgi)

    elif sarki_bilgi in turkcerapsarkilar:
        turkcerapsarkilar.remove(sarki_bilgi)

    elif sarki_bilgi in rapsarkilar:
        rapsarkilar.remove(sarki_bilgi)

    elif sarki_bilgi in popsarkilar:
        popsarkilar.remove(sarki_bilgi)

    if "indie" in tur_bilgi.lower() and dil_bilgi=="Türkçe":
        sonuc_mesaji += random.choice(turkceindiesarkilar)
    elif "indie" in tur_bilgi.lower() and dil_bilgi=="İngilizce":
        sonuc_mesaji += random.choice(indiesarkilar)
    elif "rock" in tur_bilgi.lower() and dil_bilgi=="Türkçe":
        sonuc_mesaji += random.choice(turkcerocksarkilar)
    elif "rock" in tur_bilgi.lower() and dil_bilgi=="İngilizce":
        sonuc_mesaji += random.choice(rocksarkilar)
    elif "punk" in tur_bilgi.lower() and dil_bilgi=="Türkçe":
        sonuc_mesaji += random.choice(turkcepunksarkilar)
    elif "punk" in tur_bilgi.lower() and dil_bilgi=="İngilizce":
        sonuc_mesaji += random.choice(punksarkilar)
    elif "rap" in tur_bilgi.lower() and dil_bilgi=="Türkçe":
        sonuc_mesaji += random.choice(turkcerapsarkilar)
    elif "rap" in tur_bilgi.lower() and dil_bilgi=="İngilizce":
        sonuc_mesaji += random.choice(rapsarkilar)
    elif "pop" in tur_bilgi.lower() and dil_bilgi=="Türkçe":
        sonuc_mesaji += random.choice(popsarkilar)
    elif "pop" in tur_bilgi.lower() and dil_bilgi=="İngilizce":
        sonuc_mesaji += random.choice(popsarkilar)
    
    

    return render_template('oneriSayfasi.html', sonuc=sonuc_mesaji)


if __name__ == "__main__":
    app.run(debug=True)