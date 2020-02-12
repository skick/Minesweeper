import random
import time


"""  Miinaharavapeli   """


def miinaharava():
    """ Pelisilmukka on tässä funktiossa """
    nimimerkki = input("Anna nimimerkki: ")
    miinojen_maara, b, a = kysy_kentta()
    miina_kentta, pelaaja_kentta = rakenna_kentat(a, b)
    miinoita_kentta(miina_kentta, miinojen_maara)
    laske_numerot(miina_kentta)
    tulosta_kentta(pelaaja_kentta)
    alku = time.time()
    while True:
        x, y = kysy_koordinaatit(pelaaja_kentta)
        print()
        arvo = avaa_ruutuja(pelaaja_kentta, miina_kentta, x, y)
        if arvo == False:
            tulosta_kentta(miina_kentta)
            print("Hävisit pelin!")
            tulos = "Häviö"
            break
        elif arvo == True:
            tulosta_kentta(pelaaja_kentta)
            print("Voitit pelin!")
            tulos = "Voitto"
            break
        tulosta_kentta(pelaaja_kentta)

    loppu = time.time()
    aika = loppu - alku
    print("Pelissä kesti {:.1f} sekuntia!".format(aika))
    korkeus = len(miina_kentta)
    leveys = len(miina_kentta[0])
    aika = str(aika)
    pvmtulos = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    tiedot = []
    tulokset = (nimimerkki, aika, tulos, miinojen_maara, leveys, korkeus, pvmtulos)
    tiedot.append(tulokset)
    return tiedot

def miinoita_kentta(miina_kentta, miinojen_maara):
    """ Miinoittaa kentän """

    korkeus = len(miina_kentta)
    leveys = len(miina_kentta[0])
    vapaat = []

    for y in range(korkeus):
        for x in range(leveys):
            vapaat.append((x, y))
    for i in range(miinojen_maara):
        xy = random.randint(0, len(vapaat) - 1)
        x = vapaat[xy][0]# x-koordinaatti
        y = vapaat[xy][1]# y-koordinaatti
        miina_kentta[y][x] = "X"
        del vapaat[xy]

def laske_numerot(miina_kentta):
    """ Laskee miinojen ympärillä olevien ruutujen numerot ja asettaa numeroruudut miinakentälle. """
    korkeus = len(miina_kentta)
    leveys = len(miina_kentta[0])
    vapaat = []
    for y in range(korkeus):
        for x in range(leveys):
            vapaat.append((x, y))
    while True:
        if vapaat == []:
            break
        xy1 = vapaat.pop()
        x = xy1[0]
        y = xy1[1]
        miinat = 0
        if miina_kentta[y][x] == "X":
            continue
        for rivi in range(y - 1, y + 2):
            if rivi < 0 or rivi > korkeus - 1:
                pass
            else:
                for solu in range(x - 1, x + 2):
                    if solu < 0 or solu > leveys - 1:
                        pass
                    else:
                        if miina_kentta[rivi][solu] == "X":
                            if rivi == y and solu == x:
                                pass
                            else:
                                miinat = miinat + 1
        if miinat > 0:
            miinat = str(miinat)
            miina_kentta[y][x] = miinat
    return

def kysy_kentta():
    """ Kysyy pelaajalta halutun kentän koon ja miinojen määrän """
    while True:
        try:
            leveys = int(input("Anna kentän leveys: "))
            korkeus = int(input("Anna kentän korkeus: "))
        except ValueError:
            print("Leveyden ja korkeuden täytyy olla kokonaislukuja!")
            continue
        if leveys < 1 or korkeus < 1:
            print("Leveyden ja korkeuden tulee olla suurempia kuin 0!")
            continue
        else:
            break
    while True:
        try:
            miinojen_maara = int(input("Anna miinojen määrä: "))
        except ValueError:
            print("Miinojen määrä täytyy olla kokonaisluku!")
            continue
        if miinojen_maara < 0:
            print("Miinojen määrä täytyy olla positiivinen luku!")
            continue
        else:
            break

    return miinojen_maara, leveys, korkeus

def kysy_koordinaatit(pelaaja_kentta):
    """ Kysyy pelaajalta avattavan ruudun koordinaatit. """
    korkeus = len(pelaaja_kentta)
    leveys = len(pelaaja_kentta[0])
    while True:
        try:
            xy = (input("Anna koordinaatit välilyönnillä eroitettuna:  "))
            xy1 = xy.split(" ")
            xy2 = [int(i) for i in xy1]
            if len(xy2) != 2:
                print("Anna koordinaatit välilyönnillä eroitettuna!")
                continue
            elif xy2[0] < 0 or xy2[1] < 0:
                print("Anna positiiviset kokonaisluvut!")
                continue
            elif xy2[0] > leveys - 1 or xy2[1] > korkeus - 1:
                print("Antamasi koordinaatit ovat kentän ulkopuolella!")
                continue
            else:
                pass
        except ValueError:
            print("Anna koordinaatit kokonaislukuina!")
            continue
        else:
            x = xy2[0]
            y = xy2[1]
            return x, y

