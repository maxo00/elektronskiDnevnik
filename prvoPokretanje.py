import sqlite3
import baze
import najavljivanjeKontrlonih
import izostanci
import upisOcena
import os


def zapocni():

    try:
        baza = sqlite3.connect("dnevnik.db")
        kontrola = baza.cursor()
        kontrola.execute("SELECT sifraProfesora FROM Profesori")
        ima = kontrola.fetchone()[0]
        nastaviti = input("Dnevnik je vec napravljen zelite li da ga obrisete(da/ne): ").upper()
        if nastaviti == "DA":
            os.remove("dnevnik.db")
            return print("Dnevnik obrisan, zapocnite program ponovo da kreirate novi.")
        return print("Nista nije promenjeno")
    except:
        print("Kreiranje novog dnevnika")
        baze.stvaranjeProfesora()
        najavljivanjeKontrlonih.stvaranjeTabeleKontrolnih()
        upisOcena.stvaranjeNapomena()
        upisOcena.stvaranjeBeleski()
        izostanci.stvaranjeIzostanaka()
        print("Sve je kreirano mozete se prijaviti kao direktor i urediti profesore i odeljenja nakon pokretanja sajtBackend.py")

zapocni()