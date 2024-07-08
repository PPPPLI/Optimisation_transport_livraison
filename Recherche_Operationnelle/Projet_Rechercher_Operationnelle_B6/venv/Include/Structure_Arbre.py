class Localisation:
    def __init__(self,nom,demande):
        self.nom = nom;
        self.demande = demande;
        self.connections = [];


class arbreTransport:

    def __init__(self):

        self.localisations = {};

    def add_arete(self,localisationA,localisationB):

        if localisationA.nom not in self.localisations:
            self.localisations[localisationA.nom] = localisationA
        if localisationB.nom not in self.localisations:
            self.localisations[localisationB.nom] = localisationB

        self.localisations[localisationA.nom].connections.append(self.localisations[localisationB.nom]);
        self.localisations[localisationB.nom].connections.append(self.localisations[localisationA.nom]);


    def verifierConnectivite(self):

        sousArbres = []
        #Parcours en largeur
        def dfs(node):
            visited.add(node.nom);
            for childNode in node.connections:
                if childNode.nom not in visited:
                    dfs(childNode);

        start_node = iter(self.localisations.values())
        while(True):
            mark = False
            visited = set();
            node = next(start_node,-2)
            if node == -2:
                break;
            dfs(node);
            if len(sousArbres) <= 0:
                sousArbres.append(visited);
            else:
                for each in sousArbres:
                    if(len(each.intersection(visited)) != 0):
                        mark = True

                if(mark == False):
                    sousArbres.append(visited);
                    mark = False;

        return len(sousArbres) == 1, sousArbres;



    def hasCycle(self):

        visited = set();
        trace = []
        def detectionCycle(node,parent,starter,path):
            visited.add(node.nom);
            for childNode in node.connections:

                if len(node.connections) == 1 and childNode.nom in visited:
                    return False

                if parent == None:

                    result = detectionCycle(childNode,node,starter,path+1)
                    if result:
                        trace.append(node.nom);
                        return True
                    else:continue

                if childNode.nom != parent.nom and childNode.nom not in visited:
                    result = detectionCycle(childNode,node,starter,path+1)
                    if result:
                        trace.append(node.nom)
                        return True;
                    else:continue;

                elif childNode.nom == starter.nom and path > 1:
                    trace.extend([starter.nom,node.nom])
                    return True
            return False;

        next_node = iter(self.localisations.values())
        while(True):


            start_node = next(next_node,-2);
            if start_node == -2:
                return False,trace;

            res = detectionCycle(start_node,None,start_node,0)
            if not res:
                visited.clear();
                continue;
            else:
                return res,trace;


    def is_degenerate(self,matrice:list):

        # Vérifier si tous les degrés sont <= 2
        for node in self.locations.values():
            if len(node.connections) > 2:
                return False
        return True


    def remove_cycle(self,circuit:list,matrice_fournisseur:list,matrice_client:list,matrice:list):

        minVal = -1

        for index,each in  enumerate(circuit[0:-1]):

            if index % 2 != 0:
                if minVal == -1:
                    minVal = matrice[matrice_fournisseur.index(circuit[index+1])][matrice_client.index(circuit[index])]
                else:
                    if minVal > matrice[matrice_fournisseur.index(circuit[index+1])][matrice_client.index(circuit[index])]:
                        minVal = matrice[matrice_fournisseur.index(circuit[index + 1])][matrice_client.index(circuit[index])]


        for index,each in  enumerate(circuit[0:-1]):

            if index % 2 != 0:

                matrice[matrice_fournisseur.index(circuit[index+1])][matrice_client.index(circuit[index])] -= minVal;

            else:
                matrice[matrice_fournisseur.index(circuit[index])][matrice_client.index(circuit[index+1])] += minVal;


    def hasCycle_fin(self,node_ajout):

        visited = set();
        trace = []
        def detectionCycle(node,parent,starter,path):
            visited.add(node.nom);
            for childNode in node.connections:

                if len(node.connections) == 1 and childNode.nom in visited:
                    return False

                if parent == None:

                    result = detectionCycle(childNode,node,starter,path+1)
                    if result:
                        trace.append(node.nom);
                        return True
                    else:continue

                if childNode.nom != parent.nom and childNode.nom not in visited:
                    result = detectionCycle(childNode,node,starter,path+1)
                    if result:
                        trace.append(node.nom)
                        return True;
                    else:continue;

                elif childNode.nom == starter.nom and path > 1:
                    trace.extend([starter.nom,node.nom])
                    return True
            return False;

        next_node = iter(self.localisations.values())
        while(True):


            start_node = next(next_node,-2);

            if not start_node.nom == node_ajout:
                continue;

            if start_node == -2:
                return False,trace;

            res = detectionCycle(start_node,None,start_node,0)
            if not res:
                visited.clear();
                continue;
            else:
                return res,trace;

