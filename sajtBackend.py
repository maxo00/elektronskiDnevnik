from bottle import run, route, get, post, request, template, static_file, error, response
import baze
import pregledOcena
import upisOcena
import izostanci
import prosek
import najavljivanjeKontrlonih
import razredni



@route('/static/<imeFajla>')
def slikeIcssser(imeFajla):
    return static_file(imeFajla, root='static')



@error(404)
def error404(error):
    return '<script>window.location = "/";alert("Nepostojeca stranica.");</script>'

@error(500)
def error404(error):
    return '<script>window.location = "/";alert("Prijavite se ponovo.");</script>'


@get('/')
def index():
    response.set_cookie("sifraProfesora", "ne")
    response.set_cookie("odeljenje", "ne")
    return template('drugeStranice\\index.tpl')


@post('/ucenik')
def prebacivanjePodatakaNaStranicu():
    sifraUcenika = request.forms.get('sifraUcenika')
    odeljenje = request.forms.get('odeljenje')

    print("Podaci za ucenika sa sifrom: " + sifraUcenika + ", iz odeljenja: " + odeljenje)

    podaci = pregledOcena.uzimanjeOcenaJedanUcenik(sifraUcenika, odeljenje).split(";")
    print("------------------")
    # print(podaci)
    informacijeZaIspisOcena = []
    for podatak in podaci:
        informacijeZaIspisOcena.append(podatak)

    if str(informacijeZaIspisOcena[0]).startswith("Ne postoji") or str(informacijeZaIspisOcena[0]).startswith("Ovo odeljenje"):
        return '<script>window.location = "/";alert("Greska prilikom unosa");</script>'
    # print(informacijeZaIspisOcena)
    ispisPredmeta = []
    for ispis in informacijeZaIspisOcena:
        # print(ispis)
        deo = ispis.split(":")
        try:
            ispisPredmeta.append((deo[0], deo[1]))
        except:
            print("Ovaj deo ne")

    print(ispisPredmeta)

    beleske = pregledOcena.pregledBeleski(sifraUcenika)
    # print(beleske)
    listaBeleski = beleske.split("|")
    print(listaBeleski)
    stvariZaIspis = []
    for beleskaa in listaBeleski:
        beleske = beleskaa.split(';')
        print(beleske)
        try:
            stvariZaIspis.append((beleske[0], beleske[1], beleske[2], beleske[3], beleske[4], beleske[5]))
        except:
            print("Nema za ovo")
    if listaBeleski[0].startswith("Nema beleski"):
        stvariZaIspis = [(""," "," "," "," "," ")]
    print(len(stvariZaIspis))

    izostao = izostanci.pregledIzostanakaJedanUcenik(sifraUcenika)
    # print(izostao)

    sviIzostanci = izostao.split("|")
    print(sviIzostanci)
    izostanak = []
    try:
        for jedanIzostanak in sviIzostanci:
            jedanIzostanakk = jedanIzostanak.split(";")
            izostanak.append((jedanIzostanakk[0], jedanIzostanakk[1], jedanIzostanakk[2], jedanIzostanakk[3]))
    except:
        if len(izostanak) > 0:
            print(izostanak)
        else:
            izostanak = [("Ucenik nema izostanke", "", "", "")]

    napomene = pregledOcena.pregledNapomenaJedanUcenik(sifraUcenika)

    # print(napomene)

    podaciNapomena = napomene.split("|")
    print(podaciNapomena)

    napomeneZaIspis = []
    try:
        for jednaNapomena in podaciNapomena:
            jednaNapomenaa = jednaNapomena.split(";")
            napomeneZaIspis.append((jednaNapomenaa[0], jednaNapomenaa[1], jednaNapomenaa[2], jednaNapomenaa[3]))
    except:
        if len(napomeneZaIspis) > 0:
            print(napomeneZaIspis)
        else:
            napomeneZaIspis = [("Ucenik nije u napomenama", "", "", "")]



    return template("drugeStranice\\ucenik.tpl", pregleanjeOcena = ispisPredmeta, gledanjeBeleski = stvariZaIspis, izostanciUcenika = izostanak, listaNapomeni = napomeneZaIspis,kontrolni = najavljivanjeKontrlonih.pregledKontrolnihOdeljenje(request.forms.get("odeljenje")))


