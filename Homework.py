def odd_num(x):
    return x%2!=0
a_list=[1,2,3,4,5,6,7,8,9]
b_list=list(filter(odd_num,a_list))
print(b_list)

def even_num(x):
    return x%2==0
c_list=list(filter(even_num,a_list))
print(c_list)

def sum_of_list(odd_num):
    return sum(odd_num)
total_sum=sum_of_list(b_list)
print(total_sum)

def sum_of_list(even_num):
    return sum(even_num)
total_sum=sum_of_list(c_list)
print(total_sum)