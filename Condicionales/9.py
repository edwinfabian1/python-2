"""Solicite una fecha al usuario. en formato día, mes y año. Dígale cuanto tiempo 
ha pasado desde esa fecha hasta hoy o cuanto falta para llegar a esa fecha si es 
posterior"""

from datetime import date
year = date.today().year
month = date.today().month
day = date.today().day

dia = int(input("ingrese dia: "))
mes = int(input("ingrese mes: "))
año = int(input("ingrese año: "))


"""if año < year:
    if mes < month:
        
if año > year:
    
if año == year:
    """