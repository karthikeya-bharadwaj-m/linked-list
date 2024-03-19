def solution (A):
    max_sum  = -1
    dig_set = [set(str(i)) for i in A]
    both_num = ()
    for i in range (len(A)):
        for j in range(i+1,len(A)):
            if not dig_set[i].intersection(dig_set[j]):
                cur_sum = A[i]+ A[j]
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    both_num = (A[i], A[j])
    return max_sum
A = list(map(int,input("enter array:").split()))
print(solution(A))
