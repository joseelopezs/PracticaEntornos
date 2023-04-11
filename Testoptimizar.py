import unittest

class TestMedia(unittest.TestCase):
    def test_media_iguales(self):
        self.assertEqual(media([1, 1, 1]), 1)

    def test_media_distintos(self):
        self.assertEqual(media([1, 2, 3]), 2)

    def test_media_decimal(self):
        self.assertEqual(media([1, 2, 4]), 2.3333333333333335)

def media(array):
    return sum(array) / len(array)

if __name__ == "__main__":
    unittest.main()