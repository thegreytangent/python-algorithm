def binary_search(a_list, n): 
    first = 0
    last = len(a_list) - 1
    print(last)
    while last >= first:
        
        mid = (first + last)
        
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
            
    return False

print(binary_search([1,2,3,4,5,6], 7))    
