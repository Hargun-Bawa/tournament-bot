import matchmaking

class Bracket(matchmaking.Matchmaking):
    def __init__(self):
        self.tree
    
    def calculateRounds(self, players):
        rounds = int(len(players).bit_length())
        return rounds

    def createRound(round):
       tourneyNodes = []




def main():
    s = matchmaking.player.Player(name = "steve",  id = 2)
    s.score = 4
    a = Bracket()
    print(a.calculateRounds([1,2,3,4,5,1,2,34,2, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]))

def generatePairings():

    pass

class TourneyNode:
    def __init__(self):
        self.p1
        self.p2
        self.winnerNode
        self.loserNode

    def addPlayer(self, player):
        if self.p1:
            self.p2 = player
        else:
            self.p1 = player
    def results(self, player):
        if self.winnerNode:
            if(player == self.p1):
                self.winnerNode.addPlayer(self.p1)
                self.loserNode.addPlayer(self.p2)
            else:
                self.winnerNode.addPlayer(self.p2)
                self.loserNode.addPlayer(self.p1)
        else:
            return False

if __name__ == "__main__":
    main()

