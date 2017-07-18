class Team:
    def __init__(self, team):
        self.name = team['name']
        self.code = team['code']
        self.shortName = team['shortName']
        self.squadMarketValue = team['squadMarketValue']
        self.crestURL = team['crestURL']
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def get_shortName(self):
        return self.shortName
    def get_squadMarketValue(self):
        return self.squadMarketValue