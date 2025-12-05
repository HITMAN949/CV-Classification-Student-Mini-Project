# Application Streamlit pour la classification de CV
# Responsable : Houssam
# Ce fichier contient l'interface web principale du projet

# On importe Streamlit pour créer notre interface web
import streamlit as st
# Pickle nous permet de charger notre modèle sauvegardé
import pickle
# OS pour gérer les chemins de fichiers
import os
# Sys pour modifier le chemin Python
import sys

# On ajoute le dossier parent au chemin Python
# Ceci permet d'importer les modules des autres dossiers du projet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# On importe notre fonction d'extraction de texte depuis le module de prétraitement
from preprocessing_Oumaima.text_extraction import extract_text_general
# On importe la fonction de nettoyage de texte
from preprocessing_Oumaima.text_cleaning import clean_text


def search_keywords(text, keywords):
    """
    Cette fonction cherche des mots-clés dans le texte du CV
    Elle retourne les mots trouvés et ceux non trouvés
    """
    # On convertit le texte en minuscules pour une recherche insensible à la casse
    text_lower = text.lower()
    # Liste pour stocker les mots-clés trouvés
    found = []
    # Liste pour stocker les mots-clés non trouvés
    not_found = []
    
    # On parcourt chaque mot-clé fourni par l'utilisateur
    for keyword in keywords:
        # On vérifie si le mot-clé existe dans le texte
        if keyword.lower().strip() in text_lower:
            # Si oui, on l'ajoute à la liste des trouvés
            found.append(keyword.strip())
        else:
            # Sinon, on l'ajoute à la liste des non trouvés
            not_found.append(keyword.strip())
    
    # On retourne les deux listes
    return found, not_found


