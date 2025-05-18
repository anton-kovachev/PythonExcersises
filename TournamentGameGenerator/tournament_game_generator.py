# Write your code here.
import random

def get_number_of_teams():
    number_of_teams = None 
    
    while number_of_teams is None:
        number_of_teams_input = input("Enter the number of teams in the tournament: ")
        
        if not number_of_teams_input.isdigit():
            print("You have to enter a valid integer number, try again")
        elif int(number_of_teams_input) < 2:
            print("The minimum number of teams is 2, try again")
        elif int(number_of_teams_input) % 2 != 0:
            print("You have to enter an even number of teams")
        else:
            number_of_teams = int(number_of_teams_input)
        
    return number_of_teams

def get_team_names(num_teams):
    team_names = []
    
    for i in range(num_teams):
        team_name = None
        
        while team_name is None:
            team_name_input = input(f"Enter the name for team #{i+1} ")
            if len(team_name_input) < 2:
                print("Team names must have at least 2 characters, try again.")
            elif len(team_name_input.split(" ")) > 2:
                print("Team names must have at most 2 words, try again.")
            else:
                team_name = team_name_input
        
        team_names.append(team_name)

    return team_names

def get_number_of_games_played(num_teams):
    number_of_games_played = None
    
    while number_of_games_played is None:
        number_of_games_played_input = input("Enter the number of games played by each team: ")
        
        if not number_of_games_played_input.isdigit():
            print("You have to enter a valid number, try again")
        elif int(number_of_games_played_input) < num_teams - 1:
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        else:
            number_of_games_played = int(number_of_games_played_input)

    return number_of_games_played

def get_team_wins(team_names, games_played):
    team_wins = {}
    
    for team_name in team_names:
        number_of_wins = None
        
        while number_of_wins is None:
            number_of_wins_input = input(f"Enter the number of wins Team {team_name} had: ")
            
            if not number_of_wins_input.isdigit():
                print("You have to enter a valid number, try again")
            elif int(number_of_wins_input) < 0:
                print("The minimum number of wins is 0, try again.")
            else:
                number_of_wins = int(number_of_wins_input)
        
        team_wins[team_name] = number_of_wins                
        
    return team_wins 


# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")
sorted_teams = sorted(team_names, key=lambda x: team_wins[x], reverse=True)

while len(sorted_teams) > 0:
    print(f"Home {sorted_teams[0]} VS Away {sorted_teams[-1]}")
    sorted_teams = sorted_teams[1:-1]