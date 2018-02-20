import sqlite3
from time import strftime, localtime
import random
import pregledOcena

def stvaranjeBeleski():
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    kontrola.execute(
        "CREATE TABLE IF NOT EXISTS Beleske(sifraProfesora TEXT,sifraUcenika TEXT,datum TEXT,beleska TEXT) ")
    baza.commit()
    baza.close()


def stvaranjeNapomena():
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    kontrola.execute("CREATE TABLE IF NOT EXISTS Napomene(imeProfesora TEXT,odeljenjeUcenika TEXT,imeUcenika TEXT,datum TEXT, razlog TEXT, sifraUcenika TEXT)")
    baza.commit()
    baza.close()


def dodavanjeBeleski(predmet, imeUcenika, sifraUcenika, sifraProfesora, beleska, ocena):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()
    kontrola.execute("SELECT imeProfesora FROM Profesori WHERE sifraProfesora=?", (sifraProfesora,))
    imeProfesora = kontrola.fetchone()[0]
    print(imeProfesora)
    beleska += "\n Ocena: " + ocena + "\n Ucenik:" + imeUcenika + "\n Profesor: " + imeProfesora + "\n Predmet: " + predmet
    datum = strftime("%d.%m.%Y %H:%M", localtime())
    kontrola.execute("INSERT INTO Beleske(sifraProfesora,sifraUcenika,datum,beleska) VALUES( ?, ?, ?, ?)",
                     (sifraProfesora, sifraUcenika, datum, beleska))
    baza.commit()
    baza.close()


def upisOcene(sifraProfesora, imeUcenika, odeljenjeUcenika, ocena, beleska):
    stvaranjeBeleski()
    odeljenjeUcenika = str(odeljenjeUcenika)
    imeUcenika = imeUcenika.lower()
    # print(imeUcenika)
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()
    odeljenje = ""
    for broj in odeljenjeUcenika:
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
    # noinspection PyBroadException
    try:
        kontrola.execute("SELECT sifraUcenika FROM " + odeljenje + " WHERE imeUcenika=?", (imeUcenika,))
        # noinspection PyBroadException
        try:
            sifraUcenika = kontrola.fetchone()[0]
            # print(sifraUcenika)
            # print(imeUcenika)
            kontrola.execute("SELECT predmetProfesora FROM Profesori WHERE sifraProfesora=?", (sifraProfesora,))
            # noinspection PyBroadException
            try:
                predmet = str(kontrola.fetchone()[0]).lower()
                # print(type(predmet))
                if int(ocena) > 5 or int(ocena) < 1:
                    print("Prevelika ili premala ocena")
                    return "Los unos ocene"
                else:
                    ocena = str(ocena)
                    kontrola.execute("SELECT " + predmet + " FROM " + odeljenje + " WHERE sifraUcenika=?",
                                     (sifraUcenika,))
                    # noinspection PyBroadException
                    try:
                        sad = kontrola.fetchone()[0]
                        imaOcene = sad + ocena
                        kontrola.execute("UPDATE " + odeljenje + " SET " + predmet + "=? WHERE sifraUcenika=?",
                                         (imaOcene, sifraUcenika,))
                    except:
                        kontrola.execute("UPDATE " + odeljenje + " SET " + predmet + "=? WHERE sifraUcenika=?",
                                         (ocena, sifraUcenika,))
                print("Unos uspesan")
                baza.commit()
                baza.close()
                # noinspection PyBroadException
                try:
                    dodavanjeBeleski(predmet, imeUcenika, sifraUcenika, sifraProfesora, beleska, ocena)
                    print("Beleska kreirana")
                except:
                    print("Beleska nije kreirana")
                    return "Beleska nije kreirana"
            except:
                print("Ovo odeljenje nema ovaj predmet")
                return "Ovo odeljenje nema ovaj predmet"
        except:
            print("Greska prilikom unosa. Ucenik nije u ovom odeljenju")
            return "Greska prilikom unosa. Ucenik nije u ovom odeljenju"
    except:
        print("Greska prilikom unosa.")
        return "Greska prilikom unosa."
    return "Sve je zavrseno, " + imeUcenika + " ocena: " + str(ocena)


