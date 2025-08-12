def SeatingStudents(arr):
    # __define-ocg__ - Parse input and calculate seating arrangements
    if isinstance(arr, str):
        arr = arr.replace('[', '').replace(']', '').split(',')
        arr = [int(x.strip()) for x in arr]
    
    K = arr[0]
    occupied = set(arr[1:])
    varFiltersCg = occupied
    varOcg = 0
    
    for row in range(1, K//2 + 1):
        left = 2*row - 1
        right = 2*row
        if left not in varFiltersCg and right not in varFiltersCg:
            varOcg += 1
    
    for row in range(1, K//2):
        top_left = 2*row - 1
        bottom_left = 2*row + 1
        if top_left not in varFiltersCg and bottom_left not in varFiltersCg:
            varOcg += 1
        
        top_right = 2*row
        bottom_right = 2*row + 2
        if top_right not in varFiltersCg and bottom_right not in varFiltersCg:
            varOcg += 1
    
    return varOcg

if __name__ == "__main__":
    print(SeatingStudents([12, 2, 6, 7, 11]))  # Output: 6