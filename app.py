import sys

from PyQt5.QtWidgets import QApplication

from view import View
from model import Model
from controller import Controller


class App:

    def __init__(self):
        qapp = QApplication(sys.argv)

        view = View()
        model = Model()
        controller = Controller(model, view)

        view.show()
        sys.exit(qapp.exec())


if __name__ == '__main__':
    app = App()
