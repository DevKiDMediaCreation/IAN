import SAHF_512 as sahf
import random, string
import time

for i in range(9):
    start = time.time()
    # Create random string to hash with SAHF_512
    hasdh = sahf.SAHF_512(
        "".join(random.choices(string.ascii_letters + string.digits, k=20)),
        str(random.randint(0, 1000))
        + str(random.random())
        + "".join(random.choices(string.ascii_letters + string.digits, k=3)),
        difficulty=i + 1,
    ).hash()
    print(str(time.time() - start) + "s, Test:" + str(i + 1))

for i in range(9):
    start = time.time()
    # Create random string to hash with SAHF_512
    hasdh = sahf.SAHF_512(
        "".join(random.choices(string.ascii_letters + string.digits, k=100)),
        random.randint(0, 1000000) + random.random(),
        difficulty=i + 1,
    ).hash()
    print(str(time.time() - start) + "s, Test:" + str(i + 1))
