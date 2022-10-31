import constants

players = constants.PLAYERS
teams = constants.TEAMS
panther = []
bandits = []
warriors = []
experinced_players = []
non_experienced_players = []


def clean_data(PLAYERS):

    for player in players:
        new_player = {}
        new_player['name'] = player['name']
        new_player['guardians'] = player['guardians'].split('and')
        new_player['height'] = int(player['height'].split(' ')[0])
        if player['experience'] == 'YES':
            new_player['experience'] = True
            experinced_players.append(new_player)
        else:
            new_player['experience'] = False 
            non_experienced_players.append(new_player)
    return experinced_players, non_experienced_players

def balance_teams():
    players_per_team = len(players) // len(teams)
    exp_players_per_team = len(experinced_players) // len(teams)

    for exp_player in experinced_players:
        if len(panther) < exp_players_per_team:
            panther.append(exp_player)
        elif len(warriors) < exp_players_per_team:
            warriors.append(exp_player)
        else:
            bandits.append(exp_player)
    
    for non_exp_player in non_experienced_players:
        if len(panther) < players_per_team:
            panther.append(non_exp_player)
        elif len(warriors) < players_per_team:
            warriors.append(non_exp_player)
        else:
            bandits.append(non_exp_player)


def print_status():
    print('------ MENU ------\n')
    print('Here are your choices:1\n1) Display Teams Stats\n2) Quit\n')
    option_1 = input('Enter an option: ') 
    print('1) Panthers\n2) Bandits\n3) Warriors')
    option_2 = input('Enter an option: ')

if __name__ == '__main__':
    print_status()
    clean_data(players)
    balance_teams()
    print(len(warriors))
    for player in warriors:
        print(player)


