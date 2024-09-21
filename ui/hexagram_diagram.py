from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen, QColor, QBrush, QImage
from PyQt6.QtCore import Qt, QSize, QRectF

class HexagramDiagram(QWidget):
    def __init__(self, hexagram=None, yang_color=QColor(255, 0, 0), parent=None):  # 使用 QColor 来定义红色
        super().__init__(parent)
        self.hexagram = hexagram
        self.yang_color = yang_color
        self.yin_color = QColor(0, 0, 0)  # 使用 QColor 来定义黑色
        self.setMinimumSize(30, 60)  # 设置最小尺寸

    def paintEvent(self, event):
        if not self.hexagram:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()
        
        # 计算爻的高度和间隔
        total_height = height * 0.9  # 留出10%的边距
        line_height = total_height / 13  # 6个爻 + 5个间隔 = 11份，再留出2份作为顶部和底部的间隔
        gap = line_height / 2
        
        line_width = width * 0.8
        x_start = width * 0.1

        binary = self.hexagram.binary
        for i, bit in enumerate(binary):  # 移除 reversed
            y = height - (i + 1) * (line_height + gap) - line_height
            if bit == '1':  # 阳爻
                painter.setBrush(QBrush(self.yang_color))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawRect(int(x_start), int(y), int(line_width), int(line_height))
            else:  # 阴爻
                painter.setBrush(QBrush(self.yin_color))
                painter.setPen(Qt.PenStyle.NoPen)
                half_width = line_width / 2 - width * 0.02  # 2% of width as gap
                painter.drawRect(int(x_start), int(y), int(half_width), int(line_height))
                painter.drawRect(int(x_start + line_width - half_width), int(y), int(half_width), int(line_height))

    def update_hexagram(self, hexagram):
        self.hexagram = hexagram
        self.update()

    def sizeHint(self):
        return QSize(60, 120)  # 建议的默认大小

    def minimumSizeHint(self):
        return QSize(30, 60)  # 最小可接受的大小

    def get_printable_image(self, size=QSize(60, 120)):
        if not self.hexagram:
            return None

        image = QImage(size, QImage.Format.Format_RGB32)
        image.fill(Qt.GlobalColor.white)

        painter = QPainter(image)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = size.width()
        height = size.height()
        
        total_height = height * 0.9
        line_height = total_height / 13
        gap = line_height / 2
        
        line_width = width * 0.8
        x_start = width * 0.1

        binary = self.hexagram.binary
        for i, bit in enumerate(binary):  # 移除 reversed
            y = height - (i + 1) * (line_height + gap) - line_height
            if bit == '1':  # 阳爻
                painter.setBrush(QBrush(self.yang_color))
                painter.setPen(Qt.PenStyle.NoPen)
                painter.drawRect(int(x_start), int(y), int(line_width), int(line_height))
            else:  # 阴爻
                painter.setBrush(QBrush(self.yin_color))
                painter.setPen(Qt.PenStyle.NoPen)
                half_width = line_width / 2 - width * 0.02
                painter.drawRect(int(x_start), int(y), int(half_width), int(line_height))
                painter.drawRect(int(x_start + line_width - half_width), int(y), int(half_width), int(line_height))

        painter.end()
        return image