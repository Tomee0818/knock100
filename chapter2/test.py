import sys
  
def split_list(l, n):
    spl = []

    for i in range(0, len(l), n):
        spl.append(l[i:i+n])

    return spl
    
li = [1,2,3,4,5,6,7,8,9,10]

result = split_list(li, 3)

print(result)