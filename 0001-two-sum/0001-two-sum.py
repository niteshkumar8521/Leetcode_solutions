def two_sum(arr, target):
    seen = {}
    
    for i in range(len(arr)):
        num = arr[i]
        needed = target - num
        
        if needed in seen:
            return [seen[needed], i]
        
        seen[num] = i