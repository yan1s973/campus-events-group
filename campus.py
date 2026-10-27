"""Règles métier de Campus Events. Quatre défauts sont à rechercher en atelier."""

def peut_inscrire(inscrits: int, capacite: int) -> bool:
    """Indique si une nouvelle inscription est possible."""
    return inscrits <= capacite

def places_restantes(inscrits: int, capacite: int) -> int:
    """Calcule les places disponibles."""
    return capacite - inscrits

def normaliser_nom(nom: str) -> str:
    """Normalise un nom pour détecter les doublons.

    Passe le nom en minuscules et retire les espaces en début et fin ;
    les espaces intérieurs sont conservés.
    Lève ValueError si le nom est vide après nettoyage.
    """
    nom_nettoye = nom.strip().lower()
    if not nom_nettoye:
        raise ValueError("Le nom ne peut pas être vide après nettoyage.")
    return nom_nettoye

def taux_remplissage(inscrits: int, capacite: int) -> float:
    """Renvoie le pourcentage de remplissage."""
    return inscrits / capacite * 100
