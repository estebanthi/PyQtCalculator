from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QFont
import PyQt5.QtCore as QtCore

from ui.main_window_ui import Ui_PyQtCalculator


class View(QMainWindow, Ui_PyQtCalculator):

        def __init__(self, parent=None):
            super().__init__(parent)
            self.setupUi(self)
            self.configure_font()

        def configure_font(self):
            font = self.display.font()
            font.setLetterSpacing(QFont.PercentageSpacing, 60)
            self.display.setFont(font)

        def display_tokens(self, tokens):
            str_tokens = [str(token) for token in tokens]
            split_each_token = [token for token in str_tokens for token in token]
            self.display.setText(" ".join(split_each_token))

        def event(self, event: QtCore.QEvent) -> bool:
            if event.type() == QtCore.QEvent.KeyPress:
                self.controller.handle_key_press(event)
                return True
            return super().event(event)

        def connect(self, controller):
            self.controller = controller