from .text import Text

class Prose(Text):
    def __repr__(self):
        length = len(self._value)
        truncated = self._value[:5] + "..." if length > 30 else self._value
        return f'"{truncated}" [{length}]'