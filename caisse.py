print("""Bienvenue chez nous !!
Veuillez entrer les couts des produits 1 par 1, 
et quand vous finissez tapez un nombre negative ou egal a 0
si vous tapez un nombre negative mn depart le programme sarettera
Merci !""")

C = 1
S = 0
print("entrer le cout d'achat du produit 1 :")
prix = int(input())

if prix <= 0:
    while True :
        print("tapez un montant positive SVP !!")
        prix = int(input())
        if prix > 0:
            S += prix
            print("la somme precedente apres lentree negative est :",S,)
            break


        
if prix > 0:
    while True:         # en utilisant tanque
        C += 1
        print("entrer le cout d'achat du produit",C,":")
        prix = int(input())
        if prix <= 0:
            break
        else:
            S = S + prix

    if C >= 2 :
        print("la somme des produits est :", S)
        monnaie = int(input("entrer votre monnaie SVP : "))

        if monnaie <= 0 :
            while monnaie <= 0:
                monnaie = int(input("veuillez tapez un montant positive : "))    
                if monnaie > 0 and monnaie < S:
                    while monnaie < S :    # tand que monnaie < S, faire ces deux "si" jusqua
                                        # monnaie devient plus grand que S
                        addition = int(input("veuillez ajouter l'argent"))
                        if addition <= 0 :
                            while addition <= 0:
                                addition = int(input("le nombre ajoute est negative !!\n veuillez entrer un positive !"))
                        if addition > 0:
                            monnaie += addition

        elif monnaie > 0 and monnaie < S:
            while monnaie < S :    # tand que monnaie < S, faire ces deux "si" jusqua
                                # monnaie devient plus grand que S
                addition = int(input("veuillez ajouter l'argent"))
                if addition <= 0 :
                    while addition <= 0:
                        addition = int(input("le nombre ajoute est negative !!\n veuillez entrer un positive !"))
                else :                  
                    monnaie += addition

    if monnaie == S:
        print("merci pour votre visite")
        SystemExit
        

    elif monnaie > S :
        remise = monnaie - S
        print("la remise est de ",remise,"Dh")

        if remise >= 200:
            nbf200 = remise // 200
            reste = remise % 200
            print("nombre de feuille de 200 dh est : ",nbf200)
            remise = reste

        if remise >= 100 :
            reste = remise - 100
            print("nombre de feuille de 100 dh est : 1")      
            remise = reste

        if remise >= 50:
            reste = remise - 50
            print("nombre de feuille de 50 dh est : 1")       
            remise = reste

        if remise >= 40:
            reste = remise - 40
            print("nombre de feuille de 20 dh est : 2")        
            remise = reste

        if remise >= 20:
            reste = remise - 20
            print("nombre de feuille de 20 dh est : 1")        
            remise = reste

        if remise >= 10:
            reste = remise - 10
            print("nombre de pieces de 10 dh est : 1")        
            remise = reste

        if remise >= 5:
            reste = remise - 5
            print("nombre de pieces de 5 dh est : 1")       
            remise = reste

        if remise >= 4:
            print("nombre de pieces de 2 dh est : 2")
            SystemExit

        if remise >= 2:
            reste = 1
            print("nombre de pieces de 2 dh est : 1")
            remise = reste

        if remise >= 1:
            print("nombre de pieces de 1 dh est : 1")
            
        print("merci pour votre visite")
        SystemExit
