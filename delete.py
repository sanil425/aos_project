
import numpy as np
import math

def main():
    D =  [0.125, 0.125, 0.25, 0.5]
    values = [0,1,2,3]
    Yn = 1.9
    n = 40

    print(z_score(D,values,Yn,n))


def expected(D, values):
    return np.dot(D,values)


def variance(D,values):
    res = 0
    mu = expected(D,values)
    for i in range(len(D)):
        res += D[i] * (values[i] - mu)**2 
    return res


def z_score(D,values,Yn,n):
    mu = expected(D,values)
    var = variance(D,values)


    return (Yn - mu) / np.sqrt(var/ n)


def p_val():
    
    


if __name__ == "__main__":
    main()