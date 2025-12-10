import streamlit as st

# --- Configuration du Jeu ---
CODE_SECRET = "218"

def calculer_bulls_cows(code_secret, proposition):
    """
    Calcule le nombre de Bulls (chiffre et position corrects) 
    et de Cows (chiffre correct, mauvaise position).
    """
    bulls = 0
    cows = 0
    
    # Étape 1: Calcul des Bulls
    for i in range(len(code_secret)):
        if proposition[i] == code_secret[i]:
            bulls += 1
            
    # Étape 2: Calcul des Cows
    total_chiffres_communs = 0
    for chiffre_prop in proposition:
        if chiffre_prop in code_secret:
            total_chiffres_communs += 1
            
    # Les 'vraies' Cows sont les chiffres corrects moins les Bulls (déjà bien placés).
    cows = total_chiffres_communs - bulls
            
    return bulls, cows

def initialiser_etat_jeu():
    """Initialise l'état du jeu si ce n'est pas déjà fait."""
    if 'historique' not in st.session_state:
        st.session_state.historique = []
        st.session_state.tentatives = 0
        st.session_state.jeu_fini = False

def verifier_proposition():
    """Logiciel de vérification de la proposition du joueur."""
    
    # 1. Récupérer la proposition
    proposition = st.session_state.saisie_joueur
    
    # 2. Validation
    if len(proposition) != 3 or not proposition.isdigit():
        st.error("Veuillez entrer EXACTEMENT trois chiffres (ex: 519).")
        return
    
    # 3. Calcul
    bulls, cows = calculer_bulls_cows(CODE_SECRET, proposition)
    st.session_state.tentatives += 1
    
    # 4. Enregistrement de l'historique
    st.session_state.historique.append({
        "proposition": proposition,
        "resultat": f"{bulls} Bulls, {cows} Cows"
    })
    
    # 5. Vérification de victoire
    if bulls == 3:
        st.session_state.jeu_fini = True
        
    # 6. Vider la zone de saisie
    st.session_state.saisie_joueur = ""


# --- DÉMARRAGE DE L'APPLICATION STREAMLIT ---

# 0. Initialisation
initialiser_etat_jeu()

# 1. Interface Utilisateur
st.title("Code Secret *** 🕵️‍♀️")
st.markdown("Bienvenue ! L'objectif est de déduire le code secret à **trois chiffres** en utilisant les indices *Bulls* et *Cows*.")

st.header("Règles et Indice")
st.markdown("""
* **Bulls (Bien placé)** : Chiffre correct **ET** à la bonne position.
* **Cows (Mal placé)** : Chiffre correct **MAIS** à la mauvaise position.
* ---
* **Indice pour joueurs avancés :** Le chiffre des dizaines (la position du '1') est un chiffre impair.
""")

st.divider()

# 2. Zone de Jeu
if st.session_state.jeu_fini:
    st.balloons()
    st.success(f"🥳 FÉLICITATIONS ! Vous avez trouvé le code {CODE_SECRET} en {st.session_state.tentatives} tentatives.")
    st.button("Recommencer le jeu", on_click=lambda: st.session_state.clear())
else:
    st.subheader(f"Tentative #{st.session_state.tentatives + 1}")
    
    # Widget de saisie
    st.text_input(
        "Votre proposition (3 chiffres)", 
        max_chars=3, 
        key="saisie_joueur", 
        on_change=verifier_proposition, 
        placeholder="Ex: 123"
    )
    
    # Bouton de soumission (au cas où l'utilisateur n'utilise pas 'Enter')
    st.button("Vérifier", on_click=verifier_proposition)

# 3. Affichage de l'Historique
if st.session_state.historique:
    st.header("Historique")
    
    # Affichage inversé pour voir les dernières tentatives en premier
    for item in st.session_state.historique[::-1]:
        st.code(f"Proposition : {item['proposition']} -> Résultat : {item['resultat']}")
