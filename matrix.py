# Курс "Программирование глубоких нейронных сетей на Python"
# Платформа "Открытое образование"
# Контрольная работа № 1 раздела № 4

import numpy as np

# Для каждого учащегося пример свой, размерность и наполнение матриц разные
# Ядра тоже!

# Матрица изображения (моя)
# 7 массивов по 10 элементов
matrix = [[ 32, 180,  21,  63, 255,  53, 164, 117, 116, 126],
          [ 49, 212,  22,  59,   5,  68, 104, 230,  97,  29],
          [ 66, 253,  16, 158,  96, 169,  86, 176, 127, 166],
          [230, 148,  36,  16, 242, 125,  49, 242, 148, 186],
          [225,  73,  91, 224,  34, 195,  24, 176, 179, 243],
          [215, 128,  50,  38, 135, 130,  18, 231, 129, 179],
          [ 56,  62,   3,  87,  68, 108,  96, 213, 228,  44]]

#Ядро свертки
kernel = [[-0.2, -0.7, 0.3],
          [ 1.0, -0.6, 0.6],
          [-0.4, -1.0, 0.6]]

def my_fun (x,y):
  """ На вход номер ячейки, на выход - значение свертки. Да, корявенько, но просто"""
  row1 = matrix[x-1][y-1]*kernel[0][0]+matrix[x-1][y]*kernel[0][1]+matrix[x-1][y+1]*kernel[0][2]
  row2 = matrix[x][y-1] * kernel[1][0]+matrix[x][y] * kernel[1][1]+matrix[x][y+1] * kernel[1][2]
  row3 = matrix[x+1][y-1]*kernel[2][0]+matrix[x+1][y]*kernel[2][1]+matrix[x+1][y+1]*kernel[2][2]
  return round(row1+row2+row3, 1)

# Итоговый массив. Пока из нулей
your_array = np.zeros((len(matrix)-2, len(matrix[0])-2))

for i in range(0,len(matrix)-2):
  for j in range (0,len(matrix[0])-2):
    your_array[i][j] = my_fun (i+1,j+1)

print("Ваша прелесть: ")
print(your_array.tolist());

# Следующая информация для тестирования в моём примере

print ('\nИсходный элемент [{}][{}] = {}'.format(5,4,matrix[5][4]))
print ('Итоговый элемент [{}][{}] = {}'.format(4,3,your_array[4][3]))

test = (-0.2*224) + (-0.7*34) + (0.3*195) + (1.0*38) + (-0.6*135) + (0.6*130) + (-0.4*87) + (-1.0*68) + (0.6*108)
test = round(test1,1)
print ('расчетное значение: ' + str(test))

#Итоговый результат (мой):
#[[-460.9, 180.0, -89.0, -136.2, -168.1, 5.3, -189.9, 24.6], [-446.2, 212.5, 49.4, 33.5, -163.6, 251.8, -268.9, -39.0], [-131.1, 135.8, -153.4, -108.9, -109.5, 203.2, -187.9, 86.9], [-87.0, 24.4, 54.2, 113.3, -363.0, 368.1, -269.8, 4.2], [16.8, 134.1, -104.0, -13.1, -145.9, 243.4, -232.1, -113.4]]

#[[-460.9, 180.0,  -89.0, -136.2, -168.1,   5.3, -189.9,   24.6],
# [-446.2, 212.5,   49.4,   33.5, -163.6, 251.8, -268.9,  -39.0],
# [-131.1, 135.8, -153.4, -108.9, -109.5, 203.2, -187.9,   86.9],
# [ -87.0,  24.4,   54.2,  113.3, -363.0, 368.1, -269.8,    4.2],
# [  16.8, 134.1, -104.0,  -13.1, -145.9, 243.4, -232.1, -113.4]]
