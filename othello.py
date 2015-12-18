import game

print "Othello"

numPlayers = int(raw_input("Number of players (0-2): "))
game = game.Game(numPlayers)
game.play()
