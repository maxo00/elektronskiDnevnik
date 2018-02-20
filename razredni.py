import sqlite3
import random
import string


def dodelaRazrednih(sifraDirektora, sifraProfesora, brojOdeljenja):
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
        kontrola.execute("SELECT razredni FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
        dalJeRazredni = kontrola.fetchone()[0]
        if dalJeRazredni == "ne":
            print("Ovaj profesor nije razredni.")
        else:
            print("Ovaj profesor je razredni. Prvo uklonite odeljenje ovog profesora.")
            return "Vec razredni"
    except:
        print("Ovaj profesor ne postoji")
        return "Ovaj profesor ne postoji"

    try:
        kontrola.execute("SELECT id FROM " + odeljenje)
        id = kontrola.fetchone()[0]
        print("Odeljenje postoji")
    except:
        print("Ovo odeljenje ne postoji")
        return "Ovo odeljenje ne postoji"

    #Provera sifre direktora

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
        return "Doslo je do greske."

    kontrola.execute("SELECT razredni FROM Profesori")
    odeljenja = kontrola.fetchall()
    print(odeljenja)
    listaRazrednih = []
    for ima in odeljenja:
        listaRazrednih.append(ima[0])
    if odeljenje in listaRazrednih:
        print("Ovo odeljenje vec ima razrednog.")
        return "Ovo odeljenje vec ima razrednog."
    else:
        print("Ovo odeljenje nema razrednog.")




    try:
        kontrola.execute("UPDATE Profesori SET razredni= ? WHERE sifraProfesora= ?", (odeljenje, sifraProfesora, ))
        print("Sve je dobro")
    except:
        print("Doslo je do greske.")
        return "Doslo je do greske"

    baza.commit()
    baza.close()
    print("Gotovo.")
    return "Dobro"


def prestajeRazredni(sifraDirektora, sifraProfesora):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    try:
        kontrola.execute("SELECT razredni FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
        provera = kontrola.fetchone()[0]
        if provera == "ne":
            print("Profesor nije bio razredni")
            return "Profesor nije bio razredni"
    except:
        print("Ovaj profesor ne postoji")
        return "Ovaj profesor ne postoji"

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
            print("Lose uneta sifra direktora.")
            return "Nije napravljenjo odeljenje"
    except:
        print("Doslo je do greske.....")
        return "Doslo je do greske."

    kontrola.execute("UPDATE Profesori SET razredni= ? WHERE sifraProfesora= ?", ("ne", sifraProfesora, ))
    baza.commit()
    baza.close()
    print("Profesor vise nije razredni")
    return "Profesor vise nije razredni"


def direktorGledaProfesore(sifraDirektora):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

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
            print("Lose uneta sifra direktora.")
            return "Nije napravljenjo odeljenje"
    except:
        print("Doslo je do greske.....")
        return "Doslo je do greske."

    kontrola.execute("SELECT * FROM Profesori")
    podaci = kontrola.fetchall()
    print(podaci)
    for profesor in podaci:
        print(profesor)

    return podaci


def ispisProfesora(sifraDirektora, sifraProfesora):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    try:
        kontrola.execute("SELECT imeProfesora FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora,))
        imeProfesora = kontrola.fetchone()[0]
    except:
        print("Ovaj profesor ne postoji")
        return "Ovaj profesor ne postoji"

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
            print("Lose uneta sifra direktora.")
            return "Nije napravljenjo odeljenje"
    except:
        print("Doslo je do greske.....")
        return "Doslo je do greske."

    kontrola.execute("DELETE FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
    baza.commit()
    baza.close()
    print("Obrisan " + imeProfesora)
    return "Obrisan " + imeProfesora


def promenaSifreProfesora(sifraDirektora, sifraProfesora):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    slovaBrojevi = string.ascii_lowercase + string.ascii_uppercase + string.digits
    novaSifraProfesora = ''.join(random.sample(slovaBrojevi, 7))

    try:
        kontrola.execute("SELECT imeProfesora FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora,))
        imeProfesora = kontrola.fetchone()[0]
    except:
        print("Ovaj profesor ne postoji")
        return "Ovaj profesor ne postoji"

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
            print("Lose uneta sifra direktora.")
            return "Lose uneta sifra direktora"
    except:
        print("Doslo je do greske.....")
        return "Doslo je do greske."

    kontrola.execute("UPDATE Profesori SET sifraProfesora= ? WHERE sifraProfesora= ?", (novaSifraProfesora, sifraProfesora, ))
    baza.commit()
    baza.close()
    print(imeProfesora + ", nova sifra: " + novaSifraProfesora)
    return imeProfesora + ", nova sifra: " + novaSifraProfesora


def proveraZaSajt(sifra, brojOdeljenja):
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
        kontrola.execute("SELECT predmetProfesora FROM Profesori WHERE sifraProfesora= ?", (sifra, ))
        predmet = kontrola.fetchone()[0]
    except:
        print("Lose uneta sifra")
        return "Lose uneta sifra"

    try:
        kontrola.execute("SELECT id FROM " + odeljenje)
        id = kontrola.fetchone()[0]
        print("Dobar unos odeljenja")
        try:
            kontrola.execute("SELECT " + predmet + " FROM " + odeljenje)
            imaLi = kontrola.fetchone()[0]
            print("Ovo odeljenje ima ovaj predmet")
        except:
            print("Ovo odeljenje nema ovaj predmet")
            return  "Los unos odeljenja"
    except:
        if predmet == "Vladanje":
            pass
        else:
            print("Los unos odeljenja")
            return "Los unos odeljenja"
    print(predmet)
    return predmet


def obrisatiOdeljenje(sifraDirektora, brojOdeljenja):
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
            print("Lose uneta sifra direktora.")
            return "Lose uneta sifra direktora"
    except:
        print("Doslo je do greske.....")
        return "Doslo je do greske."

    try:
        kontrola.execute("SELECT id FROM " + odeljenje)
        id = kontrola.fetchone()[0]
        print("Odeljenje postoji")
    except:
        print("Ovo odeljenje ne postoji")
        return "Ovo odeljenje ne postoji"

    kontrola.execute("DROP TABLE " + odeljenje)
    print("Gotovo")
    return "Obrisana tabela odeljenja"


def profesorDalJeRazredni(sifraProfesora):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()
    try:
        kontrola.execute("SELECT razredni FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
        jeste = kontrola.fetchone()[0]
    except:
        print("Ovaj profesor ne postoji")
        return "Greska pri unosu profesora"
    baza.commit()
    baza.close()
    return jeste


def pregledSvogodeljenja(sifraProfesora):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()
    try:
        kontrola.execute("SELECT razredni FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
        odeljenje = kontrola.fetchone()[0]
    except:
        print("Niste razredni")
        return "Niste razredni"

    sve = kontrola.execute("SELECT * FROM " + odeljenje)
    stavke = list(map(lambda x: x[0], kontrola.description))
    podaciUcenika = []
    kontrola.execute("SELECT * FROM " + odeljenje)
    podaciOdeljenja = kontrola.fetchall()
    print(podaciOdeljenja)

    return (stavke, podaciOdeljenja)


def izostanciSvogOdeljenja(sifraProfesora):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()
    try:
        kontrola.execute("SELECT razredni FROM Profesori WHERE sifraProfesora= ?" , (sifraProfesora, ))
        odeljenje = kontrola.fetchone()[0]
        print(odeljenje)
    except Exception as E:
        print("Profesor sa datom sifrom nije razredni" )
        return "Niste razredni"

    kontrola.execute("SELECT imeUcenika, datum, sifraIzostanka, dalJeOpravdano FROM Izostanci WHERE odeljenje= ?" , (odeljenje, ))
    sve = kontrola.fetchall()
    print(sve)


def izostanciRazredni(sifraProfesora):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    try:
        kontrola.execute("SELECT razredni FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
        odeljenje = kontrola.fetchone()[0]
        print("Dobro uneto odeljenje")
    except:
        print("Lose uneto odeljenje")
        return "Lose uneto odeljenje"

    listaIzostanaka = []

    kontrola.execute("SELECT imeUcenika, imeProfesora, datum, dalJeOpravdano, sifraIzostanka FROM Izostanci WHERE odeljenje= ?", (odeljenje, ))
    try:
        podaci = kontrola.fetchall()
        print(podaci)

    except:
        print("Greska")
        return "Doslo je do greske"


    if podaci == []:
        print("Nema izostanaka")
        baza.commit()
        baza.close()
        return [("Odeljenje nema izostanke", "", "", "", "")]

    baza.commit()
    baza.close()

    return podaci

def razredniGledaNapomene(sifraProfesora):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    try:
        kontrola.execute("SELECT razredni FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora,))
        odeljenje = kontrola.fetchone()[0]
        print("Dobro uneto odeljenje")
    except:
        print("Lose uneto odeljenje")
        return "Lose uneto odeljenje"

    try:
        kontrola.execute("SELECT imeUcenika, imeProfesora, datum, razlog FROM Napomene WHERE odeljenjeUcenika= ?",(odeljenje,))
        sveNapomene = kontrola.fetchall()
        print(sveNapomene)

    except Exception as E:
        print(E)
        return "Doslo je do greske"

    if sveNapomene == []:
        sveNapomene = [("Odeljenje nema napomena", "", "", "")]
    baza.commit()
    baza.close()
    return sveNapomene


print()
# dodelaRazrednih("znakovi", "bxkI5Hs", 11) # RADI
# prestajeRazredni("znakovi", "bxkI5Hs") # RADI
# direktorGledaProfesore("znakovi") # RADI
# ispisProfesora("znakovi", "asdf") # RADI
# promenaSifreProfesora("znakovi", "Wc7prmH") # RADI
# proveraZaSajt("znakovi", "") # RADI
# print(profesorDalJeRazredni("Ho0qOE2"))
# print(pregledSvogodeljenja("1234567"))

# izostanciSvogOdeljenja("uMdfpl5")

# izostanciRazredni("1234567")
# print(razredniGledaNapomene("ZjglmJp"))
