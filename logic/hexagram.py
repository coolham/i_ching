from .trigram import Trigrams

class Hexagram:
    def __init__(self, number, binary, name, symbol, description, mnemonic, palace, judgment, image, lines):
        self.number = number  # 卦序
        self.binary = binary  # 二进制
        self.name = name  # 卦名
        self.symbol = symbol  # 卦象
        self.description = description  # 卦辞
        self.mnemonic = mnemonic  # 助记词
        self.palace = palace  # 所属宫
        self.judgment = judgment  # 卦辞
        self.image = image  # 象辞
        self.lines = lines  # 爻辞
        self.upper_trigram = Trigrams.get_trigram_by_binary(binary[:3])  # 上卦
        self.lower_trigram = Trigrams.get_trigram_by_binary(binary[3:])  # 下卦

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