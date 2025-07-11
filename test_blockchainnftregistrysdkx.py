# test_blockchainnftregistrysdkx.py
"""
Tests for BlockchainNFTRegistrySDKX module.
"""

import unittest
from blockchainnftregistrysdkx import BlockchainNFTRegistrySDKX

class TestBlockchainNFTRegistrySDKX(unittest.TestCase):
    """Test cases for BlockchainNFTRegistrySDKX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainNFTRegistrySDKX()
        self.assertIsInstance(instance, BlockchainNFTRegistrySDKX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainNFTRegistrySDKX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
