def isPrime(n):
    return len(filter( 
        lambda x:x == 0,
        map(
            lambda y: n%y, range(2, int(n**0.5)+1)
        )
    )) == 0
test
for i in range(2, 100):
    if isPrime(i):
        print(i)
