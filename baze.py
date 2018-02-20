import sqlite3
import random
import string


def stvaranjeProfesora():
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    kontrola.execute(
        "CREATE TABLE IF NOT EXISTS Profesori(imeProfesora TEXT, predmetProfesora TEXT, sifraProfesora TEXT, razredni TEXT) ")

    imeDirektora = "Zamenite ovog direktora"
    sifraDirektora = "1234567"

    kontrola.execute("INSERT INTO Profesori(imeProfesora, predmetProfesora, sifraProfesora, razredni) VALUES(?, ?, ?, ?)", (imeDirektora, "Vladanje", sifraDirektora, "ne"))
    baza.commit()
    baza.close()


# Kasnije za GUI, parametre promeniti da uzimaju vrednosti iz textBox-ova
def upisProfesora(imePrezime, predmet, sifraDirektora):
    # Generisanje sifre (7 nasumicno generisanih karaktera(Velika slova, mala slova i brojevi))
    slovaBrojevi = string.ascii_lowercase + string.ascii_uppercase + string.digits
    sifraProfesora = ''.join(random.sample(slovaBrojevi, 7))

    # Konektovanje sa bazom i unos podataka
    baza = sqlite3.connect('dnevnik.db')
    kontrolaBaze = baza.cursor()
    # noinspection PyBroadException
    try:
        print("test")
        kontrolaBaze.execute("SELECT sifraProfesora FROM Profesori WHERE predmetProfesora='Vladanje'")
        print("ok")
        pravaSifra = kontrolaBaze.fetchall()
        sifreDirektora = []
        print(pravaSifra)

        for sifra in pravaSifra:
            sifreDirektora.append(sifra[0])

        print(sifreDirektora)
        print(sifraDirektora)
        if sifraDirektora in sifreDirektora:
            print("Dobra sifra za direktora.")
        else:
            print("Lose uneta sifra.")
            return "Losa sifra direktora."
    except:
        print("Doslo je do greske profesor nije dodat")
        return "Doslo je do greske profesor nije dodat"

    kontrolaBaze.execute("INSERT INTO Profesori(imeProfesora, predmetProfesora, sifraProfesora, razredni) VALUES (?,?,?,?)", (imePrezime, predmet, sifraProfesora, "ne"))
    baza.commit()
    baza.close()
    print("Uspesno kreiran profesor " + imePrezime + " za predmet " + predmet + " sa sifrom: " + sifraProfesora)
    return str("Uspesno kreiran profesor " + imePrezime + " za predmet " + predmet + " sa sifrom: " + sifraProfesora)


# predmetiOdeljenja i imenacenika je  string odvojen zarezima + jedan razmak
def upisOdeljenja(brojOdeljenja, predmetiString, imenaUcenika, sifraDirektora):

    brojOdeljenja = str(brojOdeljenja)
    predmetiLista = predmetiString.split(", ")
    uceniciLista = imenaUcenika.split(", ")
    uceniciLista.sort()
    odeljenje = ""
    provera = 0
    for broj in brojOdeljenja:
        if broj == "1":
            odeljenje += "Jedan"
            provera += 1
        elif broj == "2":
            odeljenje += "Dva"
            provera += 1
        elif broj == "3":
            odeljenje += "Tri"
            provera += 1
        elif broj == "4":
            odeljenje += "Cetiri"
            provera += 1
        elif broj == "5":
            odeljenje += "Pet"
            provera += 1
        elif broj == "6":
            odeljenje += "Sest"
            provera += 1
        elif broj == "7":
            odeljenje += "Sedam"
            provera += 1
        elif broj == "8":
            odeljenje += "Osam"
            provera += 1
        elif broj == "9":
            odeljenje += "Devet"
            provera += 1
    if provera != 2:
        print("Greska u unosu.")
    else:
        return str(bazaOdeljenja(predmetiLista, odeljenje, uceniciLista, sifraDirektora))


# Kreiranje baze za odeljenje
def bazaOdeljenja(predmetiOdeljenja, imeOdeljenja, uceniciOdeljenja, sifraDirektora):
    ispis = ""
    slovaBrojevi = string.ascii_lowercase + string.ascii_uppercase + string.digits

    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()
    # noinspection PyBroadException
    try:
        print("test")
        kontrola.execute("SELECT sifraProfesora FROM Profesori WHERE predmetProfesora='Vladanje'")
        print("ok")
        pravaSifra = kontrola.fetchall()
        sifreDirektora = []
        print(pravaSifra)

        for sifra in pravaSifra:
            sifreDirektora.append(sifra[0])

        print(sifreDirektora)
        print(sifraDirektora)
        if sifraDirektora in sifreDirektora:
            print("Dobra sifra za direktora.")
        else:
            print("Lose uneta sifra.")
            return "Nije napravljenjo odeljenje"

    except:
        print("Doslo je do greske.....")
        return "Doslo je do greske odeljenje nije kreirano."
    # noinspection PyBroadException
    try:
        kontrola.execute("SELECT imeUcenika FROM " + imeOdeljenja + " WHERE id=1")
        ime = kontrola.fetchone()[0]
        print(ime)
        nastaviti = "NE"
        if nastaviti == "DA":
            kontrola.execute("DROP TABLE IF EXISTS " + imeOdeljenja)
            kontrola.execute(
                "CREATE TABLE " + imeOdeljenja + "(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,sifraUcenika "
                                                 "TEXT,imeUcenika TEXT, prosek TEXT, neopravdani TEXT, opravdani TEXT, Vladanje TEXT)")
            for predmet in predmetiOdeljenja:
                predmet = predmet.lower()
                kontrola.execute("ALTER TABLE " + imeOdeljenja + " ADD " + predmet + " TEXT")
            for ucenik in uceniciOdeljenja:
                sifraUcenika = ''.join(random.sample(slovaBrojevi, 7))
                ucenik = ucenik.lower()
                kontrola.execute("INSERT INTO " + imeOdeljenja + "(imeUcenika,sifraUcenika) VALUES (?,?)",
                                 (ucenik, sifraUcenika))
                print(ucenik.upper() + "SIFRA: " + sifraUcenika)
            print("Baza je obrisana i nova je kreirana.")
        else:
            print("Nista nije promenjeno.")
            return "NE"

    except:
        kontrola.execute(
            "CREATE TABLE " + imeOdeljenja + "(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,sifraUcenika "
                                             "TEXT,imeUcenika TEXT, prosek TEXT,neopravdani TEXT, opravdani TEXT, Vladanje TEXT)")
        for predmet in predmetiOdeljenja:
            kontrola.execute("ALTER TABLE " + imeOdeljenja + " ADD " + predmet.lower() + " TEXT")
        for ucenik in uceniciOdeljenja:
            sifraUcenika = ''.join(random.sample(slovaBrojevi, 7))
            kontrola.execute("INSERT INTO " + imeOdeljenja + "(imeUcenika,sifraUcenika) VALUES (?,?)",
                             (ucenik.lower(), sifraUcenika))
            print(ucenik.upper() + "SIFRA: " + sifraUcenika)
            ispis += str(ucenik.upper() + " SIFRA: " + sifraUcenika) + " <br> "
        print("Baza uspesno kreirana")
        print(ispis)
    baza.commit()
    baza.close()
    print(str(ispis))
    return "Sve je dobro"

# Naknadno dodavanje ucenika, ali ih stavlja na poslednji redni broj, ali to nije problem
# zato sto se djaci uglavnom vode po siframa




def ucenikDosao(imePrezime, brojOdeljenja, sifraDirektora):
    imePrezime = imePrezime.lower()
    slovaBrojevi = string.ascii_lowercase + string.ascii_uppercase + string.digits
    sifraUcenika = ''.join(random.sample(slovaBrojevi, 7))

    odeljenje = ""
    provera = 0



    brojOdeljenja = str(brojOdeljenja)
    for broj in brojOdeljenja:
        if broj == "1":
            odeljenje += "Jedan"
            provera += 1
        elif broj == "2":
            odeljenje += "Dva"
            provera += 1
        elif broj == "3":
            odeljenje += "Tri"
            provera += 1
        elif broj == "4":
            odeljenje += "Cetiri"
            provera += 1
        elif broj == "5":
            odeljenje += "Pet"
            provera += 1
        elif broj == "6":
            odeljenje += "Sest"
            provera += 1
        elif broj == "7":
            odeljenje += "Sedam"
            provera += 1
        elif broj == "8":
            odeljenje += "Osam"
            provera += 1
        elif broj == "9":
            odeljenje += "Devet"
            provera += 1

    if provera == 2:
        # noinspection PyBroadException
        try:
            baza = sqlite3.connect("dnevnik.db")
            kontrola = baza.cursor()
            # noinspection PyBroadException
            try:
                print("test")
                kontrola.execute("SELECT sifraProfesora FROM Profesori WHERE predmetProfesora='Vladanje'")
                print("ok")
                pravaSifra = kontrola.fetchall()
                sifreDirektora = []
                print(pravaSifra)

                for sifra in pravaSifra:
                    sifreDirektora.append(sifra[0])

                print(sifreDirektora)
                print(sifraDirektora)
                if sifraDirektora in sifreDirektora:
                    print("Dobra sifra za direktora.")
                else:
                    print("Lose uneta sifra.")
                    return "Nije dodat ucenik. Losa sifra direktora."
            except:
                print("Doslo je do greske.....")
                return "Doslo je do greske odeljenje nije kreirano."

            print("Ubacivanje u bazu.")
            kontrola.execute("INSERT INTO " + odeljenje + "(imeUcenika, sifraUcenika) VALUES(?,?)", (imePrezime, sifraUcenika))

            baza.commit()
            baza.close()
            print("Unos uspesan. \n Sifra ucenika je: ", sifraUcenika)
            return str("Unos uspesan, sifra ucenika je: " + sifraUcenika)
        except:
            print("Greska u unosu.")
            return "Greska u unosu"


print()


# PROVERE:
# RADE :D
# stvaranjeProfesora()

# upisOdeljenja("99","srpski, matematika, fizicko, engleski, istorija, hemija, fizika, vladanje, programiranje, elektronika", "markovic marko, Lazarevic Lazar, Ilic Ilija, Bojanic Bojan, Darkovic Darko, Nikolic nikolA", "znakovi")
# upisProfesora("Aleksandar Urosevic", "Fizicko")
# upisProfesora("Petar Petrovic", "Fizika")
# upisProfesora("Darko Darkovic", "Istorija")
# upisProfesora("Fizicko Profesor", "Fizicko", "znakovi")
# ucenikDosao("Aleksa Aleksic", 12, "Ppa4v7Hc")
# upisProfesora("Direktor Skole 2", "Vladanje", )