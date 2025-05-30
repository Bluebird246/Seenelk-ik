import pygame, sys, random, time

pygame.init()
screen = pygame.display.set_mode([1090, 640])
pygame.display.set_caption("Seiklusmäng")

screen_width, screen_height = screen.get_size()

def küsi_valikut(pildi_aadress, küsimus, valikud):
    pilt = pygame.image.load(pildi_aadress)
    laius = pilt.get_width()
    kõrgus = pilt.get_height()

    myfont = pygame.font.SysFont("monospace", 32, bold=True)
    myfont2 = pygame.font.SysFont("monospace", 24, bold=True, italic=False)

    question = myfont2.render(küsimus, 1, (255,225,225))
    labels = [myfont.render(e, 1, (255,255,255)) for e in valikud]
    labels_select = [myfont.render(e, 1, (255,0,0)) for e in valikud]

    while True:
        x, y = pygame.mouse.get_pos()

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if i.type == pygame.MOUSEBUTTONDOWN:
                for j in range(len(valikud)):
                    valiku_y = kõrgus + 150 + 50 * j
                    if valiku_y < y < valiku_y + 32:
                        return valikud[j]

        screen.fill([0,0,0])
        screen.blit(pilt, [0, 0])
        screen.blit(question, (20, kõrgus + 50))

        for j in range(len(labels)):
            valiku_y = kõrgus + 140 + 50 * j
            if valiku_y < y < valiku_y + 32:
                screen.blit(labels_select[j], (50, valiku_y))
            else:
                screen.blit(labels[j], (50, valiku_y))

        pygame.display.flip()
        pygame.time.delay(16)

def näita_teadet(pildi_aadress, teade):
    küsi_valikut(pildi_aadress, teade, ["Edasi"])

def täringu_veeretus(dc):
    lõpptulemus = random.randint(1, 20)
    muutuv_tulemus = 1
    animatsiooni_kestus = 2.5
    alg_kiirus = 0.05
    aeglustus = 0.2

    myfont = pygame.font.SysFont("monospace", screen_width // 10, bold=True)
    tulemus_font = pygame.font.SysFont("monospace", screen_width // 30, bold=True)

    start_aeg = time.time()
    current_kiirus = alg_kiirus

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if time.time() - start_aeg > animatsiooni_kestus:
            break

        muutuv_tulemus = random.randint(1, 20)
        screen.fill((0, 0, 0))
        tekst = myfont.render(f"{muutuv_tulemus}", True, (255, 255, 255))
        screen.blit(tekst, (screen_width // 2 - tekst.get_width() // 2, screen_height // 3))
        pygame.display.flip()

        time.sleep(current_kiirus)
        current_kiirus += aeglustus * current_kiirus

    # Kuvame lõpliku tulemuse
    screen.fill((0, 0, 0))
    lõplik_tekst = myfont.render(f"{lõpptulemus}", True, (0, 255, 0))
    dc_tekst = tulemus_font.render(f"Eesmärk (DC): {dc}", True, (200, 200, 200))

    if lõpptulemus >= dc:
        tulemus_tekst = tulemus_font.render("Õnnestus!", True, (0, 255, 0))
    else:
        tulemus_tekst = tulemus_font.render("Ei õnnestunud.", True, (255, 0, 0))

    # Paiguta tekstid keskmesse
    screen.blit(lõplik_tekst, (screen_width // 2 - lõplik_tekst.get_width() // 2, screen_height // 4))
    screen.blit(dc_tekst, (screen_width // 2 - dc_tekst.get_width() // 2, screen_height // 4 + 100))
    screen.blit(tulemus_tekst, (screen_width // 2 - tulemus_tekst.get_width() // 2, screen_height // 4 + 150))

    pygame.display.flip()
    time.sleep(2)

    return lõpptulemus >= dc
