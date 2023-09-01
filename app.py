import sys
from flask import Flask
from flasgger import Swagger

sys.path.append(".")
from api.fibonacci import fib


app = Flask(__name__)
swagger = Swagger(app)

@app.route("/<int:n>", methods=['GET'])
def home(n=0):

    """
    Receives an integer and returns the Fibonacci number as a request response
    ---
    parameters:
      - name: n
        in: path
        type: int
        required: true
        default: 0

    responses:

        200:
            description: A Fibonacci nth element
        404:
            description: Invalid parameter passed or route accessed

    """
    return str(fib(n))
    
