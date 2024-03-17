# 1) синхронный метод

import random
import  time

start_time = time.time()
random_numbers = [random.randint(1, 100) for _ in range(1_000_000)]
# проверка на массиве из 1000 элементов. Сумма 49779
# random_numbers = [64, 95, 88, 61, 31, 57, 87, 31, 67, 2, 12, 66, 99, 39, 37, 29, 57, 78, 89, 44, 36, 86, 53, 90, 84, 30, 47, 10, 100, 45, 14, 48, 92, 8, 36, 55, 58, 66, 68, 6, 15, 14, 52, 20, 77, 28, 91, 50, 7, 4, 1, 51, 19, 35, 51, 100, 69, 77, 18, 97, 9, 41, 94, 37, 4, 65, 53, 2, 100, 19, 93, 47, 96, 27, 80, 86, 32, 100, 85, 96, 13, 77, 83, 58, 69, 30, 21, 62, 100, 43, 55, 2, 62, 21, 96, 88, 77, 42, 87, 6, 75, 42, 4, 57, 12, 83, 40, 53, 42, 1, 92, 30, 28, 45, 32, 52, 70, 71, 57, 84, 86, 93, 63, 32, 74, 85, 99, 89, 32, 96, 47, 32, 68, 31, 32, 26, 18, 12, 17, 59, 64, 48, 71, 19, 44, 8, 85, 2, 91, 16, 11, 5, 64, 81, 7, 89, 35, 74, 47, 9, 77, 97, 4, 96, 85, 7, 73, 50, 80, 43, 31, 88, 9, 81, 6, 28, 20, 58, 63, 40, 29, 94, 68, 44, 4, 48, 82, 19, 64, 13, 78, 60, 2, 32, 71, 70, 32, 60, 29, 73, 49, 27, 21, 20, 6, 21, 37, 89, 11, 15, 77, 84, 6, 41, 22, 11, 49, 96, 4, 57, 46, 24, 8, 35, 30, 100, 44, 2, 32, 12, 11, 85, 11, 20, 56, 46, 69, 93, 67, 97, 32, 58, 93, 55, 52, 94, 68, 9, 42, 30, 60, 25, 87, 43, 18, 93, 27, 24, 93, 52, 13, 62, 70, 75, 36, 82, 60, 56, 22, 17, 70, 70, 59, 4, 80, 89, 28, 21, 51, 40, 69, 59, 100, 23, 13, 26, 98, 73, 20, 100, 13, 50, 18, 99, 90, 32, 2, 28, 47, 89, 5, 7, 41, 32, 9, 47, 7, 21, 73, 66, 19, 92, 20, 36, 77, 1, 27, 74, 73, 96, 50, 24, 84, 42, 93, 50, 97, 62, 73, 41, 34, 88, 43, 51, 12, 63, 33, 22, 65, 46, 82, 25, 45, 4, 50, 86, 89, 81, 25, 34, 32, 26, 16, 75, 48, 78, 44, 84, 8, 21, 18, 15, 44, 7, 5, 35, 56, 56, 26, 83, 53, 58, 89, 63, 82, 35, 93, 9, 27, 42, 63, 4, 24, 94, 5, 58, 14, 40, 42, 39, 96, 89, 20, 98, 24, 20, 30, 48, 90, 37, 78, 52, 13, 36, 61, 68, 97, 54, 57, 6, 69, 98, 97, 100, 9, 11, 32, 18, 66, 86, 44, 25, 78, 30, 24, 9, 76, 40, 30, 72, 22, 4, 56, 30, 71, 95, 19, 12, 74, 51, 11, 91, 52, 5, 86, 93, 94, 49, 63, 32, 74, 59, 37, 54, 51, 21, 43, 97, 56, 56, 65, 82, 1, 28, 42, 51, 93, 8, 97, 58, 34, 5, 26, 48, 50, 56, 60, 41, 43, 87, 12, 41, 92, 43, 36, 85, 91, 80, 85, 90, 32, 75, 4, 20, 5, 42, 51, 4, 2, 29, 34, 72, 70, 32, 12, 84, 87, 58, 61, 19, 82, 25, 92, 78, 69, 81, 24, 49, 30, 97, 88, 48, 51, 27, 23, 95, 52, 60, 78, 39, 63, 95, 9, 71, 89, 75, 70, 46, 12, 42, 94, 52, 48, 20, 42, 89, 86, 70, 81, 7, 14, 13, 95, 78, 23, 35, 25, 32, 40, 24, 13, 13, 83, 89, 99, 81, 53, 31, 76, 97, 15, 65, 43, 28, 24, 8, 26, 48, 15, 26, 71, 69, 76, 58, 49, 87, 30, 77, 21, 80, 83, 49, 78, 5, 37, 69, 94, 39, 64, 4, 74, 14, 50, 46, 62, 6, 12, 97, 23, 100, 67, 43, 49, 89, 24, 36, 96, 32, 87, 38, 69, 24, 5, 27, 68, 29, 39, 16, 19, 11, 86, 5, 56, 81, 76, 13, 82, 26, 91, 87, 11, 49, 10, 54, 70, 77, 15, 100, 30, 12, 84, 6, 7, 41, 41, 96, 51, 97, 39, 83, 62, 13, 69, 92, 67, 45, 87, 48, 6, 72, 61, 75, 76, 18, 60, 46, 67, 24, 93, 88, 11, 11, 46, 50, 78, 54, 8, 65, 9, 17, 19, 80, 79, 41, 62, 67, 25, 6, 54, 39, 22, 64, 97, 85, 47, 29, 16, 99, 44, 66, 42, 81, 53, 35, 31, 88, 34, 6, 93, 78, 61, 14, 82, 6, 9, 49, 48, 32, 68, 65, 14, 33, 7, 94, 28, 39, 49, 2, 30, 76, 18, 11, 49, 26, 18, 53, 24, 54, 14, 54, 24, 72, 79, 52, 21, 27, 79, 3, 7, 28, 37, 82, 43, 99, 17, 100, 13, 94, 28, 15, 3, 56, 43, 77, 22, 77, 38, 67, 30, 34, 49, 31, 29, 55, 15, 74, 95, 3, 42, 3, 25, 100, 79, 41, 7, 80, 32, 15, 61, 38, 33, 21, 83, 98, 76, 99, 99, 20, 34, 18, 94, 47, 64, 56, 66, 5, 88, 28, 96, 10, 5, 5, 96, 55, 69, 90, 70, 96, 66, 96, 84, 29, 94, 9, 44, 63, 68, 10, 2, 14, 32, 10, 42, 80, 9, 27, 46, 85, 94, 47, 97, 51, 17, 85, 82, 85, 60, 41, 38, 64, 12, 80, 15, 13, 62, 54, 33, 92, 69, 70, 98, 82, 44, 97, 9, 71, 39, 100, 62, 97, 78, 28, 37, 41, 48, 52, 36, 18, 72, 71, 60, 89, 71, 15, 40, 41, 42, 6, 57, 90, 9, 22, 92, 15, 41, 44, 46, 1, 64, 86, 1, 2, 22, 67, 89, 22, 68, 70, 28, 64, 36, 84, 81, 89, 92, 37, 41, 48, 20, 5, 57, 9, 72, 70, 30, 84, 37, 76, 21, 88, 67, 48, 44, 12, 30, 99, 71, 59, 41, 88, 42, 96, 34, 57, 61, 95, 16, 4, 44, 22, 67, 46, 23, 76, 21, 50, 50, 17, 77, 46, 59, 32, 73, 77, 14, 33, 44, 96, 40, 18, 45, 6, 80, 3, 71, 33, 11, 61, 94, 95, 21, 40, 44, 91, 44, 51, 100, 67, 35, 13]

# print("Случайные числа:", random_numbers)
print("Сумма элементов:", sum(random_numbers))
print("Время выполнения:", time.time() - start_time, "секунд")




