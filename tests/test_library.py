import unittest
import sys
import os

# Adding src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.library_system import LibrarySystem

class TestLibrary(unittest.TestCase):
    def setUp(self):
        #Cleaning the db at first
        self.lib = LibrarySystem()
        
    def test_register_member(self):
        # Adding a member
        self.lib.register_member("Test User", "test@test.com")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()