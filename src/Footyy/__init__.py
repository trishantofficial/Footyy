import requests
import json
from Competition import Competition
from Team import Team
from Player import Player
import sys

token = 'c77774a514aa410d9c257c582abf1307'
headers = { 'X-Auth-Token' : token }


def get_competitions(season=None):
    url = "http://football-data.org/v1/competitions"
    if season:
        url += "/?season=" + str(season)
    req = requests.get(url,headers=headers)
    data = json.loads(req.content)
    competitions = []
    for comp in data:
        competition = Competition(comp)
        competitions.append(competition)
    return competitions

def get_teams(id):
    url = "http://football-data.org/v1/competitions/" + str(id) + "/teams"
    req = requests.get(url,headers=headers)
    data = json.loads(req.content)
    count = data['count']
    teams = []
    teams_data = data['teams']
    for t in teams_data:
        team = Team(t)
        teams.append(team)
    return teams

def get_team(id):
    url = "http://football-data.org/v1/teams/" + str(id)
    req = requests.get(url,headers=headers)
    data = json.loads(req.content)
    team = Team(data)
    return team


def get_players(id):
    url = "http://football-data.org/v1/teams/" + str(id) + "/players"
    req = requests.get(url,headers=headers)
    data = json.loads(req.content)
    players = []
    if len(data['players']):
        for p in players:
            player = Player(p)
            players.append(player)
    return players


def main_menu():
    print "-----| Menu |-----"
    print ""
    print "1.) Get list of competitions"
    print "2.) Get list of teams in a competition"
    print "3.) Get list of players in a team"
    print ""
    print "-----|  Menu |-----"
    return int(raw_input("Enter choice: "))


def choice1():
    season = str(raw_input("Enter season?"))
    if season == "Y" or season == "y":
        season = int(raw_input("Enter season year: "))
        competitions = get_competitions(season)
    else:
        competitions = get_competitions()
    for competition in competitions:
        print "Competition ID: " + str(competition.get_id()) + " Competiton League: " + str(competition.get_league())
    print "\n\n"
    print "1.) Get Competiton data"
    print "2.) Get teams of a competition"
    print "3.) Main Menu"
    print "4.) Exit"
    choice = int(raw_input("Enter choice: "))
    if choice == 1:
        comp_id = int(raw_input("Enter ID of competition you wish to get data of: "))
        for competition in competitions:
            if comp_id == int(competition.get_id()):
                print competition.get_data()
    elif choice == 2:
        choice2()
    elif choice == 3:
        main()
    elif choice == 4:
        sys.exit(1)
    else:
        print "Invalid choice"
        choice1()


def choice2():
    comp_id = int(raw_input("Enter ID of competition you wish to get teams of: "))
    teams = get_teams(comp_id)
    for team in teams:
        print "Team ID: " + str(team.get_id()) + " Team name: "
    print "\n\n"
    print "1.) Get Team data"
    print "2.) Get players of a team"
    print "3.) Main Menu"
    print "4.) Exit"
    choice = int(raw_input("Enter choice: "))
    if choice == 1:
        team_id = int(raw_input("Enter ID of team you wish to get data of: "))
        for team in teams:
            if team_id == int(team.get_id()):
                print team.get_data()
    elif choice == 2:
        choice3()
    elif choice == 3:
        choice1()
    elif choice == 4:
        sys.exit()
    else:
        print "Invalid option entered."
        choice2()

def choice3():
    team_id = raw_input("Enter ID of team you wish to get players of: ")
    players = get_players(team_id)
    for player in players:
        print "Player ID: " + str(player.get_id()) + "Player name: " + str(player.get_name())
    print "\n\n"
    print "1.) Get data of a player"
    print "2.) Get data of all players"
    print "3.) Main menu"
    print "4.) Exit"
    choice = int(raw_input("Enter choice: "))
    if choice == 1:
        player_id = int(raw_input("Enter ID of player you wish to get data of: "))
        for player in players:
            if player_id == player.get_id():
                player.get_data()
    elif choice == 2:
        for player in players:
            player.get_data()
    elif choice == 3:
        main()
    elif choice == 4:
        sys.exit(1)
    else:
        print "Invalid choice"
        choice3()

def main():
    choice = main_menu()
    if choice == 1:
        choice1()
    if choice == 2:
        choice2()
    if choice == 3:
        choice3()
    if choice == 4:
        sys.exit(1)


main()