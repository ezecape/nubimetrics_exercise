
# coding: utf-8

# #DECISIONES TOMADAS PARA EL ANALISIS
# 1 -Buscar un listado en internet con las marcas de celular mas conocidas. REF: MercadoLibre
# 2 -Buscar en la columna 'title' si se hace referencia a una de estas marcas, entonces generar en una columna adicional 'brand' marcando estas referencias.
# la marca a la que hace referncia el titulo de la publicacion. Para los titulos que no posean ninguna de esta marca, se añade una marca 'otros'
# 3 -Se pretende que el listado de marcas tenga alrededor de 20 referencias. Para una busqueda mas exhaustiva de las posibles 
# marcas refernciadas en los titulos, analizar palabras repetidas de aquellos titulos que tengan como marca 'otros'.
# 4 -Se busca repetir el punto 3 de busqueda de nuevas marcas hasta llegar a el numero de 20 marcas diferentes. Excluyendo 'otros'. Es importante tambien que el porcentaje de ocurrencia de 'brand' = 'otros' sea menor al 10% de las publiciones.

# In[27]:


import pandas as pd


# In[28]:


cellphoneslisting = pd.read_csv('cellphoneslisting.csv',sep='\x01')


# In[29]:


def brand(title):
    if title.lower().find('samsung') != - 1 or title.lower().find('galaxy') != - 1:
        return 'samsung'
    elif title.lower().find('apple') != - 1 or title.lower().find('iphone') != - 1:
        return 'apple'
    elif title.lower().find('lg') != - 1:
        return 'lg'
    elif title.lower().find('sony') != - 1:
        return 'sony'
    elif title.lower().find('blackberry') != - 1:
        return 'blackberry'
    elif title.lower().find('alcatel') != - 1:
        return 'alcatel'
    elif title.lower().find('xiaomi') != - 1:
        return 'xiaomi'
    elif title.lower().find('alcatel') != - 1:
        return 'alcatel'
    elif title.lower().find('nokia') != - 1:
        return 'nokia'
    elif title.lower().find('huawei') != - 1:
        return 'huawei'
    #palabra clave para motorola = moto
    elif title.lower().find('moto') != - 1:
        return 'motorola'
    
    #LISTADO ENCONTRADO BUSCANDO PALABRAS REPETIDAS
    elif title.lower().find('blu') != - 1:
        return 'blu'
    elif title.lower().find('cat') != - 1:
        return 'caterpillar'
    elif title.lower().find('bgh') != - 1:
        return 'bgh'
    elif title.lower().find('tcl') != - 1:
        return 'tcl'
    elif title.lower().find('zte') != - 1:
        return 'zte'
    elif title.lower().find('hyundai') != - 1:
        return 'hyundai'
    elif title.lower().find('kodak') != - 1:
        return 'kodak'
    elif title.lower().find('quantum') != - 1:
        return 'quantum'
    elif title.lower().find('philips') != - 1:
        return 'phipils'
    elif title.lower().find('noblex') != - 1:
        return 'noblex'
    else:
        return 'otros'        


# In[30]:


cellphoneslisting["brand"]=cellphoneslisting["title"].apply(marca)


# In[31]:


#REPETIR PASOS PARA ENCONTRAR POSIBLES "BRANDS"


# In[32]:


#PASO1: Obtener todos los titulos cuya marca sera 'otros'
otros = cellphoneslisting.loc[cellphoneslisting['brand']=='otros']["title"]


# In[33]:


#PASO2: Separar las palabras de la columna title
palabras = pd.Series(' '.join(otros).lower().split())


# In[34]:


#PASO3: Identificar marcas entre las 50 palabras mas repetidas de los "title" no categorizados.
analisis_repeticiones = palabras.value_counts()[:50]
#print(analisis_repeticiones)


# In[35]:


#Listar Marcas "Otros"
#cellphoneslisting.loc[cellphoneslisting['marca']=='otros']


# In[36]:


#20 marcas mas predominantes

resultado = cellphoneslisting.groupby('brand')[['sales','unit_sales']].sum().reset_index(0).sort_values(by=['sales','unit_sales'],ascending= False)


# In[37]:


resultado.to_csv('resultado.csv',index=False)


# In[38]:


#Chequear el porcentaje de ocurrencia de cada marca en el listado.
#cellphoneslisting["brand"].value_counts(normalize=True)*100

