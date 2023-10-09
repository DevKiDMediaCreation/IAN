class DSNA0_512:
    def __init__(self, h_string: str, salt: int, *, difficulty = 1) -> None:
        self.data = h_string
        self.salt = '0x' + \
            h_string[0:2] + str(salt) + \
            h_string[-2:] if salt != "0" and salt != 0 else "1"
        self.timestamp = '0x' + h_string[-2:]
        self.length = self.data.__len__()
        self.difficulty = 1 if difficulty == 1 or difficulty == 0 else difficult
        self.saltlen = self.salt.__len__()