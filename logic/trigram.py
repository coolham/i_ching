class Trigram:
    def __init__(self, number, name, nature, binary):
        self.number = number
        self.name = name
        self.nature = nature
        self.binary = binary

    def __str__(self):
        return f"{self.name} ({self.nature}): {self.binary}"

class Trigrams:
    TRIGRAMS = [
        Trigram(0, "坤", "地", "000"),
        Trigram(1, "艮", "山", "001"),
        Trigram(2, "坎", "水", "010"),
        Trigram(3, "巽", "风", "011"),
        Trigram(4, "震", "雷", "100"),
        Trigram(5, "离", "火", "101"),
        Trigram(6, "兑", "泽", "110"),
        Trigram(7, "乾", "天", "111")
    ]

    @staticmethod
    def get_all_trigrams(is_upper=True):
        return Trigrams.TRIGRAMS if is_upper else list(reversed(Trigrams.TRIGRAMS))

    @staticmethod
    def get_trigram_by_binary(binary):
        return next((t for t in Trigrams.TRIGRAMS if t.binary == binary), None)

    @staticmethod
    def get_trigram_by_name(name):
        return next((t for t in Trigrams.TRIGRAMS if t.name == name), None)

    @staticmethod
    def get_trigram_by_number(number):
        return next((t for t in Trigrams.TRIGRAMS if t.number == number), None)