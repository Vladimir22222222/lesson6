n = int(input("Введите количество чисел "))
zero = 0
for i in range(1, n+1):
	s = int(input("введите целое число "))
	if s == 0:
				zero += 1
print(zero)