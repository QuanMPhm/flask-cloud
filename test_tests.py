from app import fizzbuzz
from app import app

def test_fizzbuzz():
    assert fizzbuzz(1, 1) == str([1])
    assert fizzbuzz(3, 5) == str(['Fizz', 4, 'Buzz'])
    assert fizzbuzz(15,15) == str(['Fizz Buzz'])

def test_endpoint():
    res = app.test_client().get('/?start=3&end=3')
    assert str(['Fizz']) == res.text

    res = app.test_client().get('/?start=3')
    assert str(['Fizz']) != res.text

