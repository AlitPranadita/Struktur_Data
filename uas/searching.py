def binary_search_rekursif(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rekursif(arr, target, mid + 1, high)
    else:
        return binary_search_rekursif(arr, target, low, mid - 1)


# Input data dari pengguna
data = input("Masukkan elemen-elemen data (pisahkan dengan spasi): ").split()
data = [int(x) for x in data]
target = int(input("Masukkan elemen yang ingin dicari: "))

# Mengurutkan data secara ascending
data.sort()

# Melakukan binary search rekursif pada data
result = binary_search_rekursif(data, target, 0, len(data) - 1)

# Menampilkan hasil pencarian
if result != -1:
    print("Elemen ditemukan pada indeks:", result)
else:
    print("Elemen tidak ditemukan dalam data.")