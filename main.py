from game import Game
from display import plot

game = Game().game_run()

plot(game.game_stats)
