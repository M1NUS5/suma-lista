def suma_lista(lista):
    """
    Calcula la suma de todos los elementos de una lista.

    Parámetros:
        lista (list): Lista de números.

    Retorna:
        int o float: Suma de los elementos.

    Excepciones:
        TypeError: Si la entrada no es una lista.
        ValueError: Si la lista está vacía.
        TypeError: Si algún elemento no es numérico.
    """

    if not isinstance(lista, list):
        raise TypeError("La entrada debe ser una lista.")

    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")

    for elemento in lista:
        if not isinstance(elemento, (int, float)):
            raise TypeError("Todos los elementos deben ser números.")

    return sum(lista)