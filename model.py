class Model:

    def __init__(self, tokens=None):
        self.tokens = tokens or [0]

    def add_token(self, token):
        self.tokens.append(token)

    def clear_tokens(self):
        self.tokens = [0]

    def get_tokens(self):
        if len(self.tokens) > 1:
            if self.tokens[0] == 0 and isinstance(self.tokens[1], int):
                self.tokens.pop(0)
        return self.tokens

    def get_result(self):
        try:
            result = eval("".join([str(token) for token in self.tokens]))
            return [result]
        except Exception as e:
            print(e)
            return [0]