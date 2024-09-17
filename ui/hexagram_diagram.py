from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QSize, QRectF

class HexagramDiagram(QWidget):
    def __init__(self, hexagram=None, parent=None):
        super().__init__(parent)
        self.hexagram = hexagram
        self.setMinimumSize(80, 120)  # 调整最小尺寸，保持2:3的比例

    def update_hexagram(self, hexagram):
        self.hexagram = hexagram
        self.update()

    def paintEvent(self, event):
        if not self.hexagram:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()
        
        # 调整线条宽度和间距的比例
        line_width = width * 0.8  # 增加线条宽度占比
        line_thickness = height * 0.03  # 增加线条粗细
        gap_ratio = 0.15  # 减小阴爻中间的间隙比例
        vertical_gap = height * 0.06  # 增加爻之间的垂直间距

        # 使用更深的颜色
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(30, 30, 30))  # 使用更深的颜色

        for i, line in enumerate(reversed(self.hexagram.binary)):
            y = height - (i + 1) * (line_thickness + vertical_gap) - line_thickness
            if line == '1':  # 阳爻
                rect = QRectF((width - line_width) / 2, y, line_width, line_thickness)
                painter.drawRect(rect)
            else:  # 阴爻
                gap = line_width * gap_ratio
                left_rect = QRectF((width - line_width) / 2, y, (line_width - gap) / 2, line_thickness)
                right_rect = QRectF((width + gap) / 2, y, (line_width - gap) / 2, line_thickness)
                painter.drawRect(left_rect)
                painter.drawRect(right_rect)

    def sizeHint(self):
        return QSize(80, 120)  # 调整建议尺寸，保持2:3的比例