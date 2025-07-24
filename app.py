from constants import TEAMS, PLAYERS
import time
import copy


# Clean up player data
def clean_data(player):
    player['height'] = int(player['height'].split(' ')[0])  # drop inches and convert to int
    player['guardians'] = player['guardians'].split(' and ')  # convert guardians to list
    if player['experience'] == 'NO':
        player['experience'] = ''
    player['experience'] = bool(player['experience'])  # convert experience to bool
    return player

# TODO: Balance Teams Function
#   balance players across the 3 teams
#   teams should have the same number of total players


# TODO: Additional Team Balancing
#   balance team so that each team has the same number of experienced vs inexperienced
#   if done correctly, each team's stats should display the same count for experienced total and inexperienced total, as well as the same number of players on the team

def balance_teams():
    pass

# TODO: Console Readability
#   when the menu or stats display to the console, it should be in a nice readable format

# TODO: Displaying Stats
#   when displaying the selected team's stats, include:
#   Team's name (str)
#   Total Players (int)
#   Player names, separated by commas (strs)

# TODO: Additional Stats
#   the number of inexperienced players on the team
#   the number of experienced players on the team
#   average height of the team
#   guardians of all players on the team as a comma separated string

def display_stats(choice):
    input('Press Enter to continue...')


def team_menu():
    print(f'''
==== TEAMS ====
    
        ''')
    return input('> Enter an option:  ').lower()


def main_menu():
    print('''
==== MENU ====
A) Display Team Stats
B) Quit
    ''')
    return input('> Enter an option (A/B):  ').lower()


def main():
    print('''
          Basketball Team Stats
----------------------------------------
    ''')

    players = [clean_data(player) for player in copy.deepcopy(PLAYERS)]

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
                    display_stats(team_selection)
                    team_error = False
                else:
                    print('\n xxx Invalid option. Please try again. xxx')
                    time.sleep(1)

if __name__ == '__main__':
    main()