import logging
import azure.functions as func

import sympy as sym

def Fib(n):
    x = sym.symbols('x', nonnegative=True, integer=True)
    Fib = 1 / sym.sqrt(5) * (((1+sym.sqrt(5))/2)**(n-1) - ((1-sym.sqrt(5))/2)**(n-1))
    result = Fib.subs(x, n) 
    result = sym.simplify(result) 
    return result

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    num = req.params.get('num')
    if not num:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            num = req_body.get('num')

    if num:
        Fiblist = []

        for n in range(1, int(num)):
            Fiblist += [Fib(n)]

        return func.HttpResponse(
            f"Fibonacci sequence : {Fiblist}"
        )
    
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
