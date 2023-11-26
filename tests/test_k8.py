import os
import requests

def test_k8():

    url = os.getenv("K8_URL")
    res = requests.get(f"{url}/?start=8")
    assert "Fizz" not in res.text

    res = requests.get(f"{url}/?start=5&end=5")
    assert "Buzz" not in res.text
