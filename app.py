import random

def jeu_code_secret():
    # Le code secret à deviner
    code = "218" 
    tentatives = 0
    
    print("Bienvenue au Code Secret. Le code est un nombre à 3 chiffres.")

    while True:
        tentatives += 1
        
        # Demander la proposition de l'utilisateur
        proposition = input(f"\nTentative #{tentatives} (3 chiffres) : ")
        
        # Vérification de base (à améliorer dans le vrai code)
        if len(proposition) != 3 or not proposition.isdigit():
            print("Veuillez entrer un nombre valide à 3 chiffres.")
            continue
            
        bulls = 0
        cows = 0

        # Calcul des Bulls (chiffre ET position corrects)
        for i in range(3):
            if proposition[i] == code[i]:
                bulls += 1

        # Calcul des Cows (chiffre correct, mauvaise position)
        for p_chiffre in proposition:
            if p_chiffre in code:
                # Si le chiffre est dans le code, on vérifie s'il est mal placé (si ce n'est pas un Bull)
                est_bull = False
                for i in range(3):
                    if p_chiffre == code[i] and proposition[i] == code[i]:
                        est_bull = True
                        break
                
                # Un chiffre ne peut pas être à la fois un Bull et un Cow
                if not est_bull:
                    cows += 1
        
        # Le calcul de 'cows' est souvent plus simple en soustrayant les Bulls:
        # cows = (nombre total de chiffres en commun) - bulls
        
        total_chiffres_communs = 0
        for p_chiffre in proposition:
             if p_chiffre in code:
                 total_chiffres_communs += 1
        
        cows = total_chiffres_communs - bulls


        if bulls == 3:
            print(f"\nFélicitations ! Vous avez trouvé le code {code} en {tentatives} tentatives !")
            break
        else:
            print(f"Résultat : {bulls} Bulls, {cows} Cows.")

# Lancez la fonction pour jouer
# jeu_code_secret()
