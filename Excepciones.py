"""
Excepciones
"""

try:
    #print(10/0)
    print([1,2,3,4][4])
except Exception as error:
    print(f"Se ha producido un error: {error}")