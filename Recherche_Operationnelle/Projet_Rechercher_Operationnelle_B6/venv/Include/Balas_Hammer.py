from Include import Structure_Arbre as arbre;

class Balas_Hammer:

    """
    :param:
        matrice - La matrice qui contient les coûts de transport, les provisions ainsi que les commandes
        res - (Param modifié)La matrice qui le nombre de marchandise qui va être transporter du fournisseur i au client j
            (La proposition initiale sans faire l'optimisation)
        nombre - Le nombre de transport traité
        arret - La condition d'arrêt: Lors que le nombre de transport traité atteint à la totalité de transports
    """
    def proposition_initiale(matrice:list, res:list, nombre, arret,matrice_fournisseur:list,matrice_client:list):

        if nombre >= arret:
            return

        temp = []
        max_val_column = 0
        column = 0

        #vertical
        for index in range(0,len(matrice[0])-1):

            for each in matrice[:-1]:

                if each[index] == 0:
                    continue

                else:
                    temp.append(each[index])

            temp.sort()

            if len(temp) == 1 and max_val_column < temp[0]:

                max_val_column = temp[0]
                column = index

            elif len(temp) > 1 and max_val_column < temp[1] - temp[0]:

                max_val_column = temp[1] - temp[0]
                column = index

            temp.clear()

        #horizontal
        max_val_row=0
        row = 0

        for index in range(0,len(matrice)-1):
            for each in matrice[index][:-1]:
                if each == 0:
                    continue
                else:
                    temp.append(each)

            temp.sort()

            if len(temp) == 1 and max_val_row < temp[0]:

                max_val_row= temp[0]
                row = index

            elif len(temp) > 1 and max_val_row < temp[1]-temp[0]:

                max_val_row = temp[1] - temp[0]
                row = index;

            temp.clear()


        if max_val_row > max_val_column:
            print("La ligne "+str((row+1))+": Pénalité maximale: " + str(max_val_row))
            min_val = matrice[row][0]
            position = 0

            for index in range(1,len(matrice[row])-1):

                if min_val == 0 :

                    min_val = matrice[row][index]
                    position = index

                elif (matrice[row][index] != 0 and min_val > matrice[row][index]):

                    min_val = matrice[row][index]
                    position = index

            if(matrice[row][-1] < matrice[-1][position]):

                res[row][position] = matrice[row][-1]
                matrice[row][position] = 0
                nombre += 1
                matrice[-1][position] -= matrice[row][-1]
                matrice[row][-1] = 0

                for i in range(0,len(matrice[row])-1):

                    if(matrice[row][i] == 0):
                        continue

                    if i == position:
                        continue

                    else:
                        res[row][i] = 0
                        matrice[row][i] = 0
                        nombre += 1

                return Balas_Hammer.proposition_initiale(matrice,res,nombre,arret,matrice_fournisseur,matrice_client)
            else:

                res[row][position] = matrice[-1][position]
                matrice[row][position] = 0
                nombre += 1
                matrice[row][-1] -= matrice[-1][position]
                matrice[-1][position] = 0

                for i in range(0,len(matrice)-1):

                    if matrice[i][position] == 0:
                        continue
                    if i == position:
                        continue
                    else:
                        res[i][position] = 0
                        matrice[i][position] = 0
                        nombre += 1


                return Balas_Hammer.proposition_initiale(matrice,res, nombre, arret,matrice_fournisseur,matrice_client)

        else:
            print("La colonne" + str((column+ 1)) + ": Pénalité maximale:" + str(max_val_column))
            min_val = matrice[0][column]
            position = 0

            for index in range(1, len(matrice) - 1):

                if min_val == 0:
                    min_val = matrice[index][column]
                    position = index
                elif (matrice[index][column] != 0 and min_val > matrice[index][column]):
                    min_val = matrice[index][column]
                    position = index

            if (matrice[position][-1] < matrice[-1][column]):

                res[position][column] = matrice[position][-1]
                matrice[position][column] = 0
                nombre += 1
                matrice[-1][column] -= matrice[position][-1]
                matrice[position][-1] = 0

                for i in range(0, len(matrice[position]) - 1):

                    if matrice[position][i] == 0:
                        continue

                    if i == column:
                        matrice[position][i] = 0
                        continue
                    else:
                        res[position][i] = 0
                        matrice[position][i] = 0
                        nombre += 1

                return Balas_Hammer.proposition_initiale(matrice,res, nombre, arret,matrice_fournisseur,matrice_client)

            else:

                res[position][column] = matrice[-1][column]
                matrice[position][column] = 0
                nombre += 1
                matrice[position][-1] -= matrice[-1][column]
                matrice[-1][column] = 0
                for i in range(0, len(matrice) - 1):

                    if matrice[i][column] == 0:
                        continue

                    if i == position:

                        continue

                    else:
                        res[i][column] = 0
                        matrice[i][column] = 0
                        nombre += 1

                return Balas_Hammer.proposition_initiale(matrice,res,nombre, arret,matrice_fournisseur,matrice_client)




    """
       :param:
       matrice_cout : La matrice contient tous les coûts des transports
       matrice_transport: La matrice contient toutes les propositions de transport entre le fournisseur et le client
       
       :desc:
       Le coût et la proposition pour chaque arête a le même index, ainsi il suffit de parcourir les deux matrices simultanément en
       calculant la somme de leur produit. 
       
       :return:
       Le coût total de la proposition de transport
    """
    def calculerCoutTotal(matrice_cout:list, matrice_transport:list):

        cout_total = 0

        for index, each in enumerate(matrice_cout[:-1]):
            for num, element in enumerate(each[:-1]):

                cout_total += matrice_cout[index][num] * matrice_transport[index][num]

        return cout_total


    """
        :param:
            -matrice: La matrice qui contient l'ensemble de la proposition de transport
    """
    def choisirAreteAjoute(self,matrice:list,matrice_prix:list,matrice_fournisseur:list,matrice_client:list,ensemble_prec:list):

        new_arbre = arbre.arbreTransport()
        nombre_arete = 0;
        nombre_sommet = (len(matrice) - 1) + (len(matrice[0]) - 1);
        ensemble_ajout = []
        isExist = False;

        for index,each in enumerate(matrice[0:-1]):
            for num,ele in enumerate(each[0:-1]):
                if ele != 0:
                    new_arbre.add_arete(arbre.Localisation(matrice_fournisseur[index],0),arbre.Localisation(matrice_client[num],0));

        result = new_arbre.hasCycle()
        if not result[0]:
            arete_ajouter = [];
            arete_ajouter_index = []
            minVal=-1;
            res = new_arbre.verifierConnectivite();
            print("\nLes sous-graphes sont:" + str(res[1]))
            while(len(res[1]) > 1) :
                for num,each in enumerate(res[1]):
                    for ele in each:
                        if ele.find("P") != -1:
                            count = 0;
                            while(count < len(res[1])):

                                if count == num:
                                    count += 1;
                                    continue;
                                for i in res[1][count]:
                                    if i.find("C") != -1:

                                        for arete in ensemble_prec:

                                            if i in arete and ele in arete:
                                                isExist = True
                                                break

                                        if isExist:
                                            isExist = False
                                            continue

                                        if minVal == -1:
                                            minVal = matrice_prix[matrice_fournisseur.index(ele)][matrice_client.index(i)];
                                            arete_ajouter = [ele,i]
                                            arete_ajouter_index = [num,count]
                                        else:
                                            if minVal > matrice_prix[matrice_fournisseur.index(ele)][matrice_client.index(i)]:
                                                minVal = matrice_prix[matrice_fournisseur.index(ele)][matrice_client.index(i)];
                                                arete_ajouter = [ele, i]
                                                arete_ajouter_index = [num, count]
                                count += 1;

                new_arbre.localisations[arete_ajouter[0]].connections.append(new_arbre.localisations[arete_ajouter[1]]);
                new_arbre.localisations[arete_ajouter[1]].connections.append(new_arbre.localisations[arete_ajouter[0]]);
                res[1][arete_ajouter_index[0]] = res[1][arete_ajouter_index[0]].union(res[1][arete_ajouter_index[1]])
                res[1].pop(arete_ajouter_index[1])
                minVal = -1;
                print("L'arête ajoutée pour complèter la connexité" + str(arete_ajouter))
                ensemble_ajout.append(arete_ajouter);

        else:
            arbre_nodes.remove_cycle(result[1], matrice_fournisseur, matrice_client, matrice);

            arete_ajouter = [];
            arete_ajouter_index = []
            minVal = -1;
            res = new_arbre.verifierConnectivite();
            while (len(res[1]) > 1):
                for num, each in enumerate(res[1]):
                    for ele in each:
                        if ele.find("P") != -1:
                            count = 0;
                            while (count < len(res[1])):
                                if count == num:
                                    count += 1;
                                    continue;
                                for i in res[1][count]:
                                    if i.find("C") != -1:
                                        if minVal == -1:
                                            minVal = matrice_prix[matrice_fournisseur.index(ele)][
                                                matrice_client.index(i)];
                                            arete_ajouter = [ele, i]
                                            arete_ajouter_index = [num, count]
                                        else:
                                            if minVal > matrice_prix[matrice_fournisseur.index(ele)][
                                                matrice_client.index(i)]:
                                                minVal = matrice_prix[matrice_fournisseur.index(ele)][
                                                    matrice_client.index(i)];
                                                arete_ajouter = [ele, i]
                                                arete_ajouter_index = [num, count]
                                count += 1;

                new_arbre.localisations[arete_ajouter[0]].connections.append(new_arbre.localisations[arete_ajouter[1]]);
                new_arbre.localisations[arete_ajouter[1]].connections.append(new_arbre.localisations[arete_ajouter[0]]);
                res[1][arete_ajouter_index[0]] = res[1][arete_ajouter_index[0]].union(res[1][arete_ajouter_index[1]])
                res[1].pop(arete_ajouter_index[1])
                minVal = -1;
                print("L'arête ajoutée pour complèter la connexité" + str(arete_ajouter))
                ensemble_ajout.append(arete_ajouter);
        return new_arbre,ensemble_ajout;


    def calculValueNode(self,matrice_prix:list, arbre_nodes:arbre.arbreTransport, matrice_fournisseur:list,matrice_client:list,count):

            visited = set();

            def setValue(node,count):

                visited.add(node)

                for each in node.connections:
                    if count == 0:
                        node.demande = matrice_prix[matrice_fournisseur.index(node.nom)][matrice_client.index(each.nom)]
                        print(node.nom+" -> " + str(node.demande))
                        print(each.nom + " -> " + str(each.demande))
                        count += 1
                        setValue(each,count+1)

                    elif each not in visited:

                        if each.nom.find("P") == -1:
                            each.demande = node.demande - matrice_prix[matrice_fournisseur.index(node.nom)][matrice_client.index(each.nom)]
                            print(each.nom+" -> " + str(each.demande))
                            setValue(each,count+1)
                        elif each.nom.find("C") == -1:
                            each.demande = node.demande + matrice_prix[matrice_fournisseur.index(each.nom)][matrice_client.index(node.nom)]
                            print(each.nom+" -> " + str(each.demande))
                            setValue(each,count+1)

                    elif len(visited) >= len(arbre_nodes.localisations):

                        return;


            first_node = next(iter(arbre_nodes.localisations.values()))
            setValue(first_node,count)
            return;



    def calculPotentiel(self,matrice_prix:list, arbre_nodes:arbre.arbreTransport, matrice_fournisseur:list,matrice_client:list):

        for index_f,each_f in enumerate(matrice_fournisseur[0:-1]):
            for index_c,each_c in enumerate(matrice_client[0:-1]):
                matrice_prix[index_f][index_c] = arbre_nodes.localisations[each_f].demande - arbre_nodes.localisations[each_c].demande;


    def calculMarginaux(self,matrice_prix:list,matrice_potetiel:list):

        matrice_marginaux = []

        for index_colum,each_colum in enumerate(matrice_potetiel):

            if index_colum == len(matrice_potetiel)-1:
                matrice_marginaux.append(matrice_potetiel[index_colum])
            else:
                row = []
                for index_row,each_row in enumerate(each_colum):

                    if index_row == len(each_colum)-1:
                        row.append(matrice_potetiel[index_colum][index_row])
                    else:
                        row.append(matrice_prix[index_colum][index_row] - matrice_potetiel[index_colum][index_row])

                matrice_marginaux.append(row)

        return matrice_marginaux;

    def detecterValNegative(self,matrice_marginaux:list,arbre_nodes:arbre.arbreTransport,matrice:list,matrice_fournisseur:list,matrice_client:list):

        arete_ajouter = []
        minVal = 0
        has_negative = False

        for index_colum,each_colum in enumerate(matrice_marginaux[0:-1]):
            for index_row,each_row in enumerate(each_colum[0:-1]):
                if each_row < 0 and each_row < minVal:
                    arete_ajouter.clear()
                    arete_ajouter.append(matrice_fournisseur[index_colum])
                    arete_ajouter.append(matrice_client[index_row])
                    has_negative = True

        if has_negative:
            #rajouter l'arête negative
            arbre_nodes.localisations[arete_ajouter[0]].connections.append(arbre_nodes.localisations[arete_ajouter[1]])
            arbre_nodes.localisations[arete_ajouter[1]].connections.append(arbre_nodes.localisations[arete_ajouter[0]])

            #detecter le circuit
            result = arbre_nodes.hasCycle_fin(arete_ajouter[0])
            if result[0]:
                print("\nL'arête à rajouter: " + str(arete_ajouter)+" et elle forme un circuit: ")
                print("Le circuit: " + str(result[1]))
                arbre_nodes.remove_cycle(result[1], matrice_fournisseur, matrice_client, matrice);
                return True,arete_ajouter;
        else:
            return False,None;