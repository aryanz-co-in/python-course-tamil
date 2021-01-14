# bytes, bytearray, memoryview - Binary Types


x=bytearray(64)

# Convert str into byte
xByte = int.to_bytes(x, 1, byteorder='big')
print(f"Converting x={x} into str value {xByte}")
