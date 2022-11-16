#0 a 100 en un vector decir cuales son mayores y en otro los que son menores de edad

import random
vector=[round(random.randint(10,25)) for i in range (10)]
print(vector)

edad=["mayor" if x>=18 else "menor" for x in vector]

print(edad)