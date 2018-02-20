import sqlite3


def racunanjeProseka(sifraDirektora, brojOdeljenja):

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

    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()

    try:
        kontrola.execute("SELECT id FROM " + odeljenje)
        idOvi = kontrola.fetchone()[0]
        print("Dobro odeljenje")
    except:
        print("Lose uneto odeljenje")
        return "Lose uneto odeljenje"

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
            return "Losa sifra direktora."
    except:
        print("Doslo je do greske")
        return "Doslo je do greske"


    listaSifriUcenika = []
    sifre = kontrola.execute("SELECT sifraUcenika FROM " + odeljenje)
    sifre = kontrola.fetchall()
    # print(sifre)
    for sifra in sifre:
        # print(sifra[0])
        listaSifriUcenika.append(sifra[0])


    kontrola.execute("SELECT * FROM " + odeljenje)
    sviPredmeti= list(map(lambda x: x[0], kontrola.description))
    sviPredmeti = sviPredmeti[6:]
    # print(sviPredmeti)
    # print(sviPredmeti)

    for sifraUcenika in listaSifriUcenika:
        zakluceneOcene = []
        for predmet in sviPredmeti:
            try:
                if predmet == "vladanje":
                    kontrola.execute("SELECT vladanje FROM " + odeljenje + " WHERE sifraUcenika=?", (sifraUcenika, ))
                    ocena = str(kontrola.fetchone()[0])
                    zakluceneOcene.append(int(str(ocena[-1])))
                    kontrola.execute("UPDATE " + odeljenje + " SET vladanje= ? WHERE sifraUcenika= ?", (str(ocena[-1]), sifraUcenika))
                else:
                    ocenePredmeta = []
                    kontrola.execute("SELECT " + predmet + " FROM " + odeljenje + " WHERE sifraUcenika= ?", (sifraUcenika, ))
                    predmetOcene = kontrola.fetchone()[0]
                    for ocena in predmetOcene:
                        ocenePredmeta.append(int(ocena))
                    zakljucenaIzPredmeta = sum(ocenePredmeta) / len(ocenePredmeta)
                    if zakljucenaIzPredmeta % 1 > 0.5:
                        zakljucenaIzPredmeta = int(zakljucenaIzPredmeta) + 1
                    else:
                        zakljucenaIzPredmeta = int(zakljucenaIzPredmeta)
                    zakluceneOcene.append(zakljucenaIzPredmeta)
                    kontrola.execute("UPDATE " + odeljenje + " SET " + predmet + "= ? WHERE sifraUcenika= ?", (str(zakljucenaIzPredmeta), sifraUcenika))
            except:
                continue
            prosekUcenika = str(round((sum(zakluceneOcene) / len(zakluceneOcene)),2))
            if 1 in zakluceneOcene:
                prosekUcenika = 'Nedovoljan'
            kontrola.execute("UPDATE " + odeljenje + " SET prosek= ? WHERE sifraUcenika= ?", (prosekUcenika, sifraUcenika))


        baza.commit()
        print("Prosao")
    baza.close()



    print("SVE JE DOBRO")
    return "SVE JE DOBRO PROSLO"


# racunanjeProseka("znakovi", 22) #RADI




