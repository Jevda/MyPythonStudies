consume = 0 # Rashod na 100km
distance = 0 # Distancija
price = 0 # Cena
totalConsume = 0 # Vsego litrov na poezdku
totalPrice = 0 # Obshaja cena topliva

consume = float(input("Введите расход топлива на 100КМ"))
distance = float(input("Введите растояние"))
price = float(input("Введите цену топлива за литр"))

totalConsume = distance / 100 * consume
totalPrice = totalConsume * price

print("Vsego potracheno topliva: ", int(totalConsume*100) / 100, "L")
print("Stoimostj topliva: ", int(totalPrice*100) / 100, "EUR")