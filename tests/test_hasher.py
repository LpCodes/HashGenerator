import unittest
from HashGenerator import calculate_hash, SUPPORTED_ALGORITHMS
import os


class TestHasher(unittest.TestCase):

    def setUp(self):
        self.test_file = 'tests/test_file.txt'
        os.makedirs(os.path.dirname(self.test_file), exist_ok=True)
        with open(self.test_file, 'w') as f:
            f.write('Hello, World!')

    def test_calculate_hash(self):
        expected_hashes = {
            'md5': '65a8e27d8879283831b664bd8b7f0ad4',
            'sha1': '2ef7bde608ce5404e97d5f042f95f89f1c232871',
            'sha224': 'c4890faffdb0105d991a461e668e276685401b02eab1ef4372795047',
            'sha256': 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b53e3c5c54ef5f7f7',
            'sha384': '5485cc9b20ecb6fd4c3af7a1b0dfb4fba9eb1ea08bfa7aabefcf65bdc39a6cfebd0d5fb4d7c4713ad72074f206d1a3c7',
            'sha512': '861844d6704e8573fec34d967e20bcfe6f8c8a78d0c5e911d6dcb01dccc21d81e676f5a6d4ac4e1dbf9a64b3a5b3e3f1d7a6d0a6f0641b2064ec62b098e5a612',
        }

        for algorithm, expected_hash in expected_hashes.items():
            with self.subTest(algorithm=algorithm):
                self.assertEqual(calculate_hash(self.test_file, algorithm), expected_hash)

    def test_unsupported_algorithm(self):
        with self.assertRaises(ValueError):
            calculate_hash(self.test_file, 'unsupported_algo')


if __name__ == '__main__':
    unittest.main()
