import math


def TakeInput() -> None:
    n = [int(i) for i in input().split()]
    return n


def CalcMean(array: list, num_of_elem: int) -> int:
    return sum(array) / num_of_elem


def Calc_Std_deviation(array, num_of_elem):
    
    M = CalcMean(array, num_of_elem)
    
    s = []
    for i in array:
        s.append(i - M)
    sum_square = sum([i ** 2 for i in s])
    sigma = math.sqrt(sum_square / num_of_elem)
    return sigma
    

def main():
    array = TakeInput()
    num_of_elem = len(array)
    
    CalcMean(array, num_of_elem)
    result = Calc_Std_deviation(array, num_of_elem)
    print(f'{result:2f}')
    
    
if __name__ == '__main__':
    main()