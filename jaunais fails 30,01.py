def ierakstit(teksts, faila_nosaukums):
    fails =  open(faila_nosaukums, "w", encoding= 'utf-8')
    fails.write(teksts)
    fails.close()
   

           
def ierakstit(teksts, faila_nosaukums):
    fails =  open(faila_nosaukums, "w", encoding= 'utf-8')
    fails.write(teksts)
    fails.close()

def nolasit(faila_nosaukums):
    with open(faila_nosaukums, "r", encoding= "utf-8") as
        saturs= fails.read()
    print(saturs)
   
pierakstit("sveiki, visi!\n \"\n", "faili/teksts.txt")