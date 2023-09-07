def find_even_odd(lst):
    even = []
    odd =  []

    for element in lst:
        if element % 2 == 0:
            even.append(element)
        else:
            odd.append(element)
    return even,odd
lst = [1,2,3,4,2,4,6,8,256,465,32,6,41,22,31,101,20,100]
result = find_even_odd(lst)
print('List with Even Elements: ',result[0])
print('List with Odd Elements: ',result[1])