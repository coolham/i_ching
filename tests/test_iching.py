import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.iching import IChing
from logic.hexagram import Hexagram

def test_reorder_and_output_hexagrams():
    # 获取原始的HEXAGRAMS
    original_hexagrams = IChing.HEXAGRAMS
    
    # 按照number字段从小到大排序
    sorted_hexagrams = sorted(original_hexagrams, key=lambda x: x.number)
    
    # 创建输出文件
    output_file = 'reordered_hexagrams.py'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("REORDERED_HEXAGRAMS = [\n")
        for hexagram in sorted_hexagrams:
            # 构造Hexagram的字符串表示
            hexagram_str = (
                f"    Hexagram({hexagram.number}, \"{hexagram.binary}\", \"{hexagram.name}\", "
                f"\"{hexagram.symbol}\", \"{hexagram.title}\", \"{hexagram.mnemonic}\", \"{hexagram.palace}\",\n"
                f"             \"{hexagram.judgment}\",\n"
                f"             \"{hexagram.image}\",\n"
                f"             {hexagram.lines}),\n"
            )
            f.write(hexagram_str)
        f.write("]\n")
    
    print(f"重新排序的HEXAGRAMS已输出到 {output_file}")

# 如果直接运行此脚本,则执行测试函数
if __name__ == "__main__":
    test_reorder_and_output_hexagrams()
