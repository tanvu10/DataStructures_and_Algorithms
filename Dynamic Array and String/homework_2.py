
input_list = input()
# print(ord(s) - 97)
# print(ord(input_list[0]) - 97)

def counting_rotation(string_input):
    cumsum_rotation = 0
    current_index = 0
    for i in range(len(string_input)):
        real_index_order = ord(string_input[i]) - 97
        distance = abs(real_index_order - current_index)
        # print(string_input[i], 'index is', real_index_order, 'distance', distance, 'cdis', 26-distance)
        if distance >= (26- distance):
            # print( 26- distance)
            cumsum_rotation += (26- distance)
        else:
            cumsum_rotation += distance
            # print(distance)
        current_index = real_index_order
    return print(cumsum_rotation)

counting_rotation(input_list)





