import os
import requests

def test_k8():

    url = os.getenv("K8_URL")
    res = requests.get(f"{url}/?start=8")
    assert "Fizz" not in res.text

    res = requests.get(f"{url}/?start=5&end=5")
    assert "Buzz" in res.text


# # os.environ['NO_PROXY'] = '127.0.0.1'
# res = requests.get("http://localhost:5000")
# print(res.text)