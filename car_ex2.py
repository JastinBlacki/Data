# Технический осмотр автомобиля осуществляется каждые 5 000
# километров. Условный срок «жизни» двигателя 200 000 километров. Каждые
# 5 000 километров требуется замена масла. Каждые 10 000 километров
# требуется замена колодок и тормозной жидкости. Каждые 20 000 требуется
# замена ремней и свечей зажигания. Составьте алгоритм вывода сообщений
# для автомобиля с пробегом от 20 км до 200 000 км.

i = 20
while(i <= 200000):
    if((i - 20) % 5000 == 0):
        print("Требуется замена масла")
    if((i - 20) % 10000 == 0):
        print("Требуется замена колодок и тормозной жидкости")
    if((i - 20) % 20000 == 0):
        print("Требуется замена ремней и свечей зажигания")
    i += 1
