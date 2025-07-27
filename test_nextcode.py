# test_nextcode.py
"""
Tests for NextCode module.
"""

import unittest
from nextcode import NextCode

class TestNextCode(unittest.TestCase):
    """Test cases for NextCode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NextCode()
        self.assertIsInstance(instance, NextCode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NextCode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
