from app import app


def test_fib_zero_value():
# test the Fibonacci response for parameter=0
    with app.test_client() as client:
        response = client.get("/0").data.decode()
        assert response=="0"


def test_fib_positive_value():
# test the Fibonacci response for a positive integer parameter
    with app.test_client() as client:
        response = client.get("/5").data.decode()
        assert response=="5"

def test_fib_large_value():
# test the Fibonacci response for a positive integer large parameter
    with app.test_client() as client:
        response = client.get("/1000").data.decode()
        assert response=="43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875"

def test_fib_negative_value():
# test the Fibonacci response for a negative integer parameter
    with app.test_client() as client:
        response = client.get("/-1").status_code
        assert response==404

def test_fib_non_integer_value():
# test the Fibonacci response for a non integer parameter
    with app.test_client() as client:
        response = client.get("/hire_me").status_code
        assert response==404

def test_fib_float_value():
# test the Fibonacci response for a non integer parameter
    with app.test_client() as client:
        response = client.get("/19,3").status_code
        assert response==404