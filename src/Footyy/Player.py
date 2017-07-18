class Player:
    def __init__(self, player):
        self.id = player['id']
        self.name = player['name']
        self.position = player['position']
        self.jerseyNumber = player['jerseyNumber']
        self.dateOfBirth = player['dataOfBirth']
        self.nationality = player['nationality']
        self.contractUntil = player['contractUntil']
        self.marketValue = player['marketValue']
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_position(self):
        return self.position
    def get_jerseyNumber(self):
        return self.jerseyNumber
    def get_dateOfBirth(self):
        return self.dateOfBirth
    def get_nationality(self):
        return self.nationality
    def get_contractUntil(self):
        return self.contractUntil
    def get_marketValue(self):
        return self.marketValue