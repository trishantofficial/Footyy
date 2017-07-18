class Team:
    def __init__(self, team):
        self.id = team['_links']['self']['href']
        pos = self.id.rfind('/') + 1
        self.id = self.id[pos:]
        self.name = team['name']
        self.code = team['code']
        self.shortName = team['shortName']
        self.squadMarketValue = team['squadMarketValue']
        self.crestUrl = team['crestUrl']
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def get_shortName(self):
        return self.shortName
    def get_squadMarketValue(self):
        return self.squadMarketValue