def compruebaMail(mailusuario):

    """
    La función evalúa un mail recibido en busca de la @.
    Si tiene una @ es correcto
    Si tiene mas de una @ es incorrecto
    Si el @ esta al final lo manda a freir monos

    >>> compruebaMail('palominosr@hotmail.com')
    True
    >>> compruebaMail('palominosr.hotmail.com')
    False
    >>> compruebaMail('palominosr@')
    False
    >>> compruebaMail('palominosr@hotmail@.com')
    False

    """
    arroba=mailusuario.count(@)
        if (arroba!=1 or mailusuario.rfind('@')==len(mailusuario-1) or mailusuario.find('@')==0):
                return False
        else:
                return True




    import doctest
    doctest.testmod()
