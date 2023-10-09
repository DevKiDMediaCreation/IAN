#
# Hashing algorithm by SAHF, KENECTICS and DevKiD 10/08/2023 (c)
# Version: 1.0.0
#

import json


class SAHF3_512:  # Secure Advanced Hashing Function # Duy Nam Sinus Aetheny Hashing Algorithm DNSA
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
        self.difficulty = 1 if difficulty == 1 else difficulty
        self.saltlen = self.salt.__len__()

    def __len__(self) -> int:
        return self.data.__len__()

    def __str__(self) -> str:
        return self.data

    def __difficulty__(self) -> int:
        return self.difficulty

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

        # Set every char a vector position
        self.data = [ord(i) for i in self.data]

        # Multiply each element by the length of the string and the saltlen
        self.data = [i * self.length * self.saltlen for i in self.data]

        # Convert the list of int in a string
        self.data = "".join([str(i) for i in self.data])

        # Create a list of patter und replace
        self.data = [self.data[i : i + 2] for i in range(0, len(self.data), 2)]
        # Reverse every second element in the list
        self.data[::2] = self.data[::2][::-1]
        self.data = self.data[0 : self.saltlen + 1] + self.data[self.saltlen + 1 :]

        # Convert the list of string in a string
        self.data = "".join(self.data)

        # Split in 5 char
        self.data = [self.data[i : i + 5] for i in range(0, len(self.data), 5)]
        # Set all upper case if the element is odd
        self.data[::2] = [i.upper() for i in self.data[::2]]

        # Convert the list of string in a string
        self.data = "".join(self.data)

        # Read file table.json
        with open("./replace.json", "r") as file:
            # Load the file
            replace = json.load(file)

        # Replacing again with a list of patterns
        for pattern in replace["content"]:
            # Set a max-length of 512
            if self.data.__len__() <= 512 * int(self.difficulty):
                # Replace the pattern
                self.data = self.data.replace(pattern[0], pattern[1])

        # Read file table.json
        with open("./replace_2.json", "r") as file:
            # Load the file
            replace = json.load(file)

        # Replacing again with a list of patterns
        for pattern in replace["content"]:
            # Set a max-length of 512
            if self.data.__len__() <= 512 * int(self.difficulty):
                # Replace the pattern
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
            while i <= self.length * self.gcd**self.difficulty:
                # Shift the string
                self.data = self.data[1:] + self.data[0]
                i += 1

        # Split in 5 char
        self.data = [self.data[i : i + 3] for i in range(0, len(self.data), 3)]

        # Exchange the first and last element
        self.data[0], self.data[-1] = self.data[-1], self.data[0]

        # Split the salt in char
        self.salt = [self.salt[i : i + 1] for i in range(0, len(self.salt), 1)]
        # Convert string in number
        self.salt = [ord(i) for i in self.salt]
        # Difficult to binary
        self.difficulty = bin(self.difficulty)

        # Add to every salt to difficult
        self.salt = [i + int(self.difficulty, 2) for i in self.salt]

        # Get the sum of the salt and give it to every element of char
        self.data = [i + str(sum(self.salt)) for i in self.data]

        self.data = self.data + self.data[::-1]

        # Convert the list of string in a string
        self.data = "".join(self.data)

        # Return the hash
        return self.data.encode("utf-8")

print(SAHF3_512("Hello World").hash())