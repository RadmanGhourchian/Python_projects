import re

game = input('Enter your favorite game name: ')
game = game.replace(" ", "_")
if re.match(r"^(Minecraft|zula|elden_rings|joy_of_proggraming)$", game, re.I):
    print("congrats")
else:
    print("DUMB!")