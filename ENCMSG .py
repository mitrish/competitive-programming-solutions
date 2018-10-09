T = int(input())
while(T):
    T -= 1
    N = int(input())
    S = str(input())
    temp = ""
    for i in range(0,N,2):
        if(i == N-1):
            temp += S[i]
            break
        a =  S[i+1] + S[i]
        temp += a
    final_temp = ""
    for i in temp:
        j = ord(i)
        val = 122-j
        updated_val = 97+val
        char = chr(updated_val)
        final_temp += char
    print(final_temp)