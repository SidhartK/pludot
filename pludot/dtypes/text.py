class Text:
    def __init__(self, value: str):
        self._value = value

    def __repr__(self):
        return self._value