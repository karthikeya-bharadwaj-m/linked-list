A = list(map(int,input("enter the list:").split()))
B=[0]*len(A)
for i in range(len(A)-1):
    B[i]= A[i]+A[i+1]
B[i+1]= A[-1]
print (B)
