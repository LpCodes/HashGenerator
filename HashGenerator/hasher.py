import hashlib

SUPPORTED_ALGORITHMS = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']


def calculate_hash(file_path, algorithm='sha256'):
    """
    Calculate the hash of a file.

    Parameters:
    file_path (str): The path to the file.
    algorithm (str): The hashing algorithm to use (default is 'sha256').

    Choose from : 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'

    Returns:
    str: The calculated hash in hexadecimal format.

    Raises:
    ValueError: If the specified algorithm is not supported.
    """
    if algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError(
            f"Unsupported algorithm '{algorithm}'. Supported algorithms are: {', '.join(SUPPORTED_ALGORITHMS)}")

    hash_func = getattr(hashlib, algorithm)()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()
