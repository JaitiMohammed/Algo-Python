#Représentation d'un graphe par un dictionnaire

grapheDeco = {
    'K':{'M' :4,'E':1},
    'M':{'E':2,'H':2},
    'E':{'M':1,'H':3,'F':1},
    'H':{'F':3},
    'F':{'H':1},
    'S':{'H':1,'F':2}
}

dicoDijsktra(grapheDeco ,'K')

#Représentation par une matrice d'adjacence

grapheMatrice = [
    [ ],
    [ ],
    [ ],
    [ ],
    [ ],
    [ ]
]