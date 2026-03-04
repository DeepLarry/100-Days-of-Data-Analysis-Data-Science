n=int(input("Enter the number of elements: "))
arr=list(map(int,input("Enter the elements: ").split()))
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("Element\tFrequency")
for key,value in freq.items():
    print(f"{key}\t{value}")
    