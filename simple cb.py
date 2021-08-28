def gethint(secret,guess):
    a=str(secret)
    b=str(guess)
    bull=0
    bucket=[0]*10
    for s,g in  zip(a,b):
        if s==g:
            bull+=1
        else:
            bucket[int(s)]+=1
            bucket[int(g)]+=1
        A=bull
        B=len(a)-bull-sum(x for x in bucket if x>0)
    return('bull:',A,'cows:',B)
secret=int(input('enter the secret number: '))
guess=int(input('enter the guessed number: '))
gethint(secret,guess)