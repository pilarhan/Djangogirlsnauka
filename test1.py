def BMI(wzrost,waga):
	bmi = waga / (wzrost ** 2)
	print("Twoje bmi wynosi:",bmi)
wzrost = input('podaj wzrost: ')
waga = input('podaj waga: ')
wz=float(wzrost)
wg=int(waga)
BMI(wz,wg)

