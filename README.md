# Recherche d'Images Similaires par Descripteurs SIFT

Ce projet est une application de vision par ordinateur en Python permettant de rechercher et d'apparier l'image la plus similaire dans un ensemble de test (`Test`) à partir d'une image de requête choisie dans un ensemble d'entraînement (`Training`). Il utilise l'algorithme **SIFT (Scale-Invariant Feature Transform)** et un algorithme de mise en correspondance **Brute-Force (BFMatcher)** avec le test de ratio de Lowe.

---

## 🛠️ Fonctionnalités

- **Prétraitement & Redimensionnement :** Uniformisation automatique de la taille des images (`480x480`).
- **Extraction de caractéristiques SIFT :** Détection des points clés et calcul des descripteurs invariants aux échelles et rotations.
- **Mise en correspondance KNN (`BFMatcher`) :** Utilisation de l'algorithme des $k$ plus proches voisins avec un test de ratio ($d_1 < 0.75 \times d_2$) pour filtrer les correspondances pertinentes.
- **Visualisation interactive :**
  - Affichage de l'image sélectionnée et de ses points clés.
  - Affichage de la meilleure image correspondante trouvée.
  - Tracé des lignes de correspondance entre l'image requête et la cible.

---

## 📂 Structure du Projet

```text
.
├── Training/       # Dossier contenant les images d'entraînement / requêtes
├── Test/           # Dossier contenant la base d'images de test à comparer
├── temp/           # Dossier pour les fichiers temporaires
├── main.py         # Script Python principal de recherche et d'appariement
└── README.md       # Documentation du projet
```

---

## 📋 Prérequis & Installation

1. **Cloner le dépôt :**
   ```bash
   git clone [https://github.com/votre-nom-d-utilisateur/nom-du-depot.git](https://github.com/votre-nom-d-utilisateur/nom-du-depot.git)
   cd nom-du-depot
   ```

2. **Installer les dépendances :**
   ```bash
   pip install opencv-python numpy
   ```

---

## 🚀 Utilisation

1. Placez vos images de requête dans le dossier `Training/` et les images de comparaison dans le dossier `Test/`.
2. Exécutez le script principal :
   ```bash
   python main.py
   ```
3. Choisissez une image en saisissant l'index affiché dans le terminal.
4. Parcourez les fenêtres OpenCV affichées :
   - L'image sélectionnée.
   - Les points clés SIFT détectés.
   - L'image de la base de test ayant le plus grand nombre de correspondances valides.
   - La visualisation complète des lignes d'appariement entre les deux images.

---

## 📄 Licence

Ce projet est sous licence [MIT](LICENSE) - libre d'utilisation et de modification.
