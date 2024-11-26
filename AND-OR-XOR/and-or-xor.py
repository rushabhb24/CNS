string = "Hello World" 
# Perform AND operation and display the result 
print("Result of AND operation with 127:") 
for char in string: 
    and_result = ord(char) & 127  # AND with 127 
    print(f"{char} -> {and_result}") 
 
# Perform XOR operation and display the result 
print("\nResult of XOR operation with 127:") 
for char in string: 
    xor_result = ord(char) ^ 127  # XOR with 127 
    print(f"{char} -> {xor_result}")
