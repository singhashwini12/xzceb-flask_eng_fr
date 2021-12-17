"""
Module for unit tests for translations
"""

import unittest

from translator import french_to_english, english_to_french

class TranslationTest(unittest.TestCase):
    """This Class contains the unit tests for translations"""

    def test_french_to_english(self):
        """This method tests the French to English Translations"""

        self.assertEqual(french_to_english(""),None)
        self.assertEqual(french_to_english("Bonjour"),[{'translation': 'Hello'}])

    def test_english_to_french(self):
        """This method tests the English to French Translations"""

        self.assertEqual(english_to_french(""),None)
        self.assertEqual(english_to_french("Hello"),[{'translation': 'Bonjour'}])

if __name__=='__main__':
    unittest.main()
