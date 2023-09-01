import sys
from flask import Flask

sys.path.append(".")
from api.fibonacci import fib


app = Flask(__name__)


@app.route("/<int:n>", methods=['GET'])
def home(n=0):

    """
    Receives an integer and returns the Gibonacci number as a request response

    Arguments:

    n (int): Number to be used in fibonacci series
    """
    return str(fib(n))
    
