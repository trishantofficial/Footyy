
class Competition:
    def __init__(self, competition):
        self.id = competition['id']
        self.caption = competition['caption']
        self.league = competition['league']
        self.year = competition['year']
        self.currentMatchday = competition['currentMatchday']
        self.currentMatchdays = competition['numberOfMatchdays']
        self.numberOfTeams = competition['numberOfTeams']
        self.numberOfGames = competition['numberOfGames']
        self.lastUpdated = competition['lastUpdated']
    def get_id(self):
        return self.id
    def get_caption(self):
        return self.caption
    def get_league(self):
        return self.league
    def get_year(self):
        return self.year
    def get_currentMatchday(self):
        return self.currentMatchday
    def get_currentMatchdays(self):
        return self.currentMatchdays
    def get_numberOfTeams(self):
        return self.numberOfTeams
    def get_numnberOfGames(self):
        return self.numberOfGames
    def get_lastUpdated(self):
        return self.lastUpdated
