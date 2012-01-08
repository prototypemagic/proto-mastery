
def counting(num):
    output = []
    while num > 0:
        word = raw_input()
        if len(word) > 10:
            word = list(word)
            output.append(word[0] + str(len(word)-2) + word[-1])
        else:
            output.append(word)
    
        num = num-1
    return output

output = counting(int(raw_input()))
for x in range(len(output)):
    print output[x]




