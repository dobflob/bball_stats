from constants import TEAMS, PLAYERS
import time
import copy


# Clean up player data, return player
def clean_data(player):
    player['height'] = int(player['height'].split(' ')[0])  # drop inches and convert to int
    player['guardians'] = player['guardians'].split(' and ')  # convert guardians to list
    if player['experience'] == 'NO':
        player['experience'] = ''
    player['experience'] = bool(player['experience'])  # convert experience to bool
    return player


# Deep copy TEAMS into list of dicts, then fill teams with experienced players, then fill teams with inexperienced players
# Return filled teams
def balance_teams(players):
    teams = [{"name": team, "players": []} for team in copy.deepcopy(TEAMS)]
    experienced = [player for player in players if player['experience'] == True]
    inexperienced = [player for player in players if player['experience'] == False]
    while experienced:
        for team in teams:
            team['players'].append(experienced.pop())
    while inexperienced:
        for team in teams:
            team['players'].append(inexperienced.pop())
    return teams

# Format all player names and guardians into flat lists, get team size, get number of experienced players, calculate average height of team
# Print stats in clean, easy to read format
def display_stats(team):
    # build a list for player in team players, for guardians in player guardians
    # syntax is the list you want, outloop, inner loop
    guardian_list = [guardians for player in team['players'] for guardians in player['guardians']]
    player_list = [player['name'] for player in team['players']]
    team_size = len(player_list)
    experienced = len([player for player in team['players'] if player['experience']])
    avg_height = sum([player['height'] for player in team['players']])/team_size
    
    print(f'''


{team['name'].upper()} STATS
-------------------------------------------

Total Players: {team_size}
Total Experienced: {experienced}
Total Inexperienced: {team_size - experienced}

Average Height: {round(avg_height,2)} inches

Players on Team:
    {', '.join(player_list)}

Guardians:
    {', '.join(guardian_list)}

    ''')


# Display team menu options and return user's choice
def team_menu():
    teams = copy.deepcopy(TEAMS)
    print(f'''
==== TEAMS ====
A) {teams[0]}
B) {teams[1]}
C) {teams[2]}
        ''')
    return input('> Enter an option:  ').lower()


# Display main menu options and return user's choice
def main_menu():
    print('''
==== MENU ====
A) Display Team Stats
B) Quit
    ''')
    return input('> Enter an option (A/B):  ').lower()


# Control flow of app
def main():
    print('''
          Basketball Team Stats
----------------------------------------
    ''')

    players = [clean_data(player) for player in copy.deepcopy(PLAYERS)]
    balanced_teams = balance_teams(players)

    main_error = True
    while main_error:
        selection = main_menu()
        if selection == 'b':
            main_error = False
            print('\nGoodbye\n')
        elif selection != 'a':
            print('\n xxx Invalid option. Please try again. xxx')
            time.sleep(1)
        else:
            team_error = True
            while team_error:
                team_selection = team_menu()
                if team_selection in 'abc':
                    if team_selection == 'a':
                        display_stats(balanced_teams[0])
                    elif team_selection == 'b':
                        display_stats(balanced_teams[1])
                    elif team_selection == 'c':
                        display_stats(balanced_teams[2])
                    team_error = False
                    time.sleep(2)
                else:
                    print('\n xxx Invalid option. Please try again. xxx')
                    time.sleep(1)

if __name__ == '__main__':
    main()
