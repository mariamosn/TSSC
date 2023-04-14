import base64
from Crypto.Cipher import AES

BLOCK_SIZE = 32

my_priv = 11770246699657521249810253430779065705211875384103497164136403622683842607469702197253391392586542798366525960175932842159603277607056418879071902525451537

g = int(input("g = "))
p = int(input("p = "))

# my_pub = g ^ my_priv (mod p)
my_pub = int(pow(g, my_priv, p))
print("My public key: ", my_pub)

your_pub = int(input("Your public key: "))

# shared = your_pub ^ my_priv mod p
shared = int(pow(your_pub, my_priv, p))
key = shared.to_bytes((shared.bit_length() + 7) // 8, byteorder='big')[0:BLOCK_SIZE]
# print("Key: ", key)

b64_code = input("Encoded flag: ")
aes_code = base64.b64decode(b64_code)

cipher = AES.new(key, AES.MODE_ECB)
msg = cipher.decrypt(aes_code)

print(msg)
