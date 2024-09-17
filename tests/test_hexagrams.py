import unittest
from logic.iching import IChing
from logic.hexagram import Hexagram

class TestHexagrams(unittest.TestCase):

    def test_hexagram_count(self):
        self.assertEqual(len(IChing.HEXAGRAMS), 64, "There should be 64 hexagrams")

    def test_hexagram_attributes(self):
        for hexagram in IChing.HEXAGRAMS:
            self.assertIsInstance(hexagram, Hexagram)
            self.assertIsInstance(hexagram.number, int)
            self.assertIsInstance(hexagram.binary, str)
            self.assertIsInstance(hexagram.name, str)
            self.assertIsInstance(hexagram.symbol, str)
            self.assertIsInstance(hexagram.mnemonic, str)
            self.assertIsInstance(hexagram.description, str)
            self.assertIsInstance(hexagram.palace, str)
            self.assertIsInstance(hexagram.judgment, str)
            self.assertIsInstance(hexagram.image, str)
            self.assertIsInstance(hexagram.lines, list)
            self.assertEqual(len(hexagram.lines), 6)

    def test_hexagram_binary_format(self):
        for hexagram in IChing.HEXAGRAMS:
            self.assertEqual(len(hexagram.binary), 6)
            self.assertTrue(all(bit in '01' for bit in hexagram.binary))

    def test_hexagram_number_range(self):
        numbers = [hexagram.number for hexagram in IChing.HEXAGRAMS]
        self.assertEqual(min(numbers), 0)
        self.assertEqual(max(numbers), 63)
        self.assertEqual(len(set(numbers)), 64)

    def test_specific_hexagram(self):
        qian = IChing.HEXAGRAMS[0]  # 乾卦应该是第一个
        self.assertEqual(qian.number, 63)
        self.assertEqual(qian.binary, "111111")
        self.assertEqual(qian.name, "乾")
        self.assertEqual(qian.symbol, "䷀")
        self.assertEqual(qian.mnemonic, "乾为天")
        self.assertEqual(qian.palace, "乾宫")

    def test_generate_random_hexagram(self):
        hexagram = IChing.generate_random_hexagram()
        self.assertIsInstance(hexagram, Hexagram)
        self.assertIn(hexagram, IChing.HEXAGRAMS)

    def test_get_hexagram_by_name(self):
        hexagram = IChing.get_hexagram_by_name("乾")
        self.assertIsNotNone(hexagram)
        self.assertEqual(hexagram.name, "乾")
        self.assertEqual(hexagram.number, 63)

        non_existent = IChing.get_hexagram_by_name("不存在的卦")
        self.assertIsNone(non_existent)

if __name__ == '__main__':
    unittest.main()