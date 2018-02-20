import sqlite3
import random
import string

def stvaranjeTabeleKontrolnih():
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()
    kontrola.execute(
        "CREATE TABLE IF NOT EXISTS Kontrolni(predmet TEXT,odeljenje TEXT,datum TEXT, odrzan TEXT, sifraProfesora TEXT, sifraKontrolnog TEXT) ")
    baza.commit()
    baza.close()


def zakazatiKontrolni(sifraProfesora, brojOdeljenja, datum):
    stvaranjeTabeleKontrolnih()
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    kontrola.execute("SELECT imeProfesora, predmetProfesora FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
    try:
        podaciProfesora = kontrola.fetchall()
        # print(podaciProfesora)
        imeProfesora = podaciProfesora[0][0]
        predmet = podaciProfesora[0][1]
        print(imeProfesora + " " + predmet)

    except:
        print("Los unos sifre profesora")
        return "Lose uneta sifra profesora"

    brojOdeljenja = str(brojOdeljenja)
    odeljenje = ""
    for broj in brojOdeljenja:
        if broj == "1":
            odeljenje += "Jedan"
        elif broj == "2":
            odeljenje += "Dva"
        elif broj == "3":
            odeljenje += "Tri"
        elif broj == "4":
            odeljenje += "Cetiri"
        elif broj == "5":
            odeljenje += "Pet"
        elif broj == "6":
            odeljenje += "Sest"
        elif broj == "7":
            odeljenje += "Sedam"
        elif broj == "8":
            odeljenje += "Osam"
        elif broj == "9":
            odeljenje += "Devet"


    try:
        kontrola.execute("SELECT id FROM " + odeljenje)
        id = kontrola.fetchone()[0]
        print("Dobar unos odeljenja")
    except:
        print("Los unos odeljenja")
        return "Los unos odeljenja"

    datum = str(datum)
    if len(datum) != 6:
        print("Los unos datuma")
        return "Los unos datuma"
    else:
        print("Dobar unos datuma")

    slovaBrojevi = string.ascii_lowercase + string.ascii_uppercase + string.digits
    sifraKontrolnog = ''.join(random.sample(slovaBrojevi, 10))

    try:
        kontrola.execute("INSERT INTO Kontrolni(predmet, odeljenje, datum, odrzan, sifraProfesora, sifraKontrolnog) VALUES(?, ?, ?, ?, ?, ?)", (predmet, odeljenje, datum, "ne", sifraProfesora, sifraKontrolnog, ))
        baza.commit()
        baza.close()
        print("Sve je dobro")
        return "Kontrolni je zakazan"
    except:
        print("Doslo je do greske")
        baza.close()
        return "Doslo je do greske"



def pregledanjeKontrlonih(sifraProfesora):

    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()



    ispis = []

    kontrola.execute("SELECT odeljenje, datum, sifraKontrolnog FROM Kontrolni WHERE odrzan= ? AND sifraProfesora= ?", ("ne", sifraProfesora))
    podaci = kontrola.fetchall()
    print(podaci)
    for kontrolni in podaci:
        print(kontrolni)
        ispis.append((kontrolni[0], kontrolni[1], kontrolni[2]))





    if ispis == []:
        print("Nemate zakazanih kontrolnih")
        return [("Nemate zakazanih kontrolnih", "", "")]

    print(ispis)
    return ispis


def gotovKontrolni(sifraProfesora, sifraKontrolnog):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    try:
        kontrola.execute('UPDATE Kontrolni SET odrzan= "da" WHERE sifraKontrolnog= ? AND sifraProfesora= ?',(sifraKontrolnog, sifraProfesora, ))
        baza.commit()
        baza.close()
        print("Kontrolni zavrsen")
        return "Kontrolni zavrsen"
    except:
        print("Ovaj kontrolni ne postoji")
        baza.close()
        return "Ovaj kontrolni ne postoji"


def pregledKontrolnihOdeljenje(brojOdeljenja):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    brojOdeljenja = str(brojOdeljenja)
    odeljenje = ""
    for broj in brojOdeljenja:
        if broj == "1":
            odeljenje += "Jedan"
        elif broj == "2":
            odeljenje += "Dva"
        elif broj == "3":
            odeljenje += "Tri"
        elif broj == "4":
            odeljenje += "Cetiri"
        elif broj == "5":
            odeljenje += "Pet"
        elif broj == "6":
            odeljenje += "Sest"
        elif broj == "7":
            odeljenje += "Sedam"
        elif broj == "8":
            odeljenje += "Osam"
        elif broj == "9":
            odeljenje += "Devet"

    try:
        kontrola.execute("SELECT id FROM " + odeljenje)
        id = kontrola.fetchone()[0]
        print("Dobro odeljenje")
    except:
        print("Los unos odeljenja")
        return "Doslo je do greske"

    kontrolneVezbe = []
    try:
        kontrola.execute("SELECT predmet, datum FROM Kontrolni WHERE odrzan= ? AND odeljenje= ?", ("ne", odeljenje, ))
        kontrolneVezbe = kontrola.fetchall()
        # print(kontrolneVezbe)
    except:
        "Doslo je do greske"

    if kontrolneVezbe == []:
        return [("Nema zakazanih kontrolnih","")]

    baza.commit()
    baza.close()
    print(kontrolneVezbe)
    return kontrolneVezbe

print()
# zakazatiKontrolni("1234567", 36 , "22.03.") # RADI
# pregledanjeKontrlonih("udyYF4P")
# gotovKontrolni("1234567",  "B1kawDvecV")
# print(pregledKontrolnihOdeljenje(36))
profesori = ["XydEUr6", "kYErcsN", "V0ej92n", "nN1KB8k", "inSqbrG", "NpVnMmh", "LBOg6Se", "vZG3VAf", "bNADd3s", "NwsxSMm", "dnZVAT7", "HetXSPV", "Neka losa sifra"]
odeljenja = [11, 12, 21, 22, 30]
meseci = ["01.", "02.", "03.", "04.", "05.", "06.", "07.", "08.", "09.", "10.", "11.", "12."]
dani = ["01.", "02.", "03.", "04.", "05.", "06.", "07.", "08.", "09.", "10.", "11.", "12.", "13.", "14.", "15.", "16.", "17.", "18.", "19.", "20.", "21.", "22.", "23.", "24."]
# for i in range(30):
   # zakazatiKontrolni(random.choice(profesori), random.choice(odeljenja), str(random.choice(dani)+random.choice(meseci)))

