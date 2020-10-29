class Refrigerator:
    def __init__(self, firm, capacity, weight, powerConsumption):
        self.firm = str(firm)
        self.capacity = float(capacity)
        self.weight = float(weight)
        self.powerConsumption = float(powerConsumption)

refrigerator1 = Refrigerator("LG", 14.12, 250.0, 50.0)
refrigerator2 = Refrigerator("Samsung", 15.13, 200.97, 28.16)
refrigerator3 = Refrigerator("Libher", 13.67, 300.54, 97.54)
refrigerator4 = Refrigerator("Gorenja", 16.09, 100.30, 54.6)
refrigerator5 = Refrigerator("Libher", 9.47, 400.20, 96.15)
refrigerator6 = Refrigerator("LG", 30.86, 700.60, 75.98)
refrigerator7 = Refrigerator("Samsung", 18.09, 10.60, 17.3)
refrigerator8 = Refrigerator("Gorenja", 28.18, 600.50, 85.98)

refrigertorCapacity = [
    refrigerator1.capacity,
    refrigerator2.capacity,
    refrigerator3.capacity,
    refrigerator4.capacity,
    refrigerator5.capacity,
    refrigerator6.capacity,
    refrigerator7.capacity,
    refrigerator8.capacity
]

refrigeratorPowerConsumption = [
    refrigerator1.powerConsumption,
    refrigerator2.powerConsumption,
    refrigerator3.powerConsumption,
    refrigerator4.powerConsumption,
    refrigerator5.powerConsumption,
    refrigerator6.powerConsumption,
    refrigerator7.powerConsumption,
    refrigerator8.powerConsumption
]


def insertionSort(Arr):
    for i in range(len(Arr)):
        j = i - 1
        key = Arr[i]
        while Arr[j] < key and j >= 0:
            Arr[j + 1] = Arr[j]
            j -= 1
        Arr[j + 1] = key
    return Arr


def heapify(arr, n, i):
	largest = i
	left = 2 * i + 1
	right = 2 * i + 2

	if left < n and arr[i] < arr[left]:
		largest = left
	if right < n and arr[largest] < arr[right]:
		largest = right
	if largest != i:
		arr[i],arr[largest] = arr[largest],arr[i]
		heapify(arr, n, largest)

def heapSort(arr):
	n = len(arr)
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)

insertionSort(refrigertorCapacity)
heapSort(refrigeratorPowerConsumption)
print("Refrigerators sorted by capacity descending")
print(refrigertorCapacity)
print()
print("refrigerators sorted by power consumption")
print(refrigeratorPowerConsumption)

