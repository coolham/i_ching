from .trigram import Trigrams

class Hexagram:
    def __init__(self, number, binary, name, symbol, mnemonic, description, palace, judgment, image, lines):
        self.number = number
        self.binary = binary
        self.name = name
        self.symbol = symbol
        self.mnemonic = mnemonic  # 新增助记词字段
        self.description = description
        self.palace = palace
        self.judgment = judgment
        self.image = image
        self.lines = lines
        self.upper_trigram = Trigrams.get_trigram_by_binary(binary[:3])
        self.lower_trigram = Trigrams.get_trigram_by_binary(binary[3:])

    def __str__(self):
        return f"{self.number}. {self.name} ({self.symbol}) - {self.mnemonic}"

    def __repr__(self):
        return self.__str__()

    def get_full_description(self):
        return f"""
卦序: {self.number}
二进制: {self.binary}
卦名: {self.name}
卦象: {self.symbol}
助记词: {self.mnemonic}
描述: {self.description}
所属宫: {self.palace}
卦辞: {self.judgment}
象辞: {self.image}
爻辞:
{chr(10).join([f'{i+1}. {line}' for i, line in enumerate(self.lines)])}
"""