string_T = input()
string_S = input()
# print(list(string_T))


def Vitaly_and_String(string1, string2):
    string1 = list(string1)
    # string2 = list(string2)
    for i in range(len(string1)-1,-1,-1):
        if string1[i] == 'z':
            string1[i] = 'a'
        else:
            string1[i] = chr(ord(string1[i])+1)
            break
    final_string = ''.join(string1)
    if final_string == string2:
        return print('No such string')
    else:
        return print(final_string)

Vitaly_and_String(string_T, string_S)
