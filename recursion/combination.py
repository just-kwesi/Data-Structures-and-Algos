def combine(n: int, k: int):
        res =  []

        def backtrack(start,curArr):
            if len(curArr) == k:
                res.append(curArr.copy())
                return

            for i in range(start,n+1):
                curArr.append(i)
                backtrack(i+1,curArr)
                curArr.pop()


        
        backtrack(1,[])
        print(res)
        return res
    


combine(4,2)