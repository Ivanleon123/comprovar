def comprovar_rima(palabra1, palabra2):
    """Comprova si dues paraules rimen o no."""
    # Obtenir les dues últimes lletres i les tres últimes lletres
    rima_3 = palabra1[-3:] == palabra2[-3:]
    rima_2 = palabra1[-2:] == palabra2[-2:]

    if rima_3:
        return "Les paraules rimen!"
    elif rima_2:
        return "Les paraules rimen un poc!"
    else:
        return "Les paraules NO rimen."

def main():
    # Demanar dues paraules a l'usuari
    paraula1 = input("Introdueix la primera paraula: ")
    paraula2 = input("Introdueix la segona paraula: ")

    # Comprovar si rimen
    resultat = comprovar_rima(paraula1, paraula2)
    print(resultat)

# Executar el programa
if __name__ == "__main__":
    main()
