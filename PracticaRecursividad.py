def esPalindromo(palabra):
    if len(palabra) <= 1:
        return True
    print(f"Verificando: {palabra}")
    print(f"Comparando: {palabra[0]} == {palabra[-1]}")
    if palabra[0] != palabra[-1]:
        print(f"{palabra[0]} != {palabra[-1]}, no es palíndromo")
        return False
    return esPalindromo(palabra[1:-1])


print(esPalindromo("radar"))  # True
print(esPalindromo("python"))  # False