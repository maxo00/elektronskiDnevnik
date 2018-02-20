import sqlite3

# noinspection PyUnusedLocal


def uzimanjeOcenaJedanUcenik(sifraUcenika, brojOdeljenja):
    ispis = ""
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
        kontrola.execute("SELECT ID FROM "+odeljenje)
        id = kontrola.fetchone()[0]
        print("Ima ovo odeljenje")
    except:
        print("Ovo odeljenje ne postoji")
        return "Ovo odeljenje ne postoji"
    sve = kontrola.execute("SELECT * FROM " + odeljenje)
    stavke = list(map(lambda x: x[0], kontrola.description))
    trazenjeZaIspis = kontrola.execute("SELECT * FROM " + odeljenje + " WHERE sifraUcenika=?", (sifraUcenika,))
    podaci = kontrola.fetchone()
    # print(stavke)
    # print(podaci)
    stigloDo = 0
    for stavka in stavke:
        try:
            if podaci[stigloDo] is None or podaci[stigloDo] == "":
                podatak = "/"
            else:
                podatak = str(podaci[stigloDo])
            if stigloDo == 2:
                podatak = (podaci[2]).upper()
            if stavka == "imeUcenika":
                stavka = "Ime ucenika"
            if stavka == "id":
                stavka = "ID"
            if stavka == "sifraUcenika":
                stavka = "Sifra ucenika"
            else:
                stavka = stavka.title()

            print(stavka + ": " + podatak)
            ispis +=  stavka + ": " + podatak + ";"
            stigloDo += 1
        except:
            print("Ne postoji ucenik sa datom sifrom u ovom odeljenju")
            return "Ne postoji ucenik sa datom sifrom u ovom odeljenju"
    #print(ispis)
    return ispis


def pregledBeleski(sifraUcenika):
    baza = sqlite3.connect("dnevnik.db")
    kontrola = baza.cursor()
    vracanje = ""
    ispis = kontrola.execute("SELECT beleska, datum FROM Beleske where sifraUcenika=? ORDER BY  datum DESC", (sifraUcenika,))

    for beleska, datum in ispis:
        # print(beleska)
        beleska = beleska.replace("\n", ";")
        vracanje += str(beleska + ";" + datum + "|")
        print(beleska + "\n" + datum)
        print('--------------------------------')
    baza.commit()
    baza.close()
    if vracanje == "":
        vracanje = "Nema beleski za ovog ucenika"
    #print(vracanje)
    return vracanje


def pregledPredmeta(brojOdeljenja, sifraProfesora):
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
        kontrola.execute("SELECT predmetProfesora FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
        predmet = kontrola.fetchone()[0]
        print("Dobro unet profesor")
    except:
        print("Lose uneta sifra profesora")
        return "Lose uneta sifra profesora"
    try:
        ucenici = kontrola.execute("SELECT imeUcenika FROM " + odeljenje).fetchall()
    except:
        return "Los unos odeljenja."
    # print(ucenici)

    doUcenika = 0
    listaZaVracanje = []
    try:
       kontrola.execute("SELECT imeUcenika, " + predmet + " FROM " + odeljenje)
       ocenePredmeta = kontrola.fetchall()
       print(ocenePredmeta)
       for ucenik in ocenePredmeta:
           if ucenik[1] == "" or ucenik[1] == None:
               listaZaVracanje.append((ucenik[0].title(), "Nema ocenu"))
           else:
               listaZaVracanje.append((ucenik[0].title(), ucenik[1]))

    except:
        return "Los unos predmeta."

    baza.commit()
    baza.close()
    return listaZaVracanje





def pregledNapomenaOdeljenja(brojOdeljenja, sifraProfesora):

    baza = sqlite3.connect('dnevnik.db')
    kontrola = baza.cursor()
    try:
        kontrola.execute("SELECT imeProfesora FROM Profesori WHERE sifraProfesora= ?", (sifraProfesora, ))
        imeProfesora = kontrola.fetchone()[0]
        print(str(imeProfesora) + ": Dobra sifra")

    except:
        print('Losa sifra profesora')
        return 'Lose uneta sifra profesora'
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
    napomene = kontrola.execute("SELECT * FROM Napomene WHERE odeljenjeUcenika=? ORDER BY datum DESC", (odeljenje,))
    # noinspection PyBroadException
    for napomena in napomene:
        #print(napomena)
        print('Ime ucenika: ' + str(napomena[2]).title() + "\nImeProfesora: " + napomena[0] + "\nRazlog: " + napomena[4] + "\nDatum: " + napomena[3] + "\n--------------")
        ispis+='Ime ucenika: ' + str(napomena[2]).title() + "<br>ImeProfesora: " + napomena[0] + "<br>Razlog: " + napomena[4] + "<br>Datum: " + napomena[3] + "<br>--------------<br>"
    baza.commit()
    baza.close()
    if ispis == "":
        ispis = "Nema napomena za ovo odeljenje."
    return ispis

def pregledNapomenaJedanUcenik(sifraUcenika):
    ispis = ""
    baza = sqlite3.connect('dnevnik.db')
    kontrola = baza.cursor()
    napomene = kontrola.execute("SELECT * FROM Napomene WHERE sifraUcenika=? ORDER BY datum DESC", (sifraUcenika,))
    # noinspection PyBroadException
    for napomena in napomene:
        # print(napomena)
        print('Ime ucenika: ' + str(napomena[2]).title() + "\nImeProfesora: " + napomena[0] + "\nRazlog: " + napomena[
            4] + "\nDatum: " + napomena[3] + "\n--------------")
        ispis += 'Ime ucenika: ' + str(napomena[2]).title() + ";ImeProfesora: " + napomena[0] + ";Razlog: " + \
                 napomena[4] + ";Datum: " + napomena[3] + "|"
    baza.commit()
    baza.close()
    if ispis == "":
        ispis = "Nema napomena za ovog ucenika."
    print(ispis)
    return ispis





# PROVERA
# RADI :D

# pregledNapomena(12) RADI

# print(pregledPredmeta(36, 'udyYF4P')) # RADI
# uzimanjeOcenaJedanUcenik("8MUtHLT", 36) # RADI
# pregledBeleski("FGQgurm") RADI
# pregledNapomenaJedanUcenik('JrOnF2R')
