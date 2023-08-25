''' Escriba un programa que devuelva la siguiente salida:
      *
     ***
    *****
   *******
  *********
 ***********
'''

z = 7
x = 1
while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x+=2
    z-=1
