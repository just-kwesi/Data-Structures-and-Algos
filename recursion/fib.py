def fib( n: int) -> int:
        cache = {}
        
        def fib_rec(num):
            if num in cache:
                return cache[num]
            
            if num < 2:
                return num
            
            res = fib_rec(num-1) + fib_rec(num-2)
            cache[num] = res
            return res
        
        return fib_rec(n)
    

fib(6)