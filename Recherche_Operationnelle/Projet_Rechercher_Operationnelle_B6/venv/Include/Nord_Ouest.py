import copy

"""
:param:
    matrice - La matrice qui contient les coûts de transport, les provisions ainsi que les commandes

:return:
    res - La matrice qui le nombre de marchandise qui va être transporter du fournisseur i au client j
"""
def nord_ouest(matrice:list):

    nombre = 0
    arret = (len(matrice[0])-1) * (len(matrice)-1)
    index_row = 0
    index_provision = len(matrice[0])-1
    index_column = 0
    index_commande = len(matrice)-1
    res = copy.deepcopy(matrice)

    while(nombre < arret):

        if(matrice[index_row][index_provision]) <= matrice[index_commande][index_column]:

            res[index_row][index_column] = matrice[index_row][index_provision]
            matrice[index_commande][index_column] -= matrice[index_row][index_provision]
            matrice[index_row][index_provision] = 0
            nombre += 1

            for each in range(index_column+1,len(matrice[0])-1):

                res[index_row][each] = 0
                nombre += 1

            index_row += 1

        else:

            res[index_row][index_column] = matrice[index_commande][index_column]
            matrice[index_row][index_provision] -= matrice[index_commande][index_column]
            matrice[index_commande][index_column] = 0
            nombre += 1

            for each in range(index_row+1,len(matrice)-1):

                res[each][index_column] = 0
                nombre += 1

            index_column += 1

    return res