def main():
    """
    Fonction principale de l'application
    C'est ici que tout se passe !
    """
    # Configuration de la page Streamlit avec un titre et une icône
    st.set_page_config(page_title="CV Classification", page_icon="📄", layout="wide")
    
    # Affichage du titre principal de l'application
    st.title("📄 CV Classification System")
    # Une ligne horizontale pour séparer visuellement
    st.markdown("---")
    
    # On récupère le chemin du dossier actuel
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # On remonte d'un niveau pour accéder à la racine du projet
    project_root = os.path.join(base_dir, '..')
    
    # Chemin vers le fichier du modèle entraîné
    model_path = os.path.join(project_root, 'modeling_MoadChafir', 'MoadChafir_model.pkl')
    # Chemin vers le fichier du vectoriseur TF-IDF
    vectorizer_path = os.path.join(project_root, 'modeling_MoadChafir', 'MoadChafir_vectorizer.pkl')
    
    # Variable pour savoir si le modèle est chargé correctement
    model_loaded = False
    
    # On essaie de charger le modèle et le vectoriseur
    try:
        # Chargement du modèle de classification
        model = pickle.load(open(model_path, 'rb'))
        # Chargement du vectoriseur pour transformer le texte
        vectorizer = pickle.load(open(vectorizer_path, 'rb'))
        # Si tout va bien, on marque le modèle comme chargé
        model_loaded = True
    except Exception as e:
        # En cas d'erreur, on affiche un message mais l'app continue de fonctionner
        st.warning(f"Modèle non chargé : {e}. La classification est désactivée, mais la recherche par mots-clés fonctionne.")
    
    # On crée deux colonnes pour organiser l'interface
    # La première colonne est plus large (ratio 2:1)
    col1, col2 = st.columns([2, 1])
    
    # Dans la première colonne : zone d'upload
    with col1:
        # Sous-titre pour la section upload
        st.subheader("📤 Télécharger un CV")
        # Widget de téléchargement de fichier
        # Accepte les formats PDF, TXT et DOCX
        uploaded_file = st.file_uploader("Télécharger votre CV", type=['pdf', 'txt', 'docx'])
    
    # Dans la deuxième colonne : recherche par mots-clés
    with col2:
        # Sous-titre pour la section recherche
        st.subheader("🔍 Recherche par mots-clés")
        # Zone de texte pour entrer les mots-clés
        keywords_input = st.text_area(
            "Entrez les mots-clés (séparés par des virgules)",
            placeholder="Python, Java, Machine Learning, SQL...",
            height=100
        )
    
    # Ligne de séparation
    st.markdown("---")
    
    # Si un fichier a été téléchargé
    if uploaded_file is not None:
        # On crée un nom de fichier temporaire avec la bonne extension
        temp_filename = "temp_cv" + os.path.splitext(uploaded_file.name)[1]
        
        # On sauvegarde le fichier téléchargé temporairement
        with open(temp_filename, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # On essaie de traiter le fichier
        try:
            # Extraction du texte depuis le fichier (PDF, TXT ou DOCX)
            text = extract_text_general(temp_filename)
            
            # Si on a réussi à extraire du texte
            if text:
                # On nettoie le texte (suppression des caractères spéciaux, etc.)
                cleaned_text = clean_text(text)
                
                # On crée deux colonnes pour afficher les résultats
                result_col1, result_col2 = st.columns(2)
                
                # Première colonne : résultat de la classification
                with result_col1:
                    st.subheader("🎯 Résultat de Classification")
                    # Si le modèle est disponible
                    if model_loaded:
                        # Bouton pour lancer la classification
                        if st.button("Classifier le CV", type="primary"):
                            # On transforme le texte en vecteur numérique
                            features = vectorizer.transform([cleaned_text])
                            # On prédit la catégorie
                            prediction = model.predict(features)[0]
                            # On affiche le résultat
                            st.success(f"**Catégorie prédite :** {prediction}")
                    else:
                        # Message si le modèle n'est pas disponible
                        st.info("Le modèle n'est pas disponible pour la classification")
                
                # Deuxième colonne : résultats de la recherche par mots-clés
                with result_col2:
                    st.subheader("🔎 Résultats de la recherche")
                    # Si l'utilisateur a entré des mots-clés
                    if keywords_input:
                        # On sépare les mots-clés par les virgules
                        keywords = [k.strip() for k in keywords_input.split(',') if k.strip()]
                        # Si on a des mots-clés valides
                        if keywords:
                            # On cherche les mots-clés dans le texte
                            found, not_found = search_keywords(text, keywords)
                            
                            # Affichage des mots-clés trouvés en vert
                            if found:
                                st.success(f"**Trouvés ({len(found)}) :** {', '.join(found)}")
                            # Affichage des mots-clés non trouvés en rouge
                            if not_found:
                                st.error(f"**Non trouvés ({len(not_found)}) :** {', '.join(not_found)}")
                            
                            # Calcul et affichage du pourcentage de correspondance
                            match_pct = len(found) / len(keywords) * 100
                            st.metric("Taux de correspondance", f"{match_pct:.0f}%")
                    else:
                        # Message si aucun mot-clé n'a été entré
                        st.info("Entrez des mots-clés ci-dessus pour rechercher")
                
                # Section dépliable pour voir le texte brut extrait
                with st.expander("📝 Voir le texte extrait"):
                    st.text_area("Texte brut", text, height=300, disabled=True)
                
                # Section dépliable pour voir le texte nettoyé
                with st.expander("🧹 Voir le texte nettoyé"):
                    st.text_area("Texte nettoyé", cleaned_text, height=200, disabled=True)
                    
            else:
                # Message d'avertissement si l'extraction a échoué
                st.warning("Impossible d'extraire le texte du fichier")
            
        except Exception as e:
            # Affichage de l'erreur si quelque chose s'est mal passé
            st.error(f"Erreur lors du traitement du fichier : {e}")
        
        finally:
            # Nettoyage : on supprime le fichier temporaire
            if os.path.exists(temp_filename):
                os.remove(temp_filename)


# Point d'entrée de l'application
# Cette condition vérifie si le script est exécuté directement
if __name__ == "__main__":
    # On lance la fonction principale
    main()
