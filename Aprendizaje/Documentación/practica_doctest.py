def areaTriangulo(base,altura):

    """
     Esta funcion calcula el área de un triángulo dado

     >>> areaTriangulo(4,8)
     16.0

    """

    return ((base*altura)/2)

#print(areaTriangulo(4,8))

import doctest

doctest.testmod()
