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


def print_menu():
    print('------ MENU ------\n')
    print('Here are your choices:1\n1) Display Teams Stats\n2) Quit\n')
    option_1 = int(input('Enter an option: '))
    if option_1 == 2:
        return
    elif option_1 == 1: 
        print('1) Panthers\n2) Bandits\n3) Warriors')
        option_2 = int(input('Enter an option: \n'))
        if option_2 == 1:
            print_stats(panther, 'Panthers')
        elif option_2 == 2:
            print_stats(bandits, 'Bandits')
        elif option_2 == 3:
            print_stats(warriors, 'Warriors')

def print_stats(team, team_name):
    total_experienced = 0
    total_inexperienced = 0
    avg_height = 0
    total_height = 0
    players_names = ''
    guardians =''

    for index, player in enumerate(team):
        total_height += player['height']
        if index < len(team) - 1:
            players_names += (player['name']).strip() + ', '
            guardians += ', '.join(map(str.strip, player['guardians'])) + ', '
        else:
            players_names += player['name']
            guardians += ', '.join(map(str.strip, player['guardians']))
        if player['experience']:
            total_experienced += 1
        else:
            total_inexperienced += 1

    avg_height = total_height / len(team)

    print(f'Team {team_name} Stats')
    print('-----------------------')
    print(f'Total players: {len(team)}')
    print(f'Total experienced: {total_experienced}')
    print(f'Total inexperienced: {total_inexperienced}')
    print(f'Average height: {avg_height}\n')
    
    print(f'Players on Team: \n{players_names}\n')
    print(f'Guardians:\n{guardians}')

if __name__ == '__main__':
    clean_data(players)
    balance_teams()
    print_menu()


