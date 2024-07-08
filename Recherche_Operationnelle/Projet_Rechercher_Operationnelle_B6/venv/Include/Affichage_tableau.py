class Affichage_tableau:

    def afficher_tab_initial(matrice:list,noms:list):

        NOMBRE_ESPACE_ONE = 15
        NOMBRE_ESPACE_TWO = 5

        print("".center(NOMBRE_ESPACE_ONE * 2 + (NOMBRE_ESPACE_TWO+1) * ((len(matrice[0])) - 1) + (len(matrice[0]))+2, "-"))
        print("|",end="")
        print("".center(NOMBRE_ESPACE_ONE, " "), end="")
        print("|", end="")
        for index, value in enumerate(noms[0]):

            if index == len(noms[0]) - 1:

                print(value.center(NOMBRE_ESPACE_ONE, " "), end="")
                print("|", end="")
            else:
                print(value.center(NOMBRE_ESPACE_TWO, " ")+ " ", end="")
                print("|", end="")
        print("")
        print("".center(NOMBRE_ESPACE_ONE * 2 + (NOMBRE_ESPACE_TWO+1) * ((len(matrice[0])) - 1) + (len(matrice[0]))+2, "-"))

        for index,each in enumerate(matrice):

            print("|",end="")

            if index == len(matrice)-1:
                print(noms[1][index].center(NOMBRE_ESPACE_ONE, " "),end="")
                print("|",end="")
            else:
                print(noms[1][index].center(NOMBRE_ESPACE_ONE," "),end="")
                print("|",end="")

            for index, i in enumerate(each):

                if index == len(matrice[0])-1:
                    print('{:^15d}'.format(i),end="")
                    print("|",end="")
                elif index == len(each)-1:
                    print('{:^6d}'.format(i),end="")
                    print("|", end="")
                    print("".ljust(NOMBRE_ESPACE_ONE," "),end="")
                    print("|", end="")
                else:
                    print('{:^6d}'.format(i),end="")
                    print("|",end="")

            print("")
            print("".center(NOMBRE_ESPACE_ONE * 2 + (NOMBRE_ESPACE_TWO+1) * ((len(matrice[0])) - 1) + (len(matrice[0]))+2, "-"))