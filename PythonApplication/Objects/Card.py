class Card(object):
    """description of class"""
    def __init__(cardID, cardName, cardDescription):
        self.cardID = cardID
        self.cardName = cardName
        self.cardDescription = cardDescription

    def getCardID():
        print("id")
    def getCardName():
        print("CHANCE TIME")
    def getCardDescription():
        print("The FitnessGram PACER Test is a multistage aerobic capacity test that progressively gets more difficult as it continues.")
 # list of all cards
 # CHANCE:
 # Advance to go: money +200 set PosID to 0
 # Advance to St. Charles Place:
 # set PosID to 11 run space check on player
 # Advance to nearest Utility
 #  if PosID=7 set PosID to 12 else set PosID to 28 then run space check outside of if else
 # Advance to nearest railroad:
 #if PosID=8 set PosID to 5 else if PosID=22 set PosID to 25 else set PosID to 35 after if else run space check if owned multiply rent by 2(there is two of this card)
 # Bank pays you dividend of $50:
 # money +50
 # Get out of jail free:
 # remove card from the queue and set ChanceGetOut to 1
 # Go back 3 spaces:
 # PosID -3 run space check
 # Go to jail:
 # set InJail to 1 set PosID to 10 run Jail
 # Make general repairs on all your property: For each house pay $25, For each hotel $100:
 # money - (housesx25+hotelsx100)
 # Pay poor tax of $15:
 # money - 50
 #
