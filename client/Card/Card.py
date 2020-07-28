from PIL import Image
from pathlib import Path, WindowsPath
class Card:
    def __init__(self, fileName):
        self._fileName = fileName

    def getFileName(self):
        return self._fileName

class MemeCard(Card):
    def __init__(self, fileName):
        super().__init__(fileName)
        path = Path(__file__).parent / WindowsPath("memes/" + str(fileName))
        self._image = Image.open(path)

    def getImage(self):
        return self._image

class PhraseCard(Card):
    def __init__(self, fileName, playerName):
        super().__init__(fileName)
        self._playerName = playerName
        path = Path(__file__).parent / WindowsPath("phrases/" + str(fileName))
        self._phrase = open(path).read()

    def getText(self):
        return self._phrase

    def getPlayerName(self):
        return self._playerName