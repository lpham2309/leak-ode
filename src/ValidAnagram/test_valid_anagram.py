import unittest
from src.ValidAnagram.valid_anagram import isAnagram
class TestValidAnagram(unittest.TestCase):

    def test_with_two_empty_string(self):
        self.assertIsNotNone(isAnagram("", ""), True)

    def test_with_mismatch_anagram(self):
        self.assertIsNotNone(isAnagram("sas", "asa"), False)

    def test_inputs_with_case_sensitive(self):
        self.assertIsNotNone(isAnagram("Racecar", "carRace"), True)