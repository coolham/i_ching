from PyQt6.QtCore import Qt, QObject, QSize, QRectF
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from ui.hexagram_diagram import HexagramDiagram

class HexagramPrintService(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    def print_hexagram(self, hexagram, parent_widget):
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer, parent_widget)
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self._do_print(printer, hexagram)

    def _do_print(self, printer, hexagram):
        painter = QPainter(printer)
        
        # 获取打印区域的尺寸
        rect = printer.pageRect(QPrinter.Unit.DevicePixel)
        page_width = rect.width()
        page_height = rect.height()
        
        # 设置卦象尺寸
        image_size = QSize(400, 600)  # 保持卦象尺寸不变
        diagram = HexagramDiagram(hexagram)
        image = diagram.get_printable_image(image_size)
        
        # 计算居中位置
        image_x = (page_width - image_size.width()) / 2
        image_y = 50  # 距离顶部的距离
        
        painter.drawImage(int(image_x), int(image_y), image)
        
        # 设置文字字体和颜色
        font = QFont("Arial", 12)  # 稍微增大字体
        painter.setFont(font)
        painter.setPen(QColor(0, 0, 0))
        
        # 在卦象下方绘制文字信息
        text_x = 50  # 左边距
        text_y = image_y + image_size.height() + 50  # 保持卦象和文字之间的距离
        line_height = 40  # 增加行高
        
        text_items = [
            f"卦名: {hexagram.name}",
            f"序号: {hexagram.number}",
            f"二进制: {hexagram.binary}",
            f"符号: {hexagram.symbol}",
            f"助记词: {hexagram.mnemonic}",
            f"宫位: {hexagram.palace}",
            f"描述: {hexagram.description}"
        ]
        
        for item in text_items:
            rect = QRectF(text_x, text_y, page_width - 100, line_height * 3)  # 增加矩形高度，确保足够空间
            painter.drawText(rect, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop | Qt.TextFlag.TextWordWrap, item)
            
            # 计算实际绘制的文本高度
            br = painter.boundingRect(rect, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop | Qt.TextFlag.TextWordWrap, item)
            actual_height = br.height()
            
            text_y += max(actual_height, line_height) + 10  # 使用实际高度或最小行高，并添加额外间距
        
        painter.end()