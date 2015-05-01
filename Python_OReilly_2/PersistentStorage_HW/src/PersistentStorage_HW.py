"""Function takes 2 arguments, and keeps the high score of each input"""

import shelve
import os
import tempfile

def player_scores(player, score):
    input_data = (player, score)
    origdir = os.getcwd()
    #dirname = tempfile.mkdtemp("testdir")
    #player_score_data = r'v:\workspace\PersistentStorage_HW\src\player_score_data.shlf'
    player_score_data = r'player_score_data.shlf'
    player_string = str(player).lower()
    shelf = shelve.open(player_score_data, writeback=True)
    
#    shelf = shelve.open(r'v:\workspace\PersistentStorage_HW\src\player_score_data.shlf', writeback=True)

    try:
        if player_string in shelf:
            if shelf[player_string]< score:
                shelf[player_string] = score
        else:
            shelf[player_string] = score
    except KeyError:
        print('KeyError') #what else should I return here?

    shelf.sync()
            
    return shelf[player_string]

    shelf.close()


#print(player_scores('kelsey', 3))