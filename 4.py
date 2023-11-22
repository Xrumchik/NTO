n = int(input())
arr_x = list(map(int, input().split()))
arr_h = list(map(int, input().split()))

arr_right = [1]
index_right = 0
flag = 0
i = 0
while i < n - 1:
    if flag:
        if arr_x[i] + arr_h[i] == arr_x[i + 1]:
            arr_right[index_right] += 1
        elif arr_x[i] + arr_h[i] > arr_x[i + 1]:
            start_i = i
            while arr_x[start_i] + arr_h[start_i] >= arr_x[i]:
                arr_right[index_right] += 1
                i += 1
                if i == n - 1:
                    break
                if arr_x[start_i] + arr_h[start_i] == arr_x[i] or arr_x[start_i] + arr_h[start_i] < arr_x[i + 1]:
                    break
            i -= 1
        else:
            flag = 0
            index_right += 1
            arr_right.append(1)
    else:
        if arr_x[i] + arr_h[i] == arr_x[i + 1]:
            flag = 1
            arr_right[index_right] += 1
        elif arr_x[i] + arr_h[i] > arr_x[i + 1]:
            start_i = i
            while arr_x[start_i] + arr_h[start_i] >= arr_x[i]:
                arr_right[index_right] += 1
                i += 1
                if i == n - 1:
                    break
                if arr_x[start_i] + arr_h[start_i] == arr_x[i] or arr_x[start_i] + arr_h[start_i] < arr_x[i + 1]:
                    break
            i -= 1
            flag = 1
        else:
            arr_right.append(1)
            index_right += 1
    i += 1

print(*arr_right)


arr_left = [1]
index_left = 0
flag = 0
i = n - 1
while i > 0:
    if flag:
        if arr_x[i] - arr_h[i] == arr_x[i - 1]:
            arr_left[index_left] += 1
        elif arr_x[i] - arr_h[i] < arr_x[i - 1]:
            start_i = i
            while arr_x[start_i] - arr_h[start_i] <= arr_x[i]:
                arr_left[index_left] += 1
                i -= 1
                if i == 0:
                    break
                if arr_x[start_i] - arr_h[start_i] == arr_x[i] or arr_x[start_i] - arr_h[start_i] > arr_x[i - 1]:
                    break
            i += 1
        else:
            flag = 0
            arr_left.insert(0, 1)
    else:
        if arr_x[i] - arr_h[i] == arr_x[i - 1]:
            flag = 1
            arr_left[index_left] += 1
        elif arr_x[i] - arr_h[i] < arr_x[i - 1]:
            start_i = i
            while arr_x[start_i] - arr_h[start_i] >= arr_x[i]:
                arr_left[index_left] += 1
                i -= 1
                if i == 0:
                    break
                if arr_x[start_i] - arr_h[start_i] == arr_x[i] or arr_x[start_i] - arr_h[start_i] > arr_x[i - 1]:
                    break
            i += 1
            flag = 1
        else:
            arr_left.insert(0, 1)

    i -= 1

print(*arr_left)


count = 0
while len(arr_left) > 0 or len(arr_right) > 0:
    if arr_right[0] > arr_left[0]:
        n = arr_right[0]
        arr_right.remove(n)
        while n > 0:
            if arr_left[0] - n < 0:
                n -= arr_left[0]
                arr_left.remove(arr_left[0])
            else:
                tmp = n
                n -= arr_left[0]
                arr_left[0] -= tmp
                if arr_left[0] == 0:
                    arr_left.remove(arr_left[0])
    else:
        n = arr_left[0]
        arr_left.remove(n)
        while n > 0:
            if arr_right[0] - n < 0:
                n -= arr_right[0]
                arr_right.remove(arr_right[0])
            else:
                tmp = n
                n -= arr_right[0]
                arr_right[0] -= tmp
                if arr_right[0] == 0:
                    arr_right.remove(arr_right[0])

    count += 1

print(count)