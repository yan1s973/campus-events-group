import unittest
from campus import places_restantes


class TestIncidentB(unittest.TestCase):
    # Cas normal et frontieres valides
    def test_nominal(self):
        self.assertEqual(places_restantes(1, 3), 2)

    def test_evenement_plein(self):
        self.assertEqual(places_restantes(4, 4), 0)

    def test_capacite_nulle_valide(self):
        self.assertEqual(places_restantes(0, 0), 0)

    # Cas invalides : doivent lever ValueError
    def test_inscrits_superieurs_capacite(self):
        with self.assertRaises(ValueError):
            places_restantes(5, 4)

    def test_inscrits_negatifs(self):
        with self.assertRaises(ValueError):
            places_restantes(-1, 4)

    def test_capacite_negative(self):
        with self.assertRaises(ValueError):
            places_restantes(0, -1)

    # Cas original (absent du jeu fourni)
    def test_inscrit_sur_capacite_nulle(self):
        with self.assertRaises(ValueError):
            places_restantes(1, 0)


if __name__ == "__main__":
    unittest.main()
