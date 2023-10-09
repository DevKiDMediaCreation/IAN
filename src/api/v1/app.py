from fastapi import FastAPI
from hash.v0.SAHF0_512 import SAHF0_512
import random
import string

# Add Port
# uvicorn app:app --reload --port 23598
# uvicorn app:app --reload --host

version = "/api/v1"

app = FastAPI(
    title="IAN REST API", description="Secure by KNIAN API Interface", version="0.0.1"
)

# Add a route by /v1/ as version


@app.get(version + "/")
async def root():
    # Create random string to hash with SAHF0_512
    hasdh = SAHF0_512(
        "".join(random.choices(string.ascii_letters + string.digits, k=100)),
        random.randint(0, 1000000) + random.random(),
    )
    return {
        "message": "Hello World",
        "status": 404,
        "code": hasdh.hash(),
        "hash": "SAHF0_512",
    }


@app.get(version + "/test/{times}")
async def test(times: int):
    hasdh = []
    for i in range(times):
        p1 = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        p2 = random.randint(0, 100) + random.random()
        hasdh.append([SAHF0_512(p1, p2).hash(), p1, p2])
    return {"Status": "OK", "content": hasdh, "hash": "SAHF0_512"}


@app.get(version + "/archive/{item_id}")
async def read_item(item_id: int):
    hash = SAHF0_512(str(item_id))#, difficulty=5)
    return {
        "item_id": hash.hash(),
        # "difficulty": hash.__difficulty__(),
        "hash": "SAHF0_512",
        "record": f"{item_id} has been hashed with SAHF0_512",
        "Status": "OK 200",
    }


@app.get(version + "/random/{times}")
async def random_endpoint(times: int):
    result = []
    for i in range(times):
        len_p1 = random.randint(1, 4)
        len_p2 = random.randint(1, 3)
        p1 = "".join(random.choices(string.ascii_letters + string.digits, k=len_p1))
        p2 = "".join(random.choices(string.ascii_letters + string.digits, k=len_p2))
        result.append([p1, p2])
    return {"content": result}
