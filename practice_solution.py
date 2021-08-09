import pandas as pd
from matplotlib import pyplot as plt


class VideoGameStatistics:

    def __init__(self):
        self.games = pd.read_csv("video_game_classifications.csv", encoding='cp1252')

    # GET ALL THE GAME TITLES AND PRINT THEIR TITLES OUT
    def getGamesTitles(self):
        print(self.games["title"])

    # GET ALL THE M18 GAMES AND PRINT THEIR TITLES OUT
    def getM18Games(self):
        mgames = self.games[self.games["rating"] == "Mature 18"]
        print(mgames["title"])

    # GET ALL THE NINTENDO SWITCH GAMES AND PRINT THEIR TITLES OUT
    def getNintendoSwitchGames(self):
        switchgames = self.games[self.games["platform"].str.contains("Nintendo Switch")]
        print(switchgames["title"])

    # GET THE GAMES RELEASED IN A CERTAIN YEAR AND PRINT THEIR TITLES OUT
    def getGamesByReleaseYear(self, year):
        yeargames = self.games[self.games["year_release"] == year]
        print(yeargames["title"])

    # GET THE NUMBER OF M18 GAMES
    def getNumberOfM18Games(self):
        mgames = self.games[self.games["rating"] == "Mature 18"]
        return len(mgames)

    # GET THE MEDIAN RELEASE YEAR
    def getMedianReleaseYear(self):
        return self.games["year_release"].median()

    # GET THE MEAN RELEASE YEAR
    def getMeanReleaseYear(self):
        return self.games["year_release"].mean()

    # GET THE NUMBER OF M18 GAMES RELEASED IN A PARTICULAR YEAR
    def getNumberOfM18GamesReleasedInYear(self, year):
        mgames = self.games[(self.games["rating"] == "Mature 18") & (self.games["year_release"] == year)]
        return len(mgames)

    # GET THE NUMBER OF SWITCH GAMES RELEASED IN A PARTICULAR YEAR
    def getNumberOfSwitchGamesReleasedInYear(self, year):
        sgames = self.games[(self.games["platform"].str.contains("Nintendo Switch")) & (self.games["year_release"] == year)]
        return len(sgames)


# USE THE FOLLOWING CODE TO TEST YOUR SOLUTION OUT


vgs = VideoGameStatistics()

vgs.getGamesTitles()
vgs.getM18Games()
vgs.getNintendoSwitchGames()
vgs.getGamesByReleaseYear(2018)

print("\n")
print("Number of M18 Games is: " + str(vgs.getNumberOfM18Games()))
print("Median Release Year is: " + str(vgs.getMedianReleaseYear()))
print("Mean Release Year is: " + str(vgs.getMeanReleaseYear()))
print("M18 Games Released in 2018: " + str(vgs.getNumberOfM18GamesReleasedInYear(2018)))
print("Switch Games Released in 2018: " + str(vgs.getNumberOfSwitchGamesReleasedInYear(2018)))
