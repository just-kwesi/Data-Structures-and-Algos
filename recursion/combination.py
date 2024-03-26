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
    

def permute(nums):
        res = []

        if len(nums) ==1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res


permute([1,2,3])