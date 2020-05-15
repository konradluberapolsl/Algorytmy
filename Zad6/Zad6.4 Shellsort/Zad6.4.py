def shell_sort(arr):
    inc = len(arr) // 2
    while inc:
        for i, el in enumerate(arr[inc:], inc):
            while i >= inc and arr[i - inc] > el:
                arr[i] = arr[i - inc]
                i -= inc
            arr[i] = el
        inc = 1 if inc == 2 else inc * 5 // 11
