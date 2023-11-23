from flask import Flask, request

from markupsafe import escape

def fizzbuzz(start, end):

    res = []
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0: res.append("Fizz Buzz")
        elif i % 3 == 0: res.append("Fizz")
        elif i % 5 == 0: res.append("Buz")
        else: res.append(i)

    return str(res)


app = Flask(__name__)

@app.route("/")
def hello_world():
    start_int = request.args.get('start', None, type=int)
    end_int = request.args.get('end', None, type=int)

    if start_int is None and end_int is not None \
    or start_int is not None and end_int is  None:
        return "Please provide both start and end parameters, not just one or the other!"

    if start_int is None: return fizzbuzz(1, 100)
    
    if start_int > end_int: return "The start cannot be higher than the end!"
    else: return fizzbuzz(start_int, end_int)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'