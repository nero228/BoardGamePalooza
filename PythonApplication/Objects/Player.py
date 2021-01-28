class Player(object):
    """description of class"""
    def __init__(playerId, playerName, playerToken, playerColor, playerMoney, playerPositionID):
        self.playerId = playerId
        self.playerName = playerName
        self.playerToken = playerToken
        self.playerColor = playerColor
        self.playerMoney = playerMoney
        self.playerPositionID = playerPositionID
        self.OutOfJailChance = false
        self.OutOfJailCommunityChest = false

    def getPlayerId():
        print("PLAYER ID")
    def getPlayerName():
        print("I'm reginold")
    def getPlayerToken():
        print("Car, always the car")
    def getPlayerColor():
        print("Red")
    def getPlayerMoney():
        print("CASH DOLLA DOLLA")
    def getPlayerPositionID():
        print("A-4 Checkmate")
    #Bottom 2 are booleans
    def getOutOfJailChance():
        print("LET ME OUTTA HERE CHANCE")
    def getOutOfJailCommunityChest():
        print("LET ME OUTTA HERE CommunityChest")

