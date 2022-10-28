import constants

def clean_data(PLAYERS):
    players = []

    for player in PLAYERS:
        new_player = {}
        new_player['name'] = player['name']
        new_player['guardians'] = player['guardians']
        if player['experience'] == 'YES':
            new_player['experience'] = True
        else:
            new_player['experience'] = False 
        new_player['height'] = int(player['height'].split(' ')[0])
        players.append(new_player)
    return players

