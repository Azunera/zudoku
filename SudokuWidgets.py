from PySide6.QtWidgets import QPushButton


class DifficultyButton(QPushButton):
    def __init__(self, difficulty, color):
        super().__init__(difficulty)
        self.dif = difficulty
        self.setFixedWidth(100)
        if self.dif == 'Hard':
            self.setStyleSheet(f'background-color: {color.rgb_to_hex()}; color: white;')
        else:
            self.setStyleSheet(f'background-color: {color.rgb_to_hex()}; color: black;')
        self.clicked.emit()

