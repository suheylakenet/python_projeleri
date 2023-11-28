import random

isimler = ["süheyla" ,"onur", "cahide", 
           "buse", "merve" , "ecmel"]

def hediye_cekilisi():
    alanlar= isimler.copy()
    verenler=isimler.copy()
    while len(alanlar)>0:
        alici_index =random.randint(0, len(alanlar)-1)
        verici_index=random.randint(0, len(alanlar)-1)
        
        while alanlar[alici_index]== verenler[verici_index]:
            alici_index =random.randint(0, len(alanlar)-1)
            verici_index=random.randint(0, len(alanlar)-1)


        print(alanlar[alici_index], "şu kişiye hediye alcak", verenler[verici_index])
        del alanlar[alici_index]
        verenler.remove(verenler[verici_index])


hediye_cekilisi()
