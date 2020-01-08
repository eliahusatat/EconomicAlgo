import doctest as doctest


class ObjectMatch():
    """
    this object represent a member in the matching
    he has dictionary that represent his partiality's about the second group.
    and he has name(str)
    """
    def __init__(self, name , partialities):
        self.name = name
        self.partialities = partialities
    # this function gets name frome the second group and return is partiality
    def get_partiality(self, name):
           return self.partialities.get(name)
    def get_name(self):
        return self.name



def check_stability(Match1):
    """
    this function gets matching (represent by dictionary)
    and check if the matching is stable
    :param Match1: Match from boys to girls
    :return: if the matching is stable
    >>> Aviva = ObjectMatch ("Aviva",{"Rafi": 1,"Shlomo": 2,"Tomer": 3})
    >>> Batya = ObjectMatch("Batya",{"Rafi": 2,"Shlomo": 1,"Tomer": 3})
    >>> Galya = ObjectMatch("Galya",{"Rafi": 3,"Shlomo": 1,"Tomer": 2})
    >>> Rafi = ObjectMatch( "Rafi",{"Aviva": 1, "Batya": 3, "Galya": 2})
    >>> Shlomo = ObjectMatch("Shlomo", {"Aviva": 1, "Batya": 2, "Galya": 3})
    >>> Tomer = ObjectMatch("Tomer",{"Aviva": 3, "Batya": 1, "Galya": 2})
    >>> m1 = {Rafi: Aviva, Shlomo : Batya , Tomer : Galya}
    >>> check_stability(m1)
    True
    >>> m2 = {Rafi: Galya , Shlomo : Aviva ,Tomer : Batya }
    >>> check_stability(m2)
    the couple: Rafi,Aviva is unstable couple
    False
    """
    Match2 = revers(Match1)
    for key1 in Match1.keys():
        for key2 in Match2.keys():
            #for each couple chack if is make the matching unstable
            if(is_couple_unstable(Match1,key1,key2)):
                print("the couple: {},{} is unstable couple".format(key1.get_name(),key2.get_name()))
                return False
    return True



def is_couple_unstable(Match1,first,second):
    """
    this function gets couple and check if the couple is unstable("mearer")
    :param Match1: Match from boys to girls
    :param first: the first one in the current couple
    :param second: the second one in the current couple
    :return: if the current couple is unstable
    >>> Aviva = ObjectMatch ("Aviva",{"Rafi": 1,"Shlomo": 2,"Tomer": 3})
    >>> Batya = ObjectMatch("Batya",{"Rafi": 2,"Shlomo": 1,"Tomer": 3})
    >>> Galya = ObjectMatch("Galya",{"Rafi": 3,"Shlomo": 1,"Tomer": 2})
    >>> Rafi = ObjectMatch("Rafi",{"Aviva": 1, "Batya": 3, "Galya": 2})
    >>> Shlomo = ObjectMatch("Shlomo", {"Aviva": 1, "Batya": 2, "Galya": 3})
    >>> Tomer = ObjectMatch("Tomer",{"Aviva": 3, "Batya": 1, "Galya": 2})
    >>> m1 = {Rafi: Galya , Shlomo : Aviva ,Tomer : Batya }
    >>> is_couple_unstable(m1,Rafi,Aviva)
    True
    >>> is_couple_unstable(m1,Rafi,Galya)
    False
    """

    Match2 = revers(Match1)
    real_partiality_first = first.get_partiality(Match1[first].get_name())
    real_partiality_second = second.get_partiality(Match2[second].get_name())
    partiality_first_to_second = first.get_partiality(second.get_name())
    partiality_second_to_first = second.get_partiality(first.get_name())
    if (partiality_first_to_second < real_partiality_first)and(partiality_second_to_first < real_partiality_second):
        return True
    else:
        return False


def revers(d):
     """
     this function gets dictionary and swap the keys with the values
     :param d: dictionary
     :return: swaped dictionary
     """
     return dict((v, k) for k, v in d.items())


if __name__ == "__main__":
    #(failures,tests) = doctest.testmod(report=True)
    #print ("{} failures, {} tests".format(failures,tests))
    """
    Rafi = 1
    Shlomo = 2
    Tomer = 3
    
    A = ObjectMatch ("A",{"Rafi": 1,"Shlomo": 2,"Tomer": 3})
    B = ObjectMatch("B",{"Tomer": 1,"Rafi": 2,"Shlomo": 3})
    C = ObjectMatch("C",{"Shlomo": 1,"Tomer": 2,"Rafi": 3})
    Rafi = ObjectMatch( "Rafi",{"C": 1, "B": 2, "A": 3})
    Shlomo = ObjectMatch("Shlomo", {"B": 1, "A": 2, "C": 3})
    Tomer = ObjectMatch("Tomer",{"A": 1, "C": 2, "B": 3})
    """
    A = ObjectMatch ("A",{"Tomer": 1,"Shlomo": 2,"Rafi": 3})
    B = ObjectMatch("B",{"Rafi": 1,"Tomer": 2,"Shlomo": 3})
    C = ObjectMatch("C",{"Shlomo": 1,"Rafi": 2,"Tomer": 3})
    Rafi = ObjectMatch( "Rafi",{"A": 1, "C": 2, "B": 3})
    Shlomo = ObjectMatch("Shlomo", {"B": 1, "A": 2, "C": 3})
    Tomer = ObjectMatch("Tomer",{"C": 1, "B": 2, "A": 3})

    m1 = {Rafi: B, Shlomo : A , Tomer : C}
    m2 = {Rafi: A, Shlomo: C, Tomer: B}
    m3 = {Rafi: C, Shlomo: B, Tomer: A}
    m4 = {Rafi: A, Shlomo : B , Tomer : C}
    m5 = {Rafi: B, Shlomo: C, Tomer: A}
    m6 = {Rafi: C, Shlomo: A, Tomer: B}
    #print(is_couple_unstable(m6,Tomer,C))
    print(check_stability(m1))
    print(check_stability(m2))
    print(check_stability(m3))

    print(check_stability(m4))
    print(check_stability(m5))
    print(check_stability(m6))

    """
    True
    True
    True
    
    the couple: Rafi,B is unstable couple
    False
    the couple: Shlomo,A is unstable couple
    False
    True
    """

