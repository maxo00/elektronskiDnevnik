import pregledOcena

vracanje = pregledOcena.pregledPredmeta(36, "1234567")
poJedan = vracanje.split("|")

sviUcenici = []
for ucenik in poJedan:
    if ucenik == "":
        continue
    trenutno = ucenik.split(": ")
    sviUcenici.append((trenutno[0], trenutno[1]))

print(sviUcenici)