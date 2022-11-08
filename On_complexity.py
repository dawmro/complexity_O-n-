import time


# creating assigment n+1 times
# run time linear to input size 
# complexity O(n)
def sum1(n):
    result = 0
    for x in range(n+1):
        result += x
    return result


def sum2(n):
    return (n*(n+1))/2


if __name__ == '__main__':

    input_val = 100000000
    
    startTime = time.time()
    sum1(input_val)
    endTime = time.time()
    print(f"sum1 run tume: {endTime - startTime}")  

    startTime = time.time()
    sum2(input_val)
    endTime = time.time()
    print(f"sum2 run tume: {endTime - startTime}")   
        
