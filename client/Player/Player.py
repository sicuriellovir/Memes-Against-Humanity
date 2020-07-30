from .. import client
from ..Card import PhraseCard

class Player:
    def __init__(self, name):
        phraseCard1 = PhraseCard(client.getNewPhraseCard(), name)
        phraseCard2 = PhraseCard(client.getNewPhraseCard(), name)
        phraseCard3 = PhraseCard(client.getNewPhraseCard(), name)
        self._phraseCards = [phraseCard1, phraseCard2, phraseCard3]
        self._username = name

    def isJudge(self):
        return client.isJudge()

    def getPhraseCards(self):
        return self._phraseCards

    def getUsername(self):
        return self._username

    def getPoints(self):
        return client.getPoints(self._username)

    def replaceCard(self, cardToRemove):
        self._phraseCards.remove(cardToRemove)
        newCard = PhraseCard(client.getNewPhraseCard(), self.getUsername())
        self._phraseCards.append(newCard)
