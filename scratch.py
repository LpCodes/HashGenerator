from HashGenerator import calculate_hash

# Calculate SHA-256 hash
hash_value = calculate_hash(r'tests\test_file.txt', 'sha256')
print(f"SHA-256: {hash_value}")

# Calculate MD5 hash
hash_value = calculate_hash(r'tests\test_file.txt', 'md5')
print(f"MD5: {hash_value}")

# Calculate SHA-512 hash
hash_value = calculate_hash(r'tests\test_file.txt', 'sha512')
print(f"SHA-512: {hash_value}")
