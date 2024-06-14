from PySide6.QtWidgets import QPushButton

class DifficultyButton(QPushButton):
    def __init__(self, difficulty, color):
        super().__init__(difficulty)
        self.dif=difficulty
        self.setFixedWidth(100)
        self.setStyleSheet(f'background-color: {color}')
        self.clicked.emit()

if __name__ == "__main__":
    pass