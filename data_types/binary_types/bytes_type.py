# bytes, bytearray, memoryview - Binary Types

bin_value = bytes(4)
print(bin_value)
print(type(bin_value))

value = b"Hello"
print(value)
print(type(value))

# Get Byte value of 'A'
a = b'A'
x = int.from_bytes(a, byteorder='big')
print(f"Byte value of \'A\' {x}")

# Convert str into byte
xByte = int.to_bytes(x, 1, byteorder='big')
print(f"Converting x={x} into str value {xByte}")
