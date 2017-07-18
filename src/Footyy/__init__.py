import requests
import json
from Competition import Competition
from Team import Team
from Player import Player

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

