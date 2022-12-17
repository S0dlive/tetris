import random;

class Game: 
    blocs_liste = [[[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 1, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [1, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0],
                [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0]],
                [[1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[0, 1, 1, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0]],
                [[1, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0]],
                [[0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1]],
                [[0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],],
                [[0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [1, 0, 0, 1, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0]],
                [[0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 1],
                [0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0]],
                [[0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 1, 0]]]

    def lunch_game(s, spe):
        if spe == "triangle":
            grid = s.read_grid("triangle.txt");
            s.print_grid(grid);
            f = s.select_block(spe)
            for ok in f:
                print(s.print_grid(s.blocs_liste[ok]))
        elif spe == "cercle":
            grid = s.read_grid("cercle.txt");
            s.print_grid(grid);
            f = s.select_block(spe)
            for ok in f:
                print(s.print_grid(s.blocs_liste[ok]))
        elif spe == "losange":
            grid = s.read_grid("losange.txt");
            s.print_grid(grid);
            f = s.select_block(spe)
            for ok in f:
                print(s.print_grid(s.blocs_liste[ok]))

    def valid_position(s, grid, i,j):
        raise NotImplemented
    
    def emplace_bloc(s,grid,i,j):
        raise NotImplemented
    
    # lire les grid d'un fichier
    def read_grid(s,path:str) : #qui retourne une grille valide lue à partir du contenu du fichier
        with open (path, "r") as f:
            grid = []
            for l in f:
                ligne = []
                for c in l:
                    if c == "0":
                        ligne.append(0)
                    if c == "1":
                        ligne.append(1)
                    if c == "2":
                        ligne.append(2)

                grid.append(ligne)
            f.close()
            return grid
    

    def print_grid(s,grid): #affichage de la grille
        for l in grid:
            for c in l:
                if c == 0:  # pas de blocs
                    print(".", end=" ")
                if c == 1: # case vide
                    print("□", end=" ")
                if c == 2: #,case remplie
                    print("■", end=" ")
            print()

    def save_grid(s,path, grid) : #sauvegarde de le grille
        with open (path, "w") as f:
            for l in grid:
                for c in l:
                    f.write(str(c))
                    f.write(" ")
                f.write("\n")
            f.close()

    triangle_liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                    24, 25, 26, 27, 28, 29, 30]
    #liste des blocs pour le plateau triangle
    cercle_liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 31, 32, 33, 34, 35, 36, 37, 38,
                    39, 40, 41, 42]
    #liste des blocs pour le plateau cercle
    losange_liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 43, 44, 45, 46, 47, 48, 49, 50,
                    51, 52, 53, 54, 55, 56]
    
    def select_block(s,spe):
        blocs_choice = [];
        if spe == "triangle":
            t = 0;
            while t < 3:
                p = random.randint(0, len(s.triangle_liste));
                t = t + 1;
                blocs_choice.append(p);
        if spe == "cercle":
            t = 0;
            while t < 3:
                p = random.randint(0, len(s.cercle_liste));
                t = t + 1;
                blocs_choice.append(p);
        if spe == "losange":
            t = 0;
            while t < 3:
                p = random.randint(0, len(s.losange_liste));
                t = t + 1;
                blocs_choice.append(p);
            
        return blocs_choice;
                
    def print_blocs(s,grid): #choix du plateau
        response = [];
        if grid == "triangle":
            for case in s.triangle_liste:
                response.append(s.blocs_liste[case]);
            return response;
        elif grid == "cercle":
            for case in s.cercle_liste:
                return s.blocs_liste[case]
        elif grid == "losange":
            for case in s.losange_liste:
                return s.blocs_liste[case]
        else:
            print("choissisez une forme valide")
            
    # Methode qui va faire fonctionner le jeu.
    def start(s):
        print("1. Commencer le jeu")
        print("2. règles du jeu")
        choice = int(input());
        if choice == 1:
            print("Choisissez votre forme de plateau :")
            game_choice = input();
            s.lunch_game(game_choice);
        if choice == 2:
            print(" ")
            print(" ")
            print(" ")
            print("regle du jeu :")
            print("Lorsque le menu est affiché, vous devez taper 1 afin de commencer le jeu. ")
            print("Il vous sera alors proposé trois plateaux différents: le cercle,le triangle et le losange.")
            print("Ainsi après avoir choisi le plateaux, celui-ci s'affiche et 3 blocs vous sont présentés.")
            print("Le but de ce jeu est d'obtenir le score le plus élevé possible.")
            print("Pour ce faire vous devez placer les blocs de sorte à créer un maximum de lignes.")
            print(" ")
            print(" ")
            print(" ")

    
    


if __name__ == "__main__":
    game = Game();
    while(True):
        game.start();

