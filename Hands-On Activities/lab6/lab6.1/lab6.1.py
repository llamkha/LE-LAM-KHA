import unittest
from encoder import Encoder, Rotor, Reflector  # Giả sử các lớp đã được định nghĩa trong encoder.py
import string

class EncoderTest(unittest.TestCase):
    def setUp(self):
        # Thiết lập bảng chữ cái ASCII in thường
        self.alphabet = string.ascii_lowercase

        # Tạo Encoder instance với các file rotor và reflector
        rotor_files = ["rotor1.txt", "rotor2.txt", "rotor3.txt"]
        reflector_file = "reflector.txt"
        self.encoder = Encoder(rotor_files, reflector_file)

        # Thiết lập bảng chữ cái
        self.encoder.create_alphabet(self.alphabet)

    def test_rotor_bijection(self):
        # Kiểm tra tính song ánh của mỗi rotor
        for rotor_file in ["rotor1.txt", "rotor2.txt", "rotor3.txt"]:
            rotor = Rotor(rotor_file)
            self.assertTrue(check_bijection(rotor), f"Rotor {rotor_file} không song ánh")

    def test_reflector_bijection_and_symmetry(self):
        # Kiểm tra tính song ánh và đối xứng của reflector
        reflector = Reflector("reflector.txt")
        self.assertTrue(check_bijection(reflector), "Reflector không song ánh")
        
        for char in self.alphabet:
            mapped_char = reflector.get(char)
            if mapped_char is not None:
                # Kiểm tra đối xứng f(x) = y thì f(y) = x
                self.assertEqual(reflector.get(mapped_char), char, f"Reflector không đối xứng với ký tự {char}")

    def test_encryption_decryption(self):
        # Kiểm tra mã hóa và giải mã đúng cách
        test_strings = ["thequickbrownfoxjumpsoverthelazydog", "python", "bang", "dragonfly", "csharp"]

        for word in test_strings:
            encrypted_word = self.encoder.encrypt(word)
            decrypted_word = self.encoder.encrypt(encrypted_word)
            self.assertEqual(word, decrypted_word, f"Mã hóa giải mã thất bại với từ {word}")

    def test_invalid_character_exception(self):
        # Kiểm tra ngoại lệ cho ký tự không nằm trong bảng chữ cái
        with self.assertRaises(ValueError):
            self.encoder.encrypt("ñandu")

if __name__ == "__main__":
    unittest.main()
