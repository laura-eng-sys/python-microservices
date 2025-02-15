from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}


# this first solution works
# def test_read_phrase():
#    response = client.get("/phrase/Barack Obama")
#    assert response.status_code == 200
#    assert response.json() == {"message": "Wikipedia API. Call /search or /wiki"}
# run python main.py, then go to the browser, and search phrase/barack obama, copy the result and paste it in the code below


# you can also use this solution below
def test_read_phrase():
    response = client.get("/phrase/Barack Obama")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "barack hussein obama ii",
            "august",
            "american politician",
            "44th president",
        ]
    }
