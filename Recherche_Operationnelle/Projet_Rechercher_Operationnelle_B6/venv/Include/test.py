from Include import Balas_Hammer,Affichage_tableau,TraitementContenu,Nord_Ouest
import copy


while(True):


    demand = input("Veuillez taper 1 - 12 pour choisir un fichier de test, et taper 0 pour quiter le programme\n")

    if int(demand) == 0:
        print("Au revoir")
        break;
    elif int(demand) < 1 or int(demand) > 12:
        print("La valeur insérée est faute, veuillez choisir de nouveau")
        continue;
    else:

        fichier = TraitementContenu.Contenu
        matrice_coût_commande_provision = fichier.importationFichier("../ressources/test"+demand+".txt")
        matrice_potentiel = fichier.importationFichier("../ressources/test"+demand+".txt")
        matrice2 = fichier.importationFichier("../ressources/test"+demand+".txt")
        liste_fournisseur_client = fichier.creer_liste_fornisseur_client(matrice_coût_commande_provision)

        tab = Affichage_tableau.Affichage_tableau
        print("\nMatrice de coût:")
        tab.afficher_tab_initial(matrice_coût_commande_provision,liste_fournisseur_client)

        print("\nProposition de transport(Nord-Ouest):")
        tab.afficher_tab_initial(Nord_Ouest.nord_ouest(matrice_coût_commande_provision),liste_fournisseur_client);


        res = copy.deepcopy(matrice2)
        arret = (len(matrice2[0])-1) * (len(matrice2)-1)
        print("\nLes pénalité maximale:")
        Balas_Hammer.Balas_Hammer.proposition_initiale(matrice2,res,0,arret,liste_fournisseur_client[1],liste_fournisseur_client[0])


        test = Balas_Hammer.Balas_Hammer();
        ensemble_prec = []
        arret_negative = []
        while(True):

            print("\nProposition de transport(Balas-Hammer):")
            tab.afficher_tab_initial(res, liste_fournisseur_client)
            cout_total = Balas_Hammer.Balas_Hammer.calculerCoutTotal(matrice_coût_commande_provision, res)
            print("Le coût total pour la proposition de transport est: {:d}".format(cout_total))
            new_res = copy.deepcopy(res)
            if len(arret_negative) != 0:
                new_res[arret_negative[0]][arret_negative[1]] = 1;
            val = test.choisirAreteAjoute(new_res,matrice_coût_commande_provision,liste_fournisseur_client[1],liste_fournisseur_client[0],ensemble_prec)
            new_arbre = val[0]
            ensemble_prec = val[1]
            print("\nLes potentiels par sommet:")
            test.calculValueNode(matrice_coût_commande_provision,new_arbre,liste_fournisseur_client[1],liste_fournisseur_client[0],0)
            test.calculPotentiel(matrice_potentiel,new_arbre,liste_fournisseur_client[1],liste_fournisseur_client[0])
            print("\nTable des coûts potentiels:")
            tab.afficher_tab_initial(matrice_potentiel,liste_fournisseur_client)
            matrice_marginaux = test.calculMarginaux(matrice_coût_commande_provision,matrice_potentiel);
            print("\nTable des coûts marginaux:")
            tab.afficher_tab_initial(matrice_marginaux,liste_fournisseur_client)

            result = test.detecterValNegative(matrice_marginaux,new_arbre,res,liste_fournisseur_client[1],liste_fournisseur_client[0])
            if not result[0]:
                print("Le coût de transport est minimisé")
                print("Le coût total pour la proposition de transport est: {:d}".format(cout_total))
                break;
            else:
                fournisseur = liste_fournisseur_client[1].index(result[1][0])
                client = liste_fournisseur_client[0].index(result[1][1])
                arret_negative = [fournisseur,client]
                if res[fournisseur][client] == new_res[fournisseur][client]:
                    for each in ensemble_prec:
                        new_arbre.localisations[each[0]].connections.remove(new_arbre.localisations[each[1]])
                        new_arbre.localisations[each[1]].connections.remove(new_arbre.localisations[each[0]])
