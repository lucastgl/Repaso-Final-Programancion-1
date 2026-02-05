# Sincronización de Inventarios de Sucursales (Archivos y Conjuntos)

# Contexto: Una empresa fusiona dos depósitos y necesita un inventario único sin duplicados inconsistentes.

# 1. Fusión de Archivos: Leer deposito_norte.txt y deposito_sur.txt (formato CSV: SKU;Nombre;Stock). 
# Los archivos están ordenados por SKU. Ambos usan codificación UTF8.

# 2. Lógica de Inconsistencias:
#     ◦ Si un mismo SKU aparece en ambos archivos con nombres diferentes, es una inconsistencia: mostrar por 
#       pantalla y no grabar en el archivo final.
#     ◦ Si el SKU es el mismo y el nombre coincide, sumar los stocks para el archivo de salida.

# 3. Uso de Conjuntos: Utilizar conjuntos (sets) para identificar rápidamente qué SKUs son exclusivos de cada 
# depósito y cuáles están duplicados.

# 4. Salida Prolija: El archivo resultante inventario_total.txt debe mantener el orden por SKU y 
# tener el formato SKU - NOMBRE - TOTAL con el nombre del producto en mayúsculas.

# 5. Cierre Seguro: Implementar el cierre de los tres archivos (dos de lectura, uno de escritura) 
# dentro de un bloque finally, asegurando que los recursos se liberen aunque ocurra un error de lectura
#------------------------------------------------------------------------------------------------------------
