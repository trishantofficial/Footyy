import requests
import json
from Competition import Competition
from Team import Team

def get_competitions(season=None):
    url = "http://football-data.org/v1/competitions"
    if season:
        url += "/?season=" + str(season)
    req = requests.get(url)
    data = json.loads(req.content)
    competitions = []
    for comp in data:
        competition = Competition(comp)
        competitions.append(competition)
    return competitions

def get_teams(id):
    url = "http://football-data.org/v1/competitions/" + str(id) + "/teams"
    req = requests.get(url)
    data = json.loads(req.content)
    count = data['count']
    teams = data['teams']
    return teams

cs = get_competitions()
for c in cs:
    print get_teams(c.get_id())