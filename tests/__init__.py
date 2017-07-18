import sys

path = r'C:\Users\trish_000\PycharmProjects\Footyy\src'
sys.path.append(path)

from Footyy import get_competitions, get_teams, get_players

comps = get_competitions()
for comp in comps:
    teams = get_teams(comp.get_id())
    for team in teams:
        players = get_players(team.get_id())
        if len(players):
            print players