def fib(n: int = 0) -> int:

    """
        Receives an integer and returns the corresponding Fibonacci number

        Arguments:

        n (int): Number to be used in fibonacci series
    """

    if (n < 0):
        raise ValueError(f"Expected an unsigned integer as input. Received: {n}")
    if (n == 0):
        return 0

    v1, v2, v3 = 1, 1, 0    
    for rec in bin(n)[3:]: 
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':  
            v1, v2, v3 = v1+v2, v1, v2
    return v2