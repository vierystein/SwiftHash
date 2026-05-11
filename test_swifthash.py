# test_swifthash.py
"""
Tests for SwiftHash module.
"""

import unittest
from swifthash import SwiftHash

class TestSwiftHash(unittest.TestCase):
    """Test cases for SwiftHash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SwiftHash()
        self.assertIsInstance(instance, SwiftHash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SwiftHash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
