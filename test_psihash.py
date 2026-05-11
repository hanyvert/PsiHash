# test_psihash.py
"""
Tests for PsiHash module.
"""

import unittest
from psihash import PsiHash

class TestPsiHash(unittest.TestCase):
    """Test cases for PsiHash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PsiHash()
        self.assertIsInstance(instance, PsiHash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PsiHash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
