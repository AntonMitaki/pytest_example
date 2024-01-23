class NotAStringError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "is not a string"

    def __str__(self):
        return f'"{self.value}": {self.message}'

class TooShortError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "is too short to find a middle"

    def __str__(self):
        return f'"{self.value}": {self.message}'

class MiddleChar:
    def get(word: str) -> str:
        if not isinstance(word, str):
            raise NotAStringError(word)

        if len(word) < 3:
            raise TooShortError(word)

        remainder = len(word) % 2

        middle = len(word) // 2

        if remainder == 0:
            return word[middle - 1:middle + 1]
        elif remainder != 0:
            return word[middle]

if __name__ == "__main__":
    middle_char = MiddleChar()
