## Fibonacci API

This project creates an API that returns a Fibonacci number for a given number passed as parameter in the request. The algorith used to generate the Fibonacci number is available in [wikipedia](https://en.wikipedia.org/wiki/Fibonacci_sequence#Matrix_form) in the *Matrix Form* section. And the implementation in python of this mathematical formula is available in [stackoverflow](https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series).



### Libraries and technologies

* Python 3.11.5
* Flask
* Pytest
* Gunicorn
* Docker
* Makefile

### Installation

#### Windows User

In order to install and use make command it is necessary to install *chocolatey* package manager. To do that, follow the installation instructions on the  [official page](https://chocolatey.org/install#individual) and then run:

```
choco install make 
```
#### Linux User

The make and docker installation depends on the linux distribution therefore it is suggested the user do an independent installation.

#### Docker initialization


To initialize the Fibonacci API it is required to have docker and make installed. All commands below must be executed on the project root directory.

To build the docker image and run the container use the following instructions:

```
make 
```

To build the image, inform the build target as following:

```
make build
```

If the image is already built, to run the API inform the run target as following:

```
make run
```

To stop the remove the API container, run:

```
make stop
```

### Usage

The API only have a single endpoint and it requires a route parameter which is the number to be used to calculate the nth element of the Fibonacci series.

Example:

*http://127.0.0.0:5000/6*

This example should return the number 8. If any non integer argument is passed to the API then it returns 404 as the HTTP status code.

### Tests

Tests were implemented using pytest and checked for negative, positive, large and float numbers as well as non integer entries.

To run the tests, run:

```
pytest -v
```

*-v* is to visualize which tests passed and failed