@post('/profesorProvera')
def profesorskaStranicaPrebacivanje():
    sifraProfesora = request.forms.get('sifraProfesora')
    odeljenje = request.forms.get('odeljenje')
    print("Podaci za profesora sa sifrom: " + sifraProfesora + ", iz odeljenja: " + odeljenje)

    gdePrebaciti = razredni.proveraZaSajt(sifraProfesora, odeljenje)
    if gdePrebaciti == "Vladanje":
        response.set_cookie("sifraProfesora", sifraProfesora)
        response.set_cookie("odeljenje", odeljenje)
        print("Prebacen direktor")
        return '<script>window.location = "/direktorstranica";alert("Prijavljenji ste kao direktor");</script>'
    elif gdePrebaciti == "Lose uneta sifra":
        print("Greska u unosu sifre")
        return '<script>window.location = "/";alert("Lose uneta sifra profesora");</script>'
    elif gdePrebaciti == "Los unos odeljenja":
        print("Greska u unosu odeljenja")
        return '<script>window.location = "/";alert("Los unos odeljenja");</script>'
    else:
        print("Prebacen profesor")
        response.set_cookie("sifraProfesora", sifraProfesora)
        response.set_cookie("odeljenje", odeljenje)
        return '<script>window.location = "/profesorstranica";alert("Prijavljenji ste kao profesor, predmet ' + str(gdePrebaciti) + '");</script>'

#DIREKTOR

@get('/direktorstranica')
def stranicaDirektora():
    if len(request.get_cookie("sifraProfesora")) != 7:
        return '<script>window.location = "/";alert("Niste prijavljenji.");</script>'
    else:
        return template('drugeStranice\\direktor.tpl', podaciProfesora = razredni.direktorGledaProfesore(request.get_cookie("sifraProfesora")), kojeOdeljenje = request.get_cookie("odeljenje"))


@post('/promenasifre')
def promenitiSifru():
    return '<script>window.location = "/direktorstranica";alert("' + razredni.promenaSifreProfesora(request.get_cookie("sifraProfesora"), request.forms.get("staraSifra"))+ '");</script>'


@post('/ispisprofesora')
def odeProfesor():
    return '<script>window.location = "/direktorstranica";alert("' + razredni.ispisProfesora(request.get_cookie("sifraProfesora"), request.forms.get("profesorSifra")) + '");</script>'


@post('/stoprazredni')
def nemaRazrednog():
    return '<script>window.location = "/direktorstranica";alert("' + razredni.prestajeRazredni(request.get_cookie("sifraProfesora"), request.forms.get("profesorSifra")) + '");</script>'


@post('/novrazredni')
def upisRazrednog():
    return '<script>window.location = "/direktorstranica";alert("' + razredni.dodelaRazrednih(request.get_cookie("sifraProfesora"), request.forms.get("profesorSifra"), request.forms.get("odeljenje")) + '");</script>'


@post("/dosaoprofesor")
def dosaoProfesor():
    return '<script>window.location = "/direktorstranica";alert("' + baze.upisProfesora(request.forms.get("ime"), str(request.forms.get("predmet")).title(), request.get_cookie("sifraProfesora")) + '");</script>'


@post('/upisatiucenika')
def noviUcenikDosao():
    try:
        return '<script>window.location = "/direktorstranica";alert("' + baze.ucenikDosao(request.forms.get("ime"),  request.forms.get("odeljenje"), request.get_cookie("sifraProfesora")) + '");</script>'
    except:
        return '<script>window.location = "/direktorstranica";alert("Greska prilikom unosa");</script>'



@post('/doslonovoodeljenje')
def novoOdeljenjeUpis():

    try:
        rezultat = baze.upisOdeljenja(request.forms.get("odeljenje"), request.forms.get("spisakPredmeta"),
                                      request.forms.get("spisakUcenika"), request.get_cookie("sifraProfesora"))
        print("OVO JE REZULTAT: \n" + str(rezultat))
        if rezultat == "Sve je dobro":
            return '<script>window.location = "/direktorstranica";alert("Sve je dobro");</script>'
        elif rezultat == "NE":
            return '<script>window.location = "/direktorstranica";alert("Ovo odeljenje vec postoji");</script>'
        else:
            return '<script>window.location = "/direktorstranica";alert("Greska prilikom unosa");</script>'
    except Exception as E:
        print("Doslo je do except greske \n " + str(E))
        return '<script>window.location = "/direktorstranica";alert("Greska prilikom unosa");</script>'


