from alus2 import *
import pygame

while True:
    näita_teadet("mets1.jpeg", "Sõitsid vihmasel sügisõhtul metsa, et seeni korjata. Kahjuks läks auto\nkatki ja tee peale kukkus veel ka puu.")

    valik1 = küsi_valikut("puu.jpeg", "Kas proovid liigutada puud?", ["Jah, ma olen väga tugev", "Ei, see on raske"])

    if valik1 == "Jah, ma olen väga tugev":
        näita_teadet("puu.jpeg", "Kasutad oma jõudu, et puud liigutada.")
        õnnestus = täringu_veeretus(15)

        if õnnestus:
            valik = küsi_valikut("kodu.jpeg", "Sul õnnestus puud liigutada! Saad koju kõmpida. \nKas soovid mängu lõpetada või uuesti proovida?", ["Lõpeta", "Proovi uuesti!"])
            if valik == "Lõpeta":
                break
            else:
                continue
        else:
            näita_teadet("puu.jpeg", "Sul ei õnnestunud puud liigutada. Pead liikuma metsa sisse.")
    else:
        näita_teadet("metsatee.jpeg", "Oled juba pikemat aega kõndinud. Mets on muutunud pimedaks ja oled eksinud.")

    valik2 = küsi_valikut("metsatee.jpeg", "Kuuled kauguses karjet. Kuidas käitud?", ["Jätkan mööda teed", "Liigun karje poole"])

    if valik2 == "Jätkan mööda teed":
        näita_teadet("metsamaja.jpeg", "Jätkad mööda teed ja leiad hütikese.")
        valik3 = küsi_valikut("metsamaja.jpeg", "Kas sisened hütti või jätkad mööda teed edasi?", ["Sisenen", "Jätkan mööda teed"])

        if valik3 == "Sisenen":
            näita_teadet("kollmajas.jpeg", "Hütti sisse astudes näed ukse taga liikuvat mass. See aga murdis \nläbi ukse ning liigub kiiresti sinu poole. Kas oled valmis selleks?")
            õnnestus = täringu_veeretus(15)

            if õnnestus:
                valik = küsi_valikut("hütt.jpeg", "Sa alistad koletise ja saad hütti jääda, ning hommikul koju minna. \nKas soovid mängu lõpetada või uuesti proovida?", ["Lõpeta", "Proovi uuesti!"])
                if valik == "Lõpeta":
                    break
                else:
                    continue
            else:
                näita_teadet("metsamaja.jpeg", "Koletis ründab sind. Kahjuks sa sured.")
                valik = küsi_valikut("metsamaja.jpeg", "Kas soovid proovida uuesti või lõpetada?", ["Proovi uuesti!", "Lõpeta"])
                if valik == "Lõpeta":
                    break
                else:
                    continue

        elif valik3 == "Jätkan mööda teed":
            näita_teadet("metsatee.jpeg", "Jõuad surnukehani. Sa pole kindel kas see on väsimus, aga nägid seda \nvist veidi liigutamas.")
            valik4 = küsi_valikut("surnu.jpeg", "Kas ignoreerid keha ja liigud edasi või jääd seisma ja otsid keha läbi?", ["Ignoreerin", "Jään seisma"])

            if valik4 == "Ignoreerin":
                näita_teadet("metsatee.jpeg", "Ignoreerid surnukeha ning liigud edasi. Kõndides hakkab aga sul \nkõht korisema ja nälg on. Näed kauguses seeni.")
                valik5 = küsi_valikut("seen.jpeg", "Kas sa sööd seeni?", ["Jah", "Ei"])

                if valik5 == "Jah":
                    õnnestus = täringu_veeretus(10)
                    if õnnestus:
                        näita_teadet("seen.jpeg", "Seened olid söödavad ja said kõhu täis. Jätkad metsas liikumist.")
                    else:
                        näita_teadet("seen.jpeg", "Seen osutub mürgiseks ja sa sured seal samas.")
                        valik = küsi_valikut("metsatee.jpeg", "Kas soovid proovida uuesti või lõpetada?", ["Proovi uuesti!", "Lõpeta"])
                        if valik == "Lõpeta":
                            break
                        else:
                            continue

                    näita_teadet("metsatee.jpeg", "Leiad metsast jahimehe, kes pakub sulle võimalust, et viib su koju.")
                    valik6 = küsi_valikut("metsatee.jpeg", "Kas lähed temaga?", ["Jah", "Ei"])

                    if valik6 == "Jah":
                        näita_teadet("kodu.jpeg", "Jõuad koos temaga ilusti koju.")
                        break
                    else:
                        näita_teadet("karu.jpeg", "Keeldud ja kõnnid metsas edasi. On kottpime ning jalutad \nkarule otsa. Ta sööb su ära.")
                        valik = küsi_valikut("karu.jpeg", "Kas soovid proovida uuesti või lõpetada?", ["Proovi uuesti!", "Lõpeta"])
                        if valik == "Lõpeta":
                            break
                        else:
                            continue
                elif valik5 == "Ei":
                    näita_teadet("metsatee.jpeg", "Leiad metsast jahimehe, kes pakub sulle võimalust, et viib su koju.")
                    valik6 = küsi_valikut("metsatee.jpeg", "Kas lähed temaga?", ["Jah", "Ei"])
                    if valik6 == "Jah":
                        näita_teadet("kodu.jpeg", "Jõuad koos temaga ilusti koju")
                        break
                    else:
                        näita_teadet("karu.jpeg", "Keeldud ja kõnnid metsas edasi. On kottpime ning jalutad karule otsa. \nTa sööb su ära.")
                        valik = küsi_valikut("karu.jpeg", "Kas soovid proovida uuesti või lõpetada?", ["Proovi uuesti!", "Lõpeta"])
                        if valik == "Lõpeta":
                            break
                        else:
                            continue

            elif valik4 == "Jään seisma":
                näita_teadet("surnu.jpeg", "Keha hüppab sulle kõrri. Sa sured.")
                valik = küsi_valikut("metsatee.jpeg", "Kas soovid proovida uuesti või lõpetada?", ["Proovi uuesti!", "Lõpeta"])
                if valik == "Lõpeta":
                    break
                else:
                    continue

    elif valik2 == "Liigun karje poole":
        näita_teadet("metsatee.jpeg", "Liigud sügavamale metsa ja näed surnukeha.")
        valik8 = küsi_valikut("surnu.jpeg", "Kas jooksed minema või otsid keha läbi?", ["Jooksen minema", "Otsin keha läbi"])

        if valik7 == "Jooksen minema":
            näita_teadet("lõks.jpeg", "Joostes ei pane sa tähele suurt lõksu maas. Astud sellele otsa ning sured.")
            valik = küsi_valikut("lõks.jpeg", "Kas soovid proovida uuesti või lõpetada?", ["Proovi uuesti!", "Lõpeta"])
            if valik == "Lõpeta":
                break
            else:
                continue

        elif valik7 == "Otsin keha läbi":
            näita_teadet("raadio.jpeg", "Leiad raadiosaatja. Kutsud abi aga see jõuab alles hommikul. Pead öö \nüle elama.")
            õnnestus = täringu_veeretus(10)
            if õnnestus:
                näita_teadet("hommik.jpeg", "Elad öö üle ja sind päästetakse.")
                valik = küsi_valikut("hommik.jpeg", "Kas soovid mängu lõpetada või uuesti proovida?", ["Lõpeta", "Proovi uuesti!"])
                if valik == "Lõpeta":
                    break
                else:
                    continue
            else:
                näita_teadet("külm.jpeg", "Sa ei ela külma ööd üle. Said surma!")
                valik = küsi_valikut("külm.jpeg", "Kas soovid proovida uuesti või lõpetada?", ["Proovi uuesti!", "Lõpeta"])
                if valik == "Lõpeta":
                    break
                else:
                    continue

pygame.quit()
