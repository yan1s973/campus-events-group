"""Tests de l'incident C : normalisation des noms (Yanis, C)."""
import unittest
from campus import normaliser_nom


class TestNormaliserNom(unittest.TestCase):

    def test_nominal(self):
        # Cas normal : passage en minuscules
        self.assertEqual(normaliser_nom("Alice Martin"), "alice martin")

    def test_espaces_debut_et_fin(self):
        # Cas limite : contre-exemple de l'incident (copier-coller)
        self.assertEqual(normaliser_nom("  Alice Martin  "), "alice martin")

    def test_espaces_interieurs_conserves(self):
        # Cas limite : les espaces intérieurs ne doivent pas disparaître
        self.assertEqual(normaliser_nom("Alice  Martin"), "alice  martin")

    def test_nom_seulement_espaces(self):
        # Cas invalide : un nom fait d'espaces doit être refusé
        with self.assertRaises(ValueError):
            normaliser_nom("   ")

    def test_nom_vide(self):
        # Cas invalide : un nom vide doit être refusé
        with self.assertRaises(ValueError):
            normaliser_nom("")

    def test_copie_formulaire_tabulation_retour_ligne(self):
        # Cas original : un formulaire peut ajouter une tabulation ou un retour à la ligne
        self.assertEqual(normaliser_nom("\tAlice Martin\n"), "alice martin")


if __name__ == "__main__":
    unittest.main()