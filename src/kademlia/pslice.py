from ..address.address import Address,prox
from collections.abc import Callable

class PSlice:
    def __init__(self,buckets,base: Address):
        self.bins=[0] * buckets
        self.base = base
        self.peers: list[Address] = []

    def po(self,addr: Address):
        return prox(self.base.addr,addr.addr)

    def add(self,peer):
        print(len(self.peers))
        if not isinstance(peer, Address):
            raise Exception('peer is not an address')
        for addr in self.peers:
            if addr.equal(peer):
                return

        self.peers.append(peer)
        proximity = self.po(peer)
        self.inc_deeper(proximity)

    def length(self):
        return len(self.peers)

    def exists(self,peer) -> bool:
        for addr in self.peers:
            if addr.equal(peer):
                return True
        return False

    def remove(self,addr):
        i= [x for x in range(len(self.peers)) if self.peers[x].equal(addr)]
        if len(i) == 1:
            del self.peers[i[0]]
            self.dec_deeper(self.po(addr))

    def inc_deeper(self,po):
        for i in range(po+1,len(self.bins)):
            self.bins[i]+=1

    def dec_deeper(self,po):
        for i in range(po+1,len(self.bins)):
            self.bins[i]-=1

    def each_bin(self,fn: Callable[[Address,int],bool,bool]):
        bin_end=self.length()
        for i in range(len(self.bins)-1,0,-1):
            for peer in self.peers[self.bins[i]:bin_end]:
                stop, next_bin = fn(peer,i)
                if stop == True:
                    return
                if next_bin == True:
                    break
            bin_end=self.bins[i]

# // EachBinRev iterates over all peers from shallowest bin to deepest.
# func (s *PSlice) EachBinRev(pf topology.EachPeerFunc) error {
	# s.RLock()
	# peers, bins := s.peers, s.bins
	# s.RUnlock()

	# if len(peers) == 0 {
		# return nil
	# }

	# var binEnd int
	# for i := 0; i <= len(bins)-1; i++ {
		# if i == len(bins)-1 {
			# binEnd = len(peers)
		# } else {
			# binEnd = int(bins[i+1])
		# }

		# for _, v := range peers[bins[i]:binEnd] {
			# stop, next, err := pf(v, uint8(i))
			# if err != nil {
				# return err
			# }
			# if stop {
				# return nil
			# }
			# if next {
				# break
			# }
		# }
	# }
	# return nil
# }

# func (s *PSlice) BinPeers(bin uint8) []swarm.Address {
	# s.RLock()
	# defer s.RUnlock()

	# b := int(bin)
	# if b >= len(s.bins) {
		# return nil
	# }

	# var bEnd int
	# if b == len(s.bins)-1 {
		# bEnd = len(s.peers)
	# } else {
		# bEnd = int(s.bins[b+1])
	# }

	# ret := make([]swarm.Address, bEnd-int(s.bins[b]))
	# copy(ret, s.peers[s.bins[b]:bEnd])

	# return ret
# }

# // ShallowestEmpty returns the shallowest empty bin if one exists.
# // If such bin does not exists, returns true as bool value.
# func (s *PSlice) ShallowestEmpty() (bin uint8, none bool) {
	# s.RLock()
	# defer s.RUnlock()

	# binCp := make([]uint, len(s.bins)+1)
	# copy(binCp, s.bins)
	# binCp[len(binCp)-1] = uint(len(s.peers))

	# for i := uint8(0); i < uint8(len(binCp)-1); i++ {
		# if binCp[i+1] == binCp[i] {
			# return i, false
		# }
	# }
	# return 0, true
# }


