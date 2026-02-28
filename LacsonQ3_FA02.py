
import numpy as pyn

chess_players = ["Magnus", "Hikaru", "Gukesh"]
ELO = pyn.array([
    [12, -8, 14, 9, 5],
    [-5, -9, 10, -7, 14],
    [-6, 13, -12, -9, 12]
    ])

print(ELO[2][3])