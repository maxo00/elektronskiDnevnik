import sqlite3
from time import strftime, localtime
import random
import string


def stvaranjeIzostanaka():
    baza = sqlite3.connect('dnevnik.db')
    kontroa = baza.cursor()

    kontroa.execute("CREATE TABLE IF NOT EXISTS Izostanci(imeProfesora TEXT, imeUcenika TEXT,odeljenje TEXT, datum TEXT, dalJeOpravdano TEXT, sifraUcenika TEXT, sifraIzostanka TEXT)")
    baza.commit()
    baza.close()


def upisIzostanaka(sifraProfesora, imeUcenika, brojOdeljenja):
    imeUcenika = imeUcenika.lower()
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
    stvaranjeIzostanaka()
    baza = sqlite3.connect('dnevnik.db')
    kontrola = baza.cursor()

    try:
        kontrola.execute("SELECT imeProfesora FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
        imeProfesora = kontrola.fetchone()[0]
        print(str(imeProfesora) + ": Dobra sifra")

    except:
        print('Losa sifra profesora')
        return 'Lose uneta sifra profesora'
    print(imeUcenika)
    try:
        kontrola.execute("select neopravdani,sifraUcenika from " + odeljenje + " where imeUcenika = ?", (imeUcenika, ))
        podaci = kontrola.fetchall()
        podaci = podaci[0]
        print(podaci)
        sifraUcenika = str(podaci[1])
        brojNeopravdanih = ""
        if podaci[0] is None or podaci[0] == "":
            brojNeopravdanih = 0
        else:
            brojNeopravdanih = int(podaci[0])
        print("Dobro unet ucenik")

    except:
        print("Lose uneto ime ucenika ili odeljenje")
        return "Lose uneto ime ucenika ili odeljenje"

    datum = strftime("%d.%m.%Y %H:%M", localtime())
    slovaBrojevi = string.ascii_lowercase + string.ascii_uppercase + string.digits
    sifraIzostanka = ''.join(random.sample(slovaBrojevi, 10))
   # print(datum)
    try:
        kontrola.execute("INSERT INTO Izostanci (imeProfesora, imeUcenika, odeljenje, datum, dalJeOpravdano, sifraUcenika, sifraIzostanka) VALUES (?, ?, ?, ?, ?, ?, ?)", (imeProfesora, imeUcenika, odeljenje, datum, 'ne', sifraUcenika, sifraIzostanka, ))

        print("Sve je dobro ucenik je dodat u izostanke")
        #return 'Sve je dobro ucenik je dodat'
    except:
        print("Doslo je do greske")
        return 'Doslo je do greske'
    kontrola.execute("UPDATE " + odeljenje + " SET neopravdani= ? WHERE sifraUcenika= ?", (str(brojNeopravdanih+1), sifraUcenika, ))
    baza.commit()
    baza.close()
    print("Dobro je sve uneto")
    return "Sve je dobro uneto"


def pregledIzostanakaProfesori(brojOdeljenja, sifraProfesora):
    ispis = ""
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
    baza = sqlite3.connect('dnevnik.db')
    kontrola = baza.cursor()
    try:
        kontrola.execute("SELECT imeProfesora FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
        imeProfesora = kontrola.fetchone()[0]
        print("Dobra sifra profesora.")
    except:
        print("Losa sifra profesora.")
        return "Losa sifra profesora"
   # print(odeljenje)
    try:
        kontrola.execute("SELECT * FROM Izostanci WHERE odeljenje = ?", (odeljenje, ))
        podaci = kontrola.fetchall()
        # print(podaci[0])
        for izostanak in podaci:
            # print(izostanak)
            print('Ucenik: ' + str(izostanak[1]).title() + '\nProfesor: ' + izostanak[0] + '\nDatum: ' + izostanak[3] + "\nOpravdao: " + izostanak[4] + "\nSifra izostanka: " + izostanak[6] + "\n-------")
            ispis += 'Ucenik:' + str(izostanak[1]).title() + '<br>Profesor: ' + izostanak[0] + '<br>Datum: ' + izostanak[3] + "<br>Opravdao: " + izostanak[4] + "Sifra izostanka: " + izostanak[6] + '<br> ---------<nr>'
    except:
        print("Ili je lost unos ili ucenik nema izostanaka")
        return "Ili je lost unos ili ucenik nema izostanaka"
    if ispis == "":
        print("Nema izostanaka za dato odeljenje")
        return "Nema izostanaka za dato odeljenje"
    return ispis


def pregledIzostanakaJedanUcenik(sifraUcenika):
    baza = sqlite3.connect('dnevnik.db')
    kontrola = baza.cursor()
    ispis = ''
    try:
        zaIspis = kontrola.execute("SELECT * FROM Izostanci WHERE sifraUcenika = ? ORDER BY datum DESC",(sifraUcenika, ))
        for podaci in zaIspis:
            print(podaci)
            print('Ucenik: ' + str(podaci[1]).title() + '\nProfesor: ' + podaci[0] + '\nDatum: ' + podaci[3] + "\nOpravdao: " + podaci[4] + "\n-------")
            ispis += 'Ucenik: ' + str(podaci[1]).title() + ';Profesor: ' + podaci[0] + ';Datum: ' + podaci[3] + ";Opravdao: " + podaci[4] + "|"

    except:
        print("Ili je lost unos ili ucenik nema izostanaka")
        return "Ili je lost unos ili ucenik nema izostanaka"
    baza.commit()
    baza.close()
    if ispis == "":
        ispis = "Ili je lost unos ili ucenik nema izostanaka"
        print(ispis)
    print('-----------\nISPIS: '+ispis)
    return ispis


def pravdanjeJednogIzostanka(sifraProfesora, sifraIzostanka):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    try:
        kontrola.execute("SELECT imeProfesora FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
        imeProfesora = kontrola.fetchone()[0]
        print("Dobra sifra profesora: " +  imeProfesora)
    except:
        print("Los unos sifre")
        return "Lose uneta sifra profesora"

    try:
        kontrola.execute("SELECT imeUcenika, odeljenje, sifraUcenika FROM Izostanci WHERE sifraIzostanka= ?", (sifraIzostanka, ))
        podaci = kontrola.fetchall()
        podaci = podaci[0]
        imeUcenika = podaci[0]
        odeljenje = podaci[1]
        sifraUcenika = podaci[2]
        print(imeUcenika + "\n" + str(odeljenje) + "\n" + str(sifraUcenika))
        print("Dobro uneta sifra izostanka za ucenika: " + imeUcenika)
    except:
        print("Lose uneta sifra izostanka")
        return "Lose uneta sifra izostanka"

    kontrola.execute("UPDATE Izostanci SET dalJeOpravdano= ? WHERE sifraIzostanka= ?", ("DA", sifraIzostanka, ))
    print("Opravdano u Izostanci tabeli")
    try:
        kontrola.execute("SELECT opravdani, neopravdani FROM " + odeljenje + " WHERE sifraUcenika= ?", (sifraUcenika, ))
        podaci = kontrola.fetchall()
        podaci = podaci[0]
        brojOpravdanih = podaci[0]
        brojNeOpravdanih = podaci[1]
        if brojNeOpravdanih is None or brojNeOpravdanih == "":
            brojNeOpravdanih = 0
        else:
            brojNeOpravdanih = int(brojNeOpravdanih)

        if brojOpravdanih is None or brojOpravdanih == "":
            brojOpravdanih = 0
        else:
            brojOpravdanih = int(brojOpravdanih)
        print("Broj opravdanih: " + str(brojOpravdanih) + "\nBroj neopravdanih: " +str(brojNeOpravdanih))
    except:
        print("Doslo je do greske.")
        return "Doslo je do greske"

    if brojNeOpravdanih == 0:
        print("Ucenik nema neopravdanih izostanaka")
        return "Ucenik nema neopravdanih izostanaka"
    try:
        kontrola.execute("UPDATE " + odeljenje + " SET neopravdani= ? WHERE sifraUcenika= ?", (str(brojNeOpravdanih-1), sifraUcenika, ))
        kontrola.execute("UPDATE " + odeljenje + " SET opravdani= ? WHERE sifraUcenika= ?",(str(brojOpravdanih + 1), sifraUcenika, ))
        print("Sve je dobro")

    except:
        print("Doslo je do greske...")
        return "Doslo je do greske."

    baza.commit()
    baza.close()
    return "Sve je dobro"


def pravdanjeDanaJedanUcenik(sifraProfesora, sifraUcenika, datumZaPravdanje):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    try:
        kontrola.execute("SELECT imeProfesora FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
        imeProfesora = kontrola.fetchone()[0]
        print("Dobra sifra profesora: " + imeProfesora)
    except:
        print("Los unos sifre profesora")
        return "Lose uneta sifra profesora"

    kolikoIzostankaTogDana = 0

    try:
        kontrola.execute("SELECT datum FROM Izostanci WHERE sifraUcenika= ?", (sifraUcenika, ))
        datum = kontrola.fetchall()
        for datumi in datum:
            print(str(datumi[0]))
            if str(datumi[0]).startswith(datumZaPravdanje):
                #print("Ima")
                kolikoIzostankaTogDana += 1
        if kolikoIzostankaTogDana == 0:
            print("Ucenik sa ovom sifromnema izostanke tog dana")
            return "Ucenik sa ovom sifrom nema izostanke tog dana"
        else:
            print("Ima izostanke tog dana: " + str(kolikoIzostankaTogDana))
        # print("Dobra sifra ucenika za datume: " + datum)

    except:
        print("Los unos sifre ucenika")
        return "Lose uneta sifra ucenika"

    kontrola.execute("SELECT odeljenje FROM Izostanci WHERE sifraUcenika= ?", (sifraUcenika, ))
    odeljenje = kontrola.fetchone()[0]
    try:
        kontrola.execute("SELECT opravdani, neopravdani FROM " + odeljenje + " WHERE sifraUcenika= ?", (sifraUcenika, ))
        podaci = kontrola.fetchall()
        podaci = podaci[0]
        brojOpravdanih = podaci[0]
        brojNeOpravdanih = podaci[1]
        if brojNeOpravdanih is None or brojNeOpravdanih == "":
            brojNeOpravdanih = 0
        else:
            brojNeOpravdanih = int(brojNeOpravdanih)

        if brojOpravdanih is None or brojOpravdanih == "":
            brojOpravdanih = 0
        else:
            brojOpravdanih = int(brojOpravdanih)
        print("Broj opravdanih: " + str(brojOpravdanih) + "\nBroj neopravdanih: " +str(brojNeOpravdanih))
    except:
        print("Doslo je do greske.")
        return "Doslo je do greske"

    if brojNeOpravdanih == 0:
        print("Ucenik nema neopravdanih izostanaka")
        return "Ucenik nema neopravdanih izostanaka"


    try:
        datumZaPravdanje += "%"
        kontrola.execute("UPDATE " + odeljenje + " SET neopravdani= ? WHERE sifraUcenika= ?", (str(brojNeOpravdanih-kolikoIzostankaTogDana), sifraUcenika, ))
        kontrola.execute("UPDATE " + odeljenje + " SET opravdani= ? WHERE sifraUcenika= ?",(str(brojOpravdanih + kolikoIzostankaTogDana), sifraUcenika, ))
        kontrola.execute("SELECT sifraIzostanka FROM Izostanci WHERE datum LIKE ? AND sifraUcenika= ?", (datumZaPravdanje, sifraUcenika))
        sifreIzostanaka = kontrola.fetchall()
        print(sifreIzostanaka)
        # sifreIzostanaka = sifreIzostanaka[0]
        # print(sifreIzostanaka)
        for pravdanje in sifreIzostanaka:
            print(pravdanje[0])
            kontrola.execute("UPDATE Izostanci SET dalJeOpravdano= ? WHERE sifraIzostanka= ?", (imeProfesora, pravdanje[0], ))
        print("Sve je dobro")

    except:
        print("Doslo je do greske...")
        return "Doslo je do greske."

    baza.commit()
    baza.close()
    return "Sve je dobro"


print()
profesori = ["XydEUr6", "kYErcsN", "V0ej92n", "nN1KB8k", "inSqbrG", "NpVnMmh", "LBOg6Se", "vZG3VAf", "bNADd3s", "NwsxSMm", "dnZVAT7", "HetXSPV", "Neka losa sifra"]
odeljenja = [11, 12, 21, 22, 30]
ucenici = ["anic ana", "bojanic bojana", "brankovic branka", "draganic dragana", "dusanovic dusanka", "filipovic filip", "ilic ilija", "ivanovic ivana", "jankovic janko", "lukovic luka", "markovic marko", "milanovic mila", "milosevic milos", "mirkovic mirko", "nenadic nenad", "ognjenovic ognjen", "pavlovic pavle", "petrovic petar", "slobodanovic slobodan", "stankovic stanko", "stefanovic stefan", "stojanovic stojan", "zeljkovic zeljko", "zoric zorica", "dadada"]

# for i in range(5000):
    # upisIzostanaka(random.choice(profesori), random.choice(ucenici), random.choice(odeljenja))

# stvaranjeIzostanaka() #RADI
# upisIzostanaka('1234567', 'ilic ilija', 15) # RADI
# pregledIzostanakaProfesori(36, "1234567") # RADI
# pregledIzostanakaJedanUcenik('6fYE9De') # RADI
# pravdanjeJednogIzostanka("1234567", "5TJ0IuK2Dv") # RADI
# pravdanjeDanaJedanUcenik("1234567", "6fYE9De", "27.01.") # RADI