size = input().split()
choosing_size = input().split()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# print(size)
# print(choosing_size)
# print(A)
# print(B)

def min_max_array(array_A, array_B, chosing_size):
    choosing_size_A = int(chosing_size[0])
    choosing_size_B = int(chosing_size[1])

    small_list= array_A[:choosing_size_A]
    large_list = array_B[-choosing_size_B:]
    if max(small_list) < min(large_list):
        return print('YES')
    else:
        return print('NO')


min_max_array(A, B, choosing_size)