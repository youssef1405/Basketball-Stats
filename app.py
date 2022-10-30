import constants

PLAYERS = constants.PLAYERS
TEAMS = constants.TEAMS
Panther = []
Bandits = []
Warriors = []


# print(len(PLAYERS)) 18

def clean_data(PLAYERS):
    players = []

    for player in PLAYERS:
        new_player = {}
        new_player['name'] = player['name']
        new_player['guardians'] = player['guardians'].split('and')
        if player['experience'] == 'YES':
            new_player['experience'] = True
        else:
            new_player['experience'] = False 
        new_player['height'] = int(player['height'].split(' ')[0])
        players.append(new_player)
    return players

# def balance_teams():


if __name__ == '__main__':
    print(clean_data(PLAYERS)[:2])

