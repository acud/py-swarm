from ..address.address import Address
from .pslice import PSlice

MAX_BUCKETS=16

class Kademlia:
    baseAddr = bytearray()

    def __init__(self,base):
        self.baseAddr=base
        self.known=PSlice(MAX_BUCKETS)
        self.connected=PSlice(MAX_BUCKETS)

    def connect(self,peer):
        self.connected.add(peer)
    def addpeer(self,peer):
        self.known.add(peer)

def distancecmp(a,x,y):
    for i in range(len(a)):
        dx = x[i] ^ a[i]
        dy = y[i] ^ a[i]
        if dx == dy:
            continue
        elif dx < dy:
            return 1
        return -1
    return 0

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

