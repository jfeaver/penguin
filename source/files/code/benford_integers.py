"""
Benford Distribution Checker!

AUTHORS:

- Amy Feaver (2013-07-13)

- Anne Ho (2013-07-13)

- Michelle Manes (2013-07-13) 

- We would also like to thank Alina Bucur and Kate Thompson, our group members at the 
  Women in Sage workshop where we wrote this code!

Last updated July 2016

"""

import sage.libs.all

import scipy
import numpy

from scipy import stats
from numpy import array

import matplotlib.pyplot




def create_Benford_prediction(DataList, base):
    """
    INPUT:

    - ``DataList`` -- a list of real numbers

    - ``base`` -- an integer greater than or equal to 2

    OUTPUT:

    A list of length ceil(base), such that for 0 <= i <= ceil(b)-1, the i-th 
    position of the list contains the predicted number of items in the list
    which should start with the digit i under the Benford distribution 
    (when the numbers in DataList are converted to the specified base).

    EXAMPLES:

        sage: Benford_prediction([i for i in range(40)],10)
        [0, 12.0411998265592, 7.04365036222725, 4.99754946433200, 3.87640052032226, 3.16724984190499, 2.67787158522453, 2.31967787910747, 2.04610089789525, 1.83029962242701]

        sage: Benford_prediction([sqrt(2)*i^2 for i in range(3,81)],5.4402)
        [0, 31.9193381529151, 18.6716158672934, 13.2477222856217, 10.2757317216334, 8.39588414565996]

    """
    b = base
    size = len(DataList)
    first_digit_Benford = []
    first_digit_Benford.append(0)
    for d in range(1,b):
        q =log(1+1.0/d, b).n()
        first_digit_Benford.append((q*size).n())
    return first_digit_Benford



def get_first_digit_count(DataList, base):
    """
    INPUT:

    - ``DataList`` -- a list of real numbers

    - ``base`` -- a real number greater than or equal to 2

    OUTPUT:

    A list of length ceil(base), such that for 0 <= i <= ceil(base)-1, the i-th 
    position of the list contains the  number of items in the list which start 
    with the digit i (when the numbers in DataList are converted to the specified base).

    EXAMPLES:

        sage: Benford_count([0,-1,2,3,75],35/4)
        [1, 1, 1, 1, 0, 0, 0, 0, 1]

        sage: Benford_count([i for i in range(30)],10)
        [1, 11, 11, 1, 1, 1, 1, 1, 1, 1]

    """
    b = base  
    data = list(DataList)
    data.sort()
    first_digit_data = []
    for i in range(b):
        first_digit_data.append(0) 
    powers_of_b = [b]
    powpow = b    
    while powpow < DataList[-1]:
        powpow = powpow**2
        powers_of_b.append(powpow) 
    for n in data:
        q = abs(n)
        while q >= b:
            powpow = b
            for power in powers_of_b:
                if power <= q:
                    powpow = power
                else:
                    break               
            q = q//powpow
        first_digit_data[q] += 1  
    return first_digit_data



class BenfordChecker:
    

    def __init__(self,data_list,base):
        if len(data_list)==0:
            raise ValueError, "data list must be nonempty"
        if base<=1:
            raise ValueError, "base must be greater than 1"
        self.__data_list = data_list
        self.__base = base
        self.__Benny = create_Benford_prediction(data_list,base)
        self.__first_digit_count = get_first_digit_count(data_list,base)


    def data_list(self):
        return self.__data_list

    def base(self):
        return self.__base

    def Benford_prediction(self):
        return self.__Benny

    def first_digit_count(self):
        return self.__first_digit_count


    def Benford_chi_square(self):
        """
        INPUT:

        - DataList -- a list of real numbers

        - base -- a real number greater than or equal to 2

        OUTPUT:

        A list containing, first, the chi-squared value and, second, the associated p-value.

        EXAMPLES:

            sage: Benford_chi_square([1,2,3,4,5],3)
            (0.61378226057799101, 0.4333672659230694)

            sage: Benford_chi_square([i for i in range(30)],10)
            (11.78779211948263, 0.16092617606270504)

        """
        prediction = list(self.__Benny)
        count = list(self.__first_digit_count)
        del prediction[0]
        del count[0]
        cs = scipy.stats.chisquare(numpy.array(count),numpy.array(prediction))
        return cs


    def bar_graph(self):
        N = self.__base
        ind = numpy.arange(N)
        width = .35
        p1 = matplotlib.pyplot.bar(ind, self.__Benny, width, color='#669966')
        p2 = matplotlib.pyplot.bar(ind+.35, self.__first_digit_count, width, color='#66CCCC')
        matplotlib.pyplot.title('Benford Distribution')
        matplotlib.pyplot.legend( (p1[0], p2[0]), ('Prediction', 'Count') )
        matplotlib.pyplot.savefig('Graph.png')
        matplotlib.pyplot.close()

    def line_graph(self):
        p1 = matplotlib.pyplot.plot(self.__Benny, color='#669966')
        p2 = matplotlib.pyplot.plot(self.__first_digit_count, color='#66CCCC')
        matplotlib.pyplot.title('Benford Distribution')
        matplotlib.pyplot.legend( (p1[0], p2[0]), ('Prediction', 'Count') )
        matplotlib.pyplot.savefig('Graph.png')
        matplotlib.pyplot.close()
    
    

