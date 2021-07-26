class Address(object):
    def __init__(self,addr):
        self.addr=addr

    @classmethod
    def fromhex(cls,addr):
        return cls(bytes.fromhex(addr))

    def equal(self,other):
        if not isinstance(other, Address):
            raise Exception('peer is not an address')
        if not len(self.addr) == len(other.addr):
            raise Exception('address lenght mismatch')
        for i in range(len(self.addr)):
            if not self.addr[i] == other.addr[i]:
                return False
        return True
    def string(self):
        return self.addr.hex()

MaxPO=16
def prox(one,other):
    b = int(MaxPO/8) + 1
    m = 8
    for i in range(b):
        oxo = one[i] ^ other[i]
        for j in range(m):
            if oxo>>(7-j)&0x01 != 0 :
                return i*8 + j
    return MaxPO

