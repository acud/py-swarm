from src.kademlia.pslice import PSlice
from src.address.address import Address
import unittest

base = Address.fromhex("51bbdd")

class TestPSlice(unittest.TestCase):
    def test_exists(self):
        addr = Address.fromhex("00bbcc")
        p_slice=PSlice(4,base)
        p_slice.add(addr)
        self.assertTrue(p_slice.exists(addr))

    def test_remove(self):
        addr = Address.fromhex("00bbcc")
        p_slice1=PSlice(4,base)
        p_slice1.add(addr)
        p_slice1.remove(addr)
        self.assertFalse(p_slice1.exists(addr))

    def test_each_bin(self):
        addr = Address.fromhex("00bbcc")
        p_slice1=PSlice(4,base)
        p_slice1.add(addr)
        addrs = []
        def cb(p1,p2):
            addrs.append(p1)
            return False,True
        # l=lambda addr,po: (addrs.append(addr), return false,true)
        p_slice1.each_bin(cb)
        self.assertTrue(len(addrs) == p_slice1.length())
        self.assertTrue(addrs[0].equal(addr))


if __name__ == '__main__':
    unittest.main()
