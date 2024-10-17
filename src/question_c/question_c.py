#write functions here, don't add input('') statements here!
def get_sum_of_evens(num):
    sum=0
    if num==0:
        return sum
    elif num%2==0:
        sum +=num
    return sum+get_sum_of_evens(num-1)
print (get_sum_of_evens(8))