def upisNapomena(sifraProfesora, odeljenjeUcenika, imeUcenika, razlog):
    odeljenjeUcenika = str(odeljenjeUcenika)
    odeljenje = ''
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()
    for broj in odeljenjeUcenika:
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
        provera = kontrola.fetchone()[0]
        print("Dobro uneto odeljenje")
    except:
        print("Los unos odeljenja")
        return "Los unos odeljenja"

    imeUcenika = imeUcenika.lower()

    kontrola.execute(
        "CREATE TABLE IF NOT EXISTS Napomene(imeProfesora TEXT,odeljenjeUcenika TEXT,imeUcenika TEXT,datum TEXT,razlog TEXT, sifraUcenika TEXT) ")
    kontrola.execute("SELECT sifraUcenika FROM " + odeljenje + " WHERE imeUcenika=?", (imeUcenika,))
    # noinspection PyBroadException
    try:
        # print(imeUcenika)
        datum = strftime("%d.%m.%Y %H:%M", localtime())
        sifraUcenika = kontrola.fetchone()[0]
        # print(sifraUcenika)

        kontrola.execute("SELECT imeProfesora FROM Profesori where sifraProfesora=?", (sifraProfesora,))
        imeProfesora = kontrola.fetchone()[0]
        # print(imeProfesora, odeljenje, imeUcenika, datum, razlog, sifraUcenika)
        # print(imeProfesora)
        kontrola.execute(
            "INSERT INTO Napomene(imeProfesora, odeljenjeUcenika, imeUcenika, datum, razlog, sifraUcenika) VALUES(?,?,?,?,?,?)",(imeProfesora, odeljenje, imeUcenika, datum, razlog, sifraUcenika))
        print('Uneto u napomenu ', imeProfesora, '\n', odeljenjeUcenika, '\n', imeUcenika, '\n', datum, '\n', razlog, '\n')




    except:
        print("Doslo je do greske.")
        return "Doslo je do greske."

    baza.commit()
    baza.close()
    return 'Uneto u napomenu ', imeProfesora, '<br>', odeljenjeUcenika, '<br>', imeUcenika, '<br>', datum, '<br>', razlog

# PROVERA:
# RADI :D

profesori = ["XydEUr6", "kYErcsN", "V0ej92n", "nN1KB8k", "inSqbrG", "NpVnMmh", "LBOg6Se", "vZG3VAf", "bNADd3s", "NwsxSMm", "dnZVAT7", "HetXSPV", "Neka losa sifra"]
odeljenja = [11, 12, 21, 22, 30]
ucenici = ["anic ana", "bojanic bojana", "brankovic branka", "draganic dragana", "dusanovic dusanka", "filipovic filip", "ilic ilija", "ivanovic ivana", "jankovic janko", "lukovic luka", "markovic marko", "milanovic mila", "milosevic milos", "mirkovic mirko", "nenadic nenad", "ognjenovic ognjen", "pavlovic pavle", "petrovic petar", "slobodanovic slobodan", "stankovic stanko", "stefanovic stefan", "stojanovic stojan", "zeljkovic zeljko", "zoric zorica", "dadada"]

stvaranjeBeleski()
# for i in range(2000):
    # ucenik  = random.choice(ucenici)
    # upisOcene(random.choice(profesori), ucenik, random.choice(odeljenja), random.choice(range(1,7)), random.choice(["Ucenik je odgovarao", "Uradjen kontrolni", "Ucenik ispitivan", "Radnjen test", "Domaci zadatak", "Dodatni rad"]))
    # print(ucenik)
# upisOcene('1234567', 'nikolic nikola', 36, random.choice(range(1, 6)), "Ucenik je dobio ocenu iz matematike.")
# upisOcene("1234567", "petrovic petar", 12, random.choice(range(1,6)), "Ucenik je odgovarao.")

# sifraProfesora=input("Sifra: ")
# imeUcenika=input("Ime ucenika: ")
# odeljenje=input("Odeljenje: ")
# beleska=input("Beleska: ")
# upisOcene(sifraProfesora,imeUcenika,odeljenje,random.choice(range(1,6)),beleska)
stvaranjeNapomena()
# upisNapomena('1234567', 36, 'NIKOLIC NIKOLA',"Prica")

# for i in range(150):
    # ucenik  = random.choice(ucenici)
    # upisNapomena(random.choice(profesori), random.choice(odeljenja), ucenik, random.choice(["Ometa cas", "Prica na casu", "Nece da radi", "Uznemirava ucenike", "Prica", "Izasao sa casa", "Odbija da saradjuje"]))
    # print(ucenik)
