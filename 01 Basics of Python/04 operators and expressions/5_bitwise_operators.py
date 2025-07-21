# Bit-level operations (rare, but interview-worthy)

a = 5  # 0101
b = 3  # 0011

print("Bitwise AND:", a & b)   # 0001 = 1   Rule: 1 & 1 = 1, everything else = 0
print("Bitwise OR:", a | b)    # 0111 = 7   Rule: 1 | 0 = 1, 0 | 1 = 1, 1 | 1 = 1
print("Bitwise XOR:", a ^ b)   # 0110 = 6   Rule: 1 ^ 0 = 1, 1 ^ 1 = 0, flips only when bits differ
print("Left shift:", a << 1)   # 1010 = 10  Shifting bits left by 1: each bit moves one place left, and a 0 is added at the end:
print("Right shift:", a >> 1)  # 0010 = 2   Shifting bits right by 1: each bit moves one place right, the last bit is dropped:

