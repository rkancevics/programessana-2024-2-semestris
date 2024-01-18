def dienas_mekletajs (sis_gads, sis_menesis, sis_datums, si_diena, dz_gads, dz_menesis, dz_datums):
    menesu_dienu_skaits = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dienu_nosaukumi = ["nekas", "pirmdiena", "otrdiena", "trešdiena", "ceturtdiena", "piektdiena", "sestdiena", "svētdiena"]
    
    #Skaitām, cik dienas ir pagājušas
    #Pārbaude, vai šogad jau ir bijusi dzimšanas diena
    

    pagajusas_dienas = 0
    pagajusie_gadi = sis_gads-dz_gads

    if vai_datums_pagajis(sis_menesis, sis_datums, dz_menesis, dz_datums) == False:
        pagajusie_gadi -=1

    pagajusas_dienas += 365*pagajusie_gadi

    garie_gadi = 0
    sakuma_gads = dz_gads
    if vai_datums_pagajis(dz_menesis, dz_datums, 2, 29):
        sakuma_gads +=1

    beigu_gads = sis_gads
    if vai_datums_pagajis(sis_menesis, sis_datums, 2, 29) == False:
        beigu_gads -=1


    for gads in range (sakuma_gads, beigu_gads+1):
        if gads % 4 == 0:
            garie_gadi +=1
        if gads % 100 == 0 and gads % 400 != 0:
            garie_gadi -=1

    pagajusas_dienas += garie_gadi

    # cik pilni mēneši ir pagājuši kopš pēdējās dzimšanas dienas?
    if sis_menesis>=dz_menesis:
        pilni_menesi = sis_menesis-dz_menesis
    else:
        pilni_menesi = sis_menesis+12-dz_menesis

    if vai_datums_pagajis(1, sis_datums, 1, dz_datums) == False:
        pilni_menesi = pilni_menesi - 1

    dienas_menesos = 0

    menesis = dz_menesis
    while menesis != sis_menesis:
        print("Šis:", sis_menesis)
        dienas_menesos += menesu_dienu_skaits[menesis]
        print("skaititajs:", menesis)
        menesis +=1
        if menesis == 13:
            menesis=1

    pagajusas_dienas += dienas_menesos

    if sis_datums>=dz_datums:
        ekstra_dienas = sis_datums-dz_datums
    else:
        ekstra_dienas = sis_datums + menesu_dienu_skaits[sis_menesis-1] - dz_datums

    pagajusas_dienas += ekstra_dienas

    print("Kopš dzimšanas ir pagājušas: ", pagajusas_dienas, " dienas.")
    # cik dienas ir kopā pa tiem mēnešiem?
    # cik dienas ir pagājušas nepilnajā mēnesī?

    dienu_atlikums = pagajusas_dienas % 7

    dz_diena = si_diena-dienu_atlikums
    
    if dz_diena <=0:
        dz_diena +=7

    print("Jums ir ", pagajusie_gadi, " gadi, ", pilni_menesi, " menesi un ", ekstra_dienas, " dienas")


    return dienu_nosaukumi[dz_diena]


def vai_datums_pagajis(tagad_menesis, tagad_datums, salidzinamais_menesis, salidzinamais_datums):
    if tagad_menesis>salidzinamais_menesis:
        return True
    if tagad_menesis<salidzinamais_menesis:
        return False
    if tagad_datums>salidzinamais_datums:
        return True
    return False
    
def datu_parbaude (gads_dz, menesis_dz, datums_dz, gads_sis, menesis_sis, datums_sis, diena_sis):
    pareizi_dati = True
    if gads_dz<=0 or menesis_dz<=0 or datums_dz<=0 or gads_sis<=0 or menesis_sis<=0 or datums_sis<=0 or diena_sis<=0:
        pareizi_dati = False
    
    #Visas citas datu pārbaudes

    if pareizi_dati == False:
        print("Nepareizi ievades dati!")
    return pareizi_dati


atbilde = "y"
while atbilde == "y":
    dz_g = int(input("Lūdzu ievadiet savu dzimšanas gadu!:"))
    dz_m = int(input("Lūdzu ievadiet savu dzimšanas mēnesi!:"))
    dz_d = int(input("Lūdzu ievadiet savu dzimšanas datumu!:"))
    sis_g = int(input("Lūdzu ievadiet pašreizējo gadu!:"))
    sis_m = int(input("Lūdzu ievadiet pašreizējo mēnesi!:"))
    sis_d = int(input("Lūdzu ievadiet pašreizējo datumu!:"))
    sis_n = int(input("Lūdzu ievadiet pašreizējo nedēļas dienu!:"))
    if datu_parbaude(dz_g, dz_m, dz_d, sis_g, sis_m, sis_d, sis_n):
        print(dienas_mekletajs(sis_g, sis_m, sis_d, sis_n, dz_g, dz_m, dz_d))
    atbilde = input("Vai mēģināt vēlreiz? ('y'/'n')")