import random

def calculer_bulls_cows(code_secret, proposition):
    """
    Calcule le nombre de Bulls (chiffre et position corrects) 
    et de Cows (chiffre correct, mauvaise position).
    """
    bulls = 0
    cows = 0
    
    # Étape 1: Calcul des Bulls
    # Vérifie si le chiffre est le même ET à la même position
    for i in range(len(code_secret)):
        if proposition[i] == code_secret[i]:
            bulls += 1
            
    # Étape 2: Calcul des Cows
    # Vérifie si le chiffre est dans le code MAIS n'est PAS un Bull
    for chiffre_prop in proposition:
        if chiffre_prop in code_secret:
            # S'il est dans le code, il contribue au décompte total des chiffres corrects.
            cows += 1
            
    # Les Bulls sont comptés dans le décompte des Cows à l'étape 2. 
    # Pour obtenir les 'vraies' Cows (mal placées), on retire les Bulls.
    cows = cows - bulls
            
    return bulls, cows

def jeu_code_secret():
    # Définition du code secret
    code = "218" 
    tentatives = 0
    
    print("====================================")
    print("         CODE SECRET 218            ")
    print("====================================")
    print("Le code secret est un nombre à 3 chiffres (218).")
    print("Les indices sont donnés en Bulls (chiffre correct/bonne place) et Cows (chiffre correct/mauvaise place).")
    
    # --- AJOUT DE COMPLEXITÉ (Indice initial) ---
    print("\n--- Indice pour joueurs avancés ---")
    print("Le chiffre des dizaines (la position du '1') est un chiffre impair.")
    print("----------------------------------\n")


    while True:
        tentatives += 1
        
        # Demander la proposition de l'utilisateur
        # NOTE : La fonction input() dans les environnements hébergés peut parfois nécessiter un 'Enter' supplémentaire.
        proposition = input(f"Tentative #{tentatives} > Entrez un nombre à 3 chiffres : ")
        
        # Validation de l'entrée
        if len(proposition) != 3 or not proposition.isdigit():
            print("Erreur : Veuillez entrer EXACTEMENT trois chiffres (ex: 519).")
            continue
            
        bulls, cows = calculer_bulls_cows(code, proposition)

        if bulls == 3:
            print("\n====================================")
            print(f"Félicitations ! Vous avez trouvé le code {code} en {tentatives} tentatives !")
            print("====================================")
            break
        else:
            print(f"Résultat : {bulls} Bulls, {cows} Cows.\n")

# --- POINT DE DÉMARRAGE DU PROGRAMME ---
# Cela garantit que le jeu se lance automatiquement à l'exécution du script.
if __name__ == "__main__":
    jeu_code_secret()
