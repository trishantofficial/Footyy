import sys
import os

path = str(os.path.split(os.path.split(sys.argv[0])[0])[0]) + "/src"
sys.path.append(path)

from Footyy import get_competitions, get_teams, get_players

comps = get_competitions()
for comp in comps:
    print "Competition: " + str(comp.get_id())
    teams = get_teams(comp.get_id())
    for team in teams:
        print "Team name:" + team.get_name()
        players = get_players(team.get_id())
        if len(players):
            print players
        else:
            print "Couldn't find players."