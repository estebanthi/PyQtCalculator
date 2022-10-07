import PyQt5.QtCore as QtCore


class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect()

    def connect(self):
        self.view.connect(self)
        self.view.button_0.clicked.connect(lambda: self.add_token(0))
        self.view.button_1.clicked.connect(lambda: self.add_token(1))
        self.view.button_2.clicked.connect(lambda: self.add_token(2))
        self.view.button_3.clicked.connect(lambda: self.add_token(3))
        self.view.button_4.clicked.connect(lambda: self.add_token(4))
        self.view.button_5.clicked.connect(lambda: self.add_token(5))
        self.view.button_6.clicked.connect(lambda: self.add_token(6))
        self.view.button_7.clicked.connect(lambda: self.add_token(7))
        self.view.button_8.clicked.connect(lambda: self.add_token(8))
        self.view.button_9.clicked.connect(lambda: self.add_token(9))
        self.view.button_plus.clicked.connect(lambda: self.add_token('+'))
        self.view.button_minus.clicked.connect(lambda: self.add_token('-'))
        self.view.button_multiply.clicked.connect(lambda: self.add_token('*'))
        self.view.button_divide.clicked.connect(lambda: self.add_token('/'))
        self.view.button_equal.clicked.connect(lambda: self.equal())
        self.view.button_C.clicked.connect(self.clear_tokens)
        self.view.button_dot.clicked.connect(lambda: self.add_token('.'))

    def add_token(self, token):
        self.model.add_token(token)
        tokens = self.get_tokens()
        self.view.display_tokens(tokens)

    def get_tokens(self):
        return self.model.get_tokens()

    def clear_tokens(self):
        self.model.clear_tokens()
        tokens = self.get_tokens()
        self.view.display_tokens(tokens)

    def equal(self):
        result = self.model.get_result()
        self.view.display_tokens(result)
        self.model.tokens = result

    def handle_key_press(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_0:
            self.add_token(0)
        elif key == QtCore.Qt.Key_1:
            self.add_token(1)
        elif key == QtCore.Qt.Key_2:
            self.add_token(2)
        elif key == QtCore.Qt.Key_3:
            self.add_token(3)
        elif key == QtCore.Qt.Key_4:
            self.add_token(4)
        elif key == QtCore.Qt.Key_5:
            self.add_token(5)
        elif key == QtCore.Qt.Key_6:
            self.add_token(6)
        elif key == QtCore.Qt.Key_7:
            self.add_token(7)
        elif key == QtCore.Qt.Key_8:
            self.add_token(8)
        elif key == QtCore.Qt.Key_9:
            self.add_token(9)
        elif key == QtCore.Qt.Key_Plus:
            self.add_token('+')
        elif key == QtCore.Qt.Key_Minus:
            self.add_token('-')
        elif key == QtCore.Qt.Key_Asterisk:
            self.add_token('*')
        elif key == QtCore.Qt.Key_Slash:
            self.add_token('/')
        elif key == QtCore.Qt.Key_Period:
            self.add_token('.')
        elif key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter:
            self.equal()
        elif key == QtCore.Qt.Key_Backspace:
            self.clear_tokens()