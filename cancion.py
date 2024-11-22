class Cancion:
    title = ""
    link = ""

    # Constructor
    def __init__(self, title):
        self.title = title

    # Gettes & Setters
    def getTitle(self):
        return self.title

    def setLink(self, link):
        self.link = link
