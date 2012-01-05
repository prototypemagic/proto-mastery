
def max_if_exchanged(num):
    return num/2 + num/3 + num/4
     
def check(num):
    exchanged = max_if_exchanged(num)
    return num if num > exchanged else exchanged
              
if __name__ == "__main__":
    while True:
       try:
           n = int(raw_input())
           print check(n)
       except:
           break
