#
# Hashing algorithm by SAHF, KENECTICS and DevKiD 10/08/2023 (c)
# Version: 1.0.0
#

import json


class SAHF_512:
    # Init the class and runtime variables
    def __init__(self, h_string: str, salt: str = "1", *, difficulty: int = 1) -> None:
        self.data = h_string
        self.salt = (
            "0x" + h_string[0:2] + str(salt) + h_string[-2:]
            if salt != "0" and salt != 0
            else "1"
        )
        self.timestamp = "0x" + h_string[-2:]
        self.length = h_string.__len__()
        self.difficulty = 1 if difficulty not in {0, 1} else difficulty
        self.saltlen = self.salt.__len__()

    # Hash
    def hash(self) -> str:
        # Check the length of the string to avoid errors like IndexError
        if self.saltlen < 8:
            self.data = (
                self.data * 6 + str(self.difficulty) * self.saltlen + self.salt * 3
            )
        i = 0
        # Shift the string of lenght of salt + timestamp
        while i <= self.saltlen + self.timestamp.__len__():
            # Shift the string
            self.data = self.data[1:] + self.data[0]
            i += 1

        # split the string into 3 char
        self.data = [self.data[i : i + 3] for i in range(0, len(self.data), 3)]
        self.data = (
            self.data[0] + self.salt + self.data[1] + self.timestamp + self.data[2]
        )

        # Check if the salt is odd
        if self.saltlen % 2 == 0:
            # reverse the string
            self.data = self.data[::-1]
        else:
            # Add manipulation
            self.data = self.data[0 : self.saltlen + 1] + self.data[self.saltlen + 1 :]

        # If salt is numric
        if self.salt.isnumeric():
            # Reverse the string
            self.data = self.data[::-1]

        # Find pattern and replace
        replace = [
            ["0", "a"],
            ["!", "Abms"],
            ["ms1", "4ac"],
            ["ms2", "4bc"],
            ["ed", "adc"],
        ]

        # Replacing from a list of pattern
        for i in replace:
            self.data = self.data.replace(i[0], i[1])

        # Create a list of patter und replace
        self.data = [self.data[i : i + 2] for i in range(0, len(self.data), 2)]
        # Reverse every second element in the list
        self.data[::2] = self.data[::2][::-1]
        self.data = self.data[0 : self.saltlen + 1] + self.data[self.saltlen + 1 :]

        # Convert the list of string in a string
        self.data = "".join(self.data)

        # Create a list of patter und replace
        replace = [
            ["ex", "d"],
            ["x", "3"],
            ["4", "23g6"],
            ["6", "4"],
            ["4vs", "a3d"],
            ["sa", "a03"],
            ["2d", "Ac"],
            [" ", "c"],
            [".", "1e"],
        ]

        # Replacing again with a list of pattern
        for i in replace:
            # Replace the pattern
            self.data = self.data.replace(i[0], i[1])

        # Split in 5 char
        self.data = [self.data[i : i + 5] for i in range(0, len(self.data), 5)]
        # Set all upper case if the element is odd
        self.data[::2] = [i.upper() for i in self.data[::2]]

        # Convert the list of string in a string
        self.data = "".join(self.data)

        # Read file table.json
        with open("./hash/v1/replace.json", "r") as file:
            # Load the file
            replace = json.load(file)

        # Replacing again with a list of patterns
        for pattern in replace["content"]:
            self.data = self.data.replace(pattern[0], pattern[1])

        # Do the formatation
        self.data = self.data + "$" + self.salt + "$" + self.timestamp + "$"

        # Shift the string of lenght of salt - timestamp * length
        i = 0
        while i <= self.length * self.saltlen**self.difficulty:
            # Shift the string
            self.data = self.data[1:] + self.data[0]
            i += 1

        # If salt is numric
        if self.salt.isnumeric():
            # gcd
            self.gcd = self.difficulty % self.salt

            # Final shift algorithm: Shift by gcd * length ** difficulty
            i = 0
            while i <= self.length * self.gcd * self.difficulty:
                # Shift the string
                self.data = self.data[1:] + self.data[0]
                i += 1

        # Split in 5 char
        self.data = [self.data[i : i + 3] for i in range(0, len(self.data), 3)]

        # Exchange the first and last element
        self.data[0], self.data[-1] = self.data[-1], self.data[0]

        # Convert the list of string in a string
        self.data = "".join(self.data)

        # Return the hash
        return self.data.encode("utf-8")
