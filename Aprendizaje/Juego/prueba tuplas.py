def easy_unpack(tuplap):
    tupla=tuplap
    print(tupla)
    tuple1 = (tupla[0], tupla[2], tupla[(len(tupla)-3)])
    print(tuple1)

easy_unpack((1, 2, 3, 4, 5, 6, 7, 9))
