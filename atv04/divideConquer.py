 
def binarySearch(arr, l, r, x):
 
    # Checando o caso base
    if r >= l:

        mid = l + (r - l) // 2
 
        # se o elemento está presente no meio
        if arr[mid] == x:
            return mid
 
        # Se for menor que o meio
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, arr[mid-1])
 
        # se não, estará a direita
        else:
            return binarySearch(arr, mid + 1, r, arr[mid+1])
 
    else:
        # Elemento não está presente no array
        return -1
 

# Dados
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = arr[0] #primeiro elemento
 
# Chamada da função
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")