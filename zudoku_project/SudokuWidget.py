from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QPainter, QColor

class ColorTableWidgetItem(QTableWidgetItem):
    def __init__(self, text="", color=None):
        super().__init__(text)
        self.color = color if color else QColor(0, 0, 0)

    def paint(self, painter):
        painter.save()
        painter.setPen(self.color)
        painter.drawText(self.rect(), self.text())
        painter.restore()

app = QApplication([])

tableWidget = QTableWidget(2, 2)

# Create a QTableWidgetItem with custom text color
item = ColorTableWidgetItem("Text", QColor(255, 0, 0))

tableWidget.setItem(0, 0, item)

tableWidget.show()
app.exec()
