import player
class Matchmaking:
    def __init__(self):
        self.rounds

    def generatePairings(self, players):
        bye = self.testBye(players)
        return bye
        
    def testBye(self, players):
        if(len(players)%2 == 1):
            score = -1
            bye = None
            for p in players:
                if(score <1 or p.score < score & p.bye == False):
                    score = p.score
                    bye = p
            return bye
        return None

    def hasPlayed(self, player1 = player.Player, player2 = player.Player):
        if(player2 in player1.record):
            return True

    def getScore(self, a):
        return a.score

    def sortPlayers(self, players):
        sorted(players, key = self.getScore)
    def calculateRounds(self, players):
        return NotImplementedError()

