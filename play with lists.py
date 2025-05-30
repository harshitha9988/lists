a=[4,5,1,2,9,7,10,8]
print("Original List: ",a)

count=0
for i in a:
    count+=i

avg=count/len(a)
print("sum = ",count)
print("average = ",avg)

a.sort()
print("Smallest element is:", a[0])

print("Largest element is:", a[-1])