def tulosta_kentta(kentta):
    """ Tulostaa pelattavan kentän """
    leveys = len(kentta[0])
    a = 0
    for rivi in kentta:
        if a == 0:
            printtirivi1 = ""
            printtirivi2 = ""
            for i in range(leveys):
                i = str(i)
                printtirivi1 = printtirivi1 + " " + " " + i + " "
                printtirivi2 = printtirivi2 + "----"
            print("     {} ".format(printtirivi1))
            print("     {}-".format(printtirivi2))
        printtirivi1 = ""
        printtirivi2 = ""
        for solu in rivi:
            printtirivi1 = printtirivi1 + "|" + " " + solu + " "
            printtirivi2 = printtirivi2 + "----"
        print("{:4d} {}|".format(a, printtirivi1))
        print("     {}-".format(printtirivi2))
        a = a + 1

def rakenna_kentat(a, b):
    """ Luo pelattavan kentän ja miinakentän """
    """ a = korkeus ja b = leveys"""
    miina_kentta = []
    pelaaja_kentta = []
    for rivi in range(a):
        miina_kentta.append([])
        for sarake in range(b):
            miina_kentta[-1].append("o")
    for rivi in range(a):
        pelaaja_kentta.append([])
        for sarake in range(b):
            pelaaja_kentta[-1].append("o")
    return miina_kentta, pelaaja_kentta

def avaa_ruutuja(pelaaja_kentta, miina_kentta, x, y):
    """ Avaa ruutuja kentästä. """
    korkeus = len(miina_kentta)
    leveys = len(miina_kentta[0])

    #Jos avaat miinan, peli loppuu.
    if miina_kentta[y][x] == "X":
        return False

    alue = [(x, y)]
    a = 0
    while True:
        if a == 0:
            # Jos avaat "numeron" muut ruudut eivät avaannu.
            if not miina_kentta[y][x] == "o":
                pelaaja_kentta[y][x] = miina_kentta[y][x]
                break
        elif alue == []:
            # Lopettaa loopin kun avattavia ruutuja ei enää löydy.
            break
        xy = alue.pop()
        x = xy[0]
        y = xy[1]
        pelaaja_kentta[y][x] = " "
        miina_kentta[y][x] = " "
        # Etsii avattavat ruudut vierestä:
        for rivi in range(y - 1, y + 2):
            if rivi < 0 or rivi > korkeus - 1:
                pass
            else:
                for solu in range(x - 1, x + 2):
                    if solu < 0 or solu > leveys - 1:
                        pass
                    else:
                        if miina_kentta[rivi][solu] == "o":
                            if rivi == y and solu == x:
                                pass
                            else:
                                koordinaatit = (solu, rivi)
                                alue.append(koordinaatit)
                        elif miina_kentta[rivi][solu] != "X" and miina_kentta[rivi][solu] != "o":
                            pelaaja_kentta[rivi][solu] = miina_kentta[rivi][solu]
                        else:
                            pass
        a = a + 1
    i = sum(rivi.count("o") for rivi in pelaaja_kentta)
    j = sum(rivi.count("X") for rivi in miina_kentta)
    if i == j:
        return True

def tallenna_tiedot(tiedot, tiedosto):
    """ Tallentaa tulokset tiedostoon. """
    with open(tiedosto, "a") as tulokset:
        for rivi in tiedot:
            line = ""
            i = 0
            for solu in rivi:
                i = i + 1
                solu = str(solu)
                if i != 7:
                    line = line + solu + "/"
                else:
                    line = line + solu + "|"
            tulokset.write(line)

def tulosta_tiedot(tiedosto):
    """ Tulostaa tulokset pelaajalle. """
    try:
        with open (tiedosto, "r") as tulokset:
            for line in tulokset.read().split("|"):
                if line == "":
                    break
                line = str.strip(line)
                tiedot = line.split("/")
                tulos = tiedot[2]
                nimi = tiedot[0].strip()
                aika = float(tiedot[1])
                maara = tiedot[3]
                leveys = tiedot[4]
                korkeus = tiedot[5]
                pvmtulos = tiedot[6]
                print("{} | {} {:.1f}s - {} | Miinojen määrä: {}, kentän koko: {}x{}".format(pvmtulos, tulos, aika, nimi, maara, leveys, korkeus))
            input("Paina jotain näppäintä")
    except FileNotFoundError:
        print()
        print()
        print("Tuloksia ei ole.")
        return








while True:
    print()
    print()
    print("Miinaharavapeli")
    print()
    print("Mahdolliset toiminnot:")
    print("(P)elaa")
    print("(T)ulokset")
    print("(L)opeta")
    print()
    valinta = input("Tee valintasi: ").strip().lower()

    if valinta == "p" or valinta == "pelaa":
        tiedot = miinaharava()
        print("Haluatko tallentaa tuloksesi?")

        while True:
            valinta1 = input("Valitse (K)yllä / (E)i: ").strip().lower()
            if valinta1 == "k" or valinta == "kyllä":
                tallenna_tiedot(tiedot, "tulokset.txt")
                print("Tulos on tallennettu.")
                break
            elif valinta1 == "e" or valinta == "ei":
                break
            else:
                print("Valitsemaasi toimintoa ei ole olemassa!")
                continue


    elif valinta == "t" or valinta == "tulokset":
        tulosta_tiedot("tulokset.txt")

    elif valinta == "l" or valinta == "lopeta":
        break

    else:
        print("Valitsemaasi toimintoa ei ole olemassa")




""" Jonne Taipale """