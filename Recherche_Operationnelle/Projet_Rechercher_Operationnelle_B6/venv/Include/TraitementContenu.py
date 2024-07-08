#La classe pour convertir le contenu du fichier en matrice
class Contenu:

    """
    :parameter:
        chemin - L'emplacement du fichier cible
    :return:
        matrice - Le tableau de contraintes sous forme de matrice
    """
    def importationFichier(chemin):
        matrice = []
        #Stream I/O pour importer le fichier dans le memoire
        with open(chemin,"r") as file:
            while(True):
                #lire le fichier ligne par ligne
                ligne = file.readline()
                #Si la lecture du fichier est arrivée à la fin, arrêter!
                if not ligne:
                    break
                #Mettre chaque ligne du matrice dans une liste en les convertissant en entité
                contenu = list(map(int, ligne.split(" ")))
                matrice.append(contenu)

            return matrice

    """
    :parameter:
        nombre - La matrice qui contient la liste des coûts de transport 
                 afin de indiquer le nombre de client et celui de fournisseur
    :var:
        fourniseurs - Liste des noms de fornisseur
        clients - Liste des noms de client
        
    :return:
        groupe - La liste qui contient tous les noms de fournisseur et ceux de client
    """
    def creer_liste_fornisseur_client(nombre: list):

        fournisseurs = []
        clients = []

        #remplir la liste de fournisseurs
        for each in range(1,len(nombre)+1):

            if each == len(nombre):
                fournisseurs.append("Commandes Cj")
            else:
                fournisseurs.append("P"+str(each))

        #remplir la liste de client
        for each in range(1,len(nombre[0])+1):

            if each == len(nombre[0]):
                clients.append("Provisions Pi")
            else:
                clients.append("C"+str(each))


        return clients,fournisseurs