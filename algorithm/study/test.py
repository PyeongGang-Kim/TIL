import hashlib
class block():
    def __init__(self, a, b):
        self.prev = a
        self.data = str(b)

        temp = self.prev + self.data
        nonce = 0
        while 1:
            sha.update((temp + str(nonce)).encode('utf-8'))
            temp2 = sha.hexdigest()
            if temp2[:5] == '00000':
                break
            nonce += 1
        self.nonce = nonce
        self.hash = temp2


chain = []
initial = 'initial'
sha = hashlib.new('sha256')
chain.append(block(initial, initial))
blockdata = 0
while 1:
    blockdata += 1
    chain.append(block(chain[-1].hash, blockdata))
    if blockdata == 3:
        break

for block in chain:
    print()
    print('nonce:', block.nonce)
    print('data:', block.data)
    print('prevhash:', block.prev)
    print('hash:', block.hash)
