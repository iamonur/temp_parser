import nicer_parser
import former

basic_maze = """
BasicGame
    SpriteSet
        hedef > Immovable color=GREEN
        dusman > Immovable color=RED
        oyuncu > MovingAvatar
            avatar > alternate_keys=True
            #dusman > color=BLUE
        #dusman > stype=avatar alternate_keys=True color=RED
    TerminationSet
        SpriteCounter stype=hedef win=True
        SpriteCounter stype=dusman win=False
    InteractionSet
        dusman hedef > stepBack
        avatar wall > stepBack
        dusman wall > stepBack
        hedef avatar > killSprite
        dusman avatar > killSprite
    LevelMapping
        E > dusman
        G > hedef
"""

#FIXME:
#py-vgdl do not let us to have two moving characters in bot re-play. Thus, I need
#to move the project to python 3.6 to have py-vgdl 2.0. However, I need to be sure
#of that it supports that kind of replay first.

def bot_play():
    import pygame
    from vgdl.interfaces import GameEnvironment
    from vgdl.core import VGDLParser

    former.generate_compile_spin()
    maze = former.mazify()

    a, b = nicer_parser.parse_moves(nicer_parser.parse_trail_out())
    avatar_actions, opponent_actions = nicer_parser.change_to_actions(a, b)

    g = VGDLParser().parseGame(basic_maze)
    g.buildLevel(maze)

    env = GameEnvironment(g, visualize=True, actionDelay=100)
    env.rollOut(actions)

if __name__ == "__main__":
    bot_play()