@post('/izracunajprossek')
def proeskRacunaj():
    return '<script>window.location = "/direktorstranica";alert("' + prosek.racunanjeProseka(request.get_cookie("sifraProfesora"), request.get_cookie("odeljenje")) + '");</script>'


@post('/odeodeljenje')
def odeljenjeObrisano():
    return '<script>window.location = "/";alert("' + razredni.obrisatiOdeljenje(request.get_cookie("sifraProfesora"), request.get_cookie("odeljenje")) + '");</script>'


#PROFESOR
@get('/profesorstranica')
def stranaProfesor():



    return template("drugeStranice\\profesor.tpl", sve= pregledOcena.pregledPredmeta(request.get_cookie("odeljenje"), request.get_cookie("sifraProfesora")), trenutnoOdeljenje = request.get_cookie("odeljenje"), kontrolniSvi = najavljivanjeKontrlonih.pregledanjeKontrlonih(request.get_cookie("sifraProfesora")), dalJeRazredni = razredni.profesorDalJeRazredni(request.get_cookie("sifraProfesora")))


@post("/upisatiocenu")
def ocenaUdnevnik():
    return '<script>window.location = "/profesorstranica";alert("' + upisOcena.upisOcene(request.get_cookie("sifraProfesora"), request.forms.get("ime"), request.get_cookie("odeljenje"), request.forms.get("ocena"), request.forms.get("beleskaOcene")) + '");</script>'



@post('/upisatiizostanak')
def upisatiIzostanakUceniku():
    return '<script>window.location = "/profesorstranica";alert("' + izostanci.upisIzostanaka(request.get_cookie("sifraProfesora"), request.forms.get("ime"), request.get_cookie("odeljenje")) + '");</script>'



@post('/upisatinapomenu')
def upisivanjeUnapomenu():
    print(request.forms.get("ime"))
    print(request.forms.get("zasto"))
    dalJeProslo = upisOcena.upisNapomena(request.get_cookie("sifraProfesora"), request.get_cookie("odeljenje"),str(request.forms.get("ime")), str(request.forms.get("zasto")))
    if dalJeProslo != "Doslo je do greske.":
        return '<script>window.location = "/profesorstranica";alert("Upisano u napomenu");</script>'
    else:
        return '<script>window.location = "/profesorstranica";alert("Greska u upisu");</script>'


@post("/zakazikontrolni")
def zakazivanjeKontrologZaOdeljenje():
    return '<script>window.location = "/profesorstranica";alert("' + najavljivanjeKontrlonih.zakazatiKontrolni(request.get_cookie("sifraProfesora"), request.get_cookie("odeljenje"),request.forms.get("datum")) + '");</script>'


@post("/ponistavanjekontrolnog")
def otkazatiKontrolniOdeljenju():
    return '<script>window.location = "/profesorstranica";alert("' + najavljivanjeKontrlonih.gotovKontrolni(request.get_cookie("sifraProfesora"), request.forms.get("sifraKontrolneVezbe")) + '");</script>'


@get('/mojeodeljenje')
def pogledatiOdeljenje():

    izostanciOdeljenja = razredni.izostanciRazredni(request.get_cookie("sifraProfesora"))
    print(izostanciOdeljenja)
    print(type(izostanciOdeljenja))
    stavkeOdeljenja = razredni.pregledSvogodeljenja(request.get_cookie("sifraProfesora"))
    return template("drugeStranice\\pregledRazredna.tpl", predmeti = stavkeOdeljenja[0], ucenici = stavkeOdeljenja[1], izostanciUcenika = izostanciOdeljenja, napomene = razredni.razredniGledaNapomene(request.get_cookie("sifraProfesora")))


@post('/pravdanjejedan')
def opravdatiJedanIzostanak():
    return '<script>window.location = "/mojeodeljenje";alert("' + izostanci.pravdanjeJednogIzostanka(request.get_cookie("sifraProfesora"), request.forms.get("sifraIzostanka")) + '");</script>'


@post('/pravdanjedana')
def opravdatiJedanIzostanak():
    return '<script>window.location = "/mojeodeljenje";alert("' + izostanci.pravdanjeDanaJedanUcenik(request.get_cookie("sifraProfesora"), request.forms.get("sifraUcenika"), request.forms.get("datum")) + '");</script>'

# POKRETANJE
run(host='127.0.0.1', port=8000, reloader = True, debug = True)
