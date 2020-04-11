vector_recibido=[1,2,3,4,5,6]
vector1=[]
vector2=[]
x=len(vector1)
if len(vector_recibido)==0:
    vector1=[]
    vector2=[]
elif    len(vector_recibido)%2 == 0:
    indice=len(vector_recibido)/2
    vector1=vector_recibido[0:int(indice)]
    vector2=vector_recibido[int(indice):int(len(vector_recibido))]

elif  len(vector_recibido)%2 != 0:
    indice=int(len(vector_recibido)/2)
    vector1=vector_recibido[0:int(indice+1)]
    vector2=vector_recibido[int(indice)+1:int(len(vector_recibido))]

resultado=(vector1,vector2)
print(resultado)
