import doctest as doctest


def choices(values):
    """
    this function represent a monotonic role of choice:
    choose the max number
    :param values: list of int that represent the values
    :return:binary list - with how chosen
    >>> val=[4,5,8,10]
    >>> print(choices(val))
    [0, 0, 0, 1]
    >>> val=[4,5,7,2]
    >>> print(choices(val))
    [0, 0, 1, 0]
    >>> val=[3,5,1,1]
    >>> print(choices(val))
    [0, 1, 0, 0]
    """
    size = len(values)
    ans = [0]*size
    max = values[0]
    index = 0
    for i in range(0,size):
        if(values[i] > max):
            max = values[i]
            index = i
    ans[index] = 1
    return ans


def payments(values):
    """
    this function calculate the role of price according
    to Maison
    :param values: list of int that represent the values
    :return: list of int that represent the price every agent needs to pay
    >>> val=[4,5,8,10]
    >>> print(payments(val))
    [0, 0, 0, 7.990000000000043]
    >>> val=[4,5,8,7]
    >>> print(payments(val))
    [0, 0, 6.9900000000000215, 0]
    >>> val=[2,5,1,2]
    >>> print(payments(val))
    [0, 1.990000000000064, 0, 0]

    """
    if(chacks_of_monotonic(values)== False):
        raise Exception('not a monotonic role of choice!!!')
    size = len(values)
    ans = [0]*size
    for i in range(0,size):
        temp = personal_price(values,i)
        if(values[i] >= temp):
            ans[i] = temp
    return ans



def personal_price(values,x):
    """
    this function calculate the number "Saf value"
    of specific agent
    :param values: list of int that represent the values
    :param x: the index of the agent int the list
    :return: "Saf value" of x

    >>> val=[4,5,8,10]
    >>> print(personal_price(val,0))
    10.009999999999872
    >>> val=[4,5,8,10]
    >>> print(personal_price(val,1))
    10.009999999999893
    >>> val=[4,5,8,10]
    >>> print(personal_price(val,2))
    10.009999999999957
    >>> val=[4,5,8,10]
    >>> print(personal_price(val,3))
    7.990000000000043
    """
    temp = values[x]
    ans = values[x]
    if(choices(values)[x]==0):
        while(choices(values)[x]==0):
            ans += 0.01
            values[x] = ans
    else:
        while(choices(values)[x]==1):
            ans -= 0.01
            values[x] = ans
    values[x] = temp
    return ans

def chacks_of_monotonic(values):
    """
    this function does some checks for monotonic
    note! this function its not "if and only if"
    this is only does some checks - if it return true its doesnt mean that
    the role is monotonic
    but if it return false its mean that the role is not monotonic
    :param values: list of int that represent the values
    :return: true if the role stand in all the checks

    >>> val=[4,5,8,10]
    >>> print(chacks_of_monotonic(val))
    True
    """
    flag = True
    for i in range(0,len(values)):
        temp = values [i]
        if(choices(values)[i]==0):
            for j in range(0,1000):
                values[i] -= 0.01
                if(choices(values)[i]==1):
                   flag = False
        else:
            for j in range(0,1000):
                values[i]+= 0.01
                if(choices(values)[i]==0):
                   flag = False
        values[i] = temp
        if(flag == False):
            break
    return flag


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
