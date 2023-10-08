from fastapi import FastAPI
from hash.v1.SAHF_512 import SAHF_512
import random
import string

# Add Port
# uvicorn app:app --reload --port 23598
# uvicorn app:app --reload --host

app = FastAPI(
    title="IAN REST API", description="Secure by KNIAN API Interface", version="0.0.1"
)

# Add a route by /v1/ as version


@app.get("/")
async def root():
    # Create random string to hash with SAHF_512
    hasdh = SAHF_512(
        "".join(random.choices(string.ascii_letters + string.digits, k=100)),
        random.randint(0, 1000000) + random.random(),
    )
    return {
        "message": "Hello World",
        "status": 404,
        "code": hasdh.hash(),
        "hash": "SAHF_512",
    }


@app.get("/test/{times}")
async def test(times: int):
    hasdh = []
    for i in range(times):
        p1 = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        p2 = random.randint(0, 100) + random.random()
        hasdh.append([SAHF_512(p1, p2).hash(), p1, p2])
    return {"Status": "OK", "content": hasdh, "hash": "SAHF_512"}


@app.get("/archive/{item_id}")
async def read_item(item_id: int):
    return {"item_id": SAHF_512(str(item_id), difficulty=10).hash()}


@app.delete("/archive/:archive_record_id")
async def del_archive(archive_record_id: int):
    return {"archive_record_id": archive_record_id}


@app.get("/random/{times}")
async def random_endpoint(times: int):
    result = []
    for i in range(times):
        len_p1 = random.randint(1, 10)
        len_p2 = random.randint(1, 5)
        p1 = "".join(random.choices(string.ascii_letters + string.digits, k=len_p1))
        p2 = "".join(random.choices(string.ascii_letters + string.digits, k=len_p2))
        result.append([p1, p2])
    return {"content": result}
