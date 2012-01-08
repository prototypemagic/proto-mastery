
def counting(num):
    output = []
    while num > 0:
        word = raw_input()
        if len(list(word)) > 10:
            word = list(word)
            yo = str(len(word)-2)
            output.append(word[0] + yo + word[-1])
        else:
            output.append(word)
    
        num = num-1
    return output

num = int(raw_input())
output = counting(num)
times = len(output) - 1
l = 0
while l <= times:
    print output[l]
    l = l + 1




