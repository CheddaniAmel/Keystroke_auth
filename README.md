
# Keystroke Biometrics Backend (FastAPI + HMM)

Ce projet est un backend Python qui permet d'enregistrer et d'authentifier un utilisateur à partir de ses frappes au clavier (`dwell time`, `flight time`) grâce à un modèle HMM (Hidden Markov Model).

---

##  Fonctionnalités

-  Enregistrement des séquences de frappe avec `/register`
-  Authentification avec `/authenticate`
-  Stockage dans `user_data.json`
-  Modélisation comportementale par utilisateur avec `hmmlearn`

---

##  Prérequis

- Python 3.8+
- Pip

---

## 🔧 Structure du projet

```
keystroke-backend/
├── main.py                  # Fichier principal FastAPI
├── models/
│   └── user_models.py       # model pour Entraînement et scoring HMM
├── schemas/
│   └── keystroke_schema.py  # Définition des données reçues
├── database/
│   └── db.py                # Lecture/écriture dans user_data.json
├── user_data.json           # Fichier de stockage utilisateur
└── README.md                # Ce fichier
```

---

##  Endpoints

### 🔹 POST `/register`

> Enregistre les frappes et entraîne un modèle HMM

* **Requête :**

```json
{
  "username": "Anel",
  "sequence": [
    [120, 80],
    [130, 70],
    [110, 90]
  ]
}
```

* **Réponse :**

```json
{
  "message": "Modèle HMM entraîné pour Anel"
}
```

---

### 🔹 POST `/authenticate`

> Calcule un score avec le modèle HMM du user

* **Requête :**

```json
{
  "username": "Amel",
  "sequence": [
    [125, 78],
    [132, 68],
    [113, 88]
  ]
}
```

* **Réponse :**

```json
{
  "authenticated": true,
  "score": -45.2
}
```

---

## 🗃️ Format du fichier `user_data.json`

```json
{
  "Amel": [
    [120, 80],
    [130, 70],
    [110, 90],
    ...
  ],
  "amina": [
    [100, 60],
    [105, 72]
  ]
}
```

Chaque utilisateur a une liste de `[dwell_time, flight_time]` (les frappes).

---

