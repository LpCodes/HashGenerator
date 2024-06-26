
# HashGenerator 🔒

HashGenerator is a simple Python package to calculate the hash of a file using various hashing algorithms.

## Installation ⚙️

To install the package, use pip:

```bash
pip install HashGenerator
```

## Usage 🚀

Here's how you can use the `HashGenerator` package to calculate file hashes:

```python
from HashGenerator import calculate_hash

# Calculate SHA-256 hash
hash_value = calculate_hash('path/to/your/file.txt', 'sha256')
print(f"SHA-256: {hash_value}")

# Calculate MD5 hash
hash_value = calculate_hash('path/to/your/file.txt', 'md5')
print(f"MD5: {hash_value}")

# Calculate SHA-512 hash
hash_value = calculate_hash('path/to/your/file.txt', 'sha512')
print(f"SHA-512: {hash_value}")
```

## Supported Algorithms 🔐

The following hashing algorithms are supported:

- md5
- sha1
- sha224
- sha256
- sha384
- sha512

## Example 💡

Here's an example of how to use the `HashGenerator` package:

```python
from HashGenerator import calculate_hash

file_path = 'example.txt'
algorithm = 'sha256'

hash_value = calculate_hash(file_path, algorithm)
print(f"The {algorithm} hash of the file is: {hash_value}")
```