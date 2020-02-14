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

maze= """
wwwwwwww
wA     w
w     Gw
w   E  w
w      w
w      w
w      w
wwwwwwww
"""

actions = [3, 3, 3, 3, 3, 2, 0, 2, 0, 0, 0]

if __name__ == "__main__":
    import pygame
    #from ontology import DARKGRAY, BASEDIRS, LIGHTGRAY, RED, LIGHTBLUE
    from vgdl.interfaces import GameEnvironment
    from vgdl.core import VGDLParser
    g = VGDLParser().parseGame(basic_maze)
    g.buildLevel(maze)

    #VGDLParser.playGame(basic_maze, maze)
    env = GameEnvironment(g, visualize=True, actionDelay=100)
    env.rollOut(actions)
    #env.reset()
