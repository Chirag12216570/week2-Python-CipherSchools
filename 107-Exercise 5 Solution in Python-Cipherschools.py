numbers=[6,60,2]
#printy(min(numbers))
#print(max(numbers))

def greatest_diff(l):
    return max(l)-min(l)

print(greatest_diff(numbers))