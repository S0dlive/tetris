class Game: 
    def start(s):
        print("1. Commencer le jeu")
        print("2. règles du jeu")
        choice = int(input());
        if choice == 1:
            print("Le jeu va commencer . . . ")
        if choice == 2:
            print("regle du jeu :")
            print("Lorsque le menu est affiché, vous devez taper 1 afin de commencer le jeu. ")
            print("Il vous sera alors proposé trois plateaux différents: le cercle,le triangle et le losange.")
            print("Ainsi après avoir choisi le plateaux, celui-ci s'affiche et 3 blocs vous sont présentés.")
            print("Le but de ce jeu est d'obtenir le score le plus élevé possible.")
            print("Pour ce faire vous devez placer les blocs de sorte à créer un maximum de lignes.")

    


if __name__ == "__main__":
    game = Game()
    t = False;
    while t == False:
        game.start();

