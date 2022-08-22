nb = int(input())
array = list(map(int,input().split()))

def reverse_array(array):
    if len(array) == 2:
        print('yes')
        print(1, 1)
    else:
        array.insert(0,0)
        # print(array)
        left_index = 0
        for i in range(len(array)-1):
            if array[i+1]- array[i] <0:
                left_index = i
                break
            else:
                pass
        # print(left_index)
        if left_index == 0:
            print('yes')
            print(1,1)
            return
        else:
            right_index = len(array) - 1
            cache = []
            while left_index < right_index:
                if array[left_index] < array[right_index]:
                    right_index -=1
                elif array[left_index] > array[right_index]:
                    cache.append(left_index)
                    cache.append(right_index)
                    array[left_index], array[right_index] = array[right_index], array[left_index]
                    left_index +=1
                    right_index -=1


            if len(cache) == 0 or array != sorted(array):
                print('no')
            else:
                print('yes')

                print(str(cache[:2]).replace(',', ' ')[1:-1])

reverse_array(array)