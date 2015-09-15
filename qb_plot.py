import nflgame
import numpy
import matplotlib.pyplot as plt
from pylab import *

# Find our player
team_to_find = "GB"
player_to_find = "A.Rodgers"

# Create a list to store all of the TDs for our player
list_player_tds = []

# Get all the games in 2014
games = nflgame.games_gen(2014, home=team_to_find, away=team_to_find)
for game in games:
  players = game.players
  # Find our player and store the number of passing TDs to our list
  found_player = players.name(player_to_find)
  try:
    list_player_tds.append(found_player.passing_tds)
  except AttributeError:
    list_player_tds.append(0)

# Convert the list of TDs into an array using numpy
arr_tds = numpy.array(list_player_tds)

# Clear the matploylib plot
plt.clf()

# Create a second list for our x-axis values
xaxis = []
for temp_week in arr_tds:
    xaxis.append(len(xaxis) + 1)

# Create a blue line plot to show our TDs
p1, = plt.plot(xaxis, arr_tds, 'b', linewidth=2.0)

# Create a legend for the plot defined above
legend([p1], ["TDs Per Game"])

# Label the ticks of our xaxis using our simple list
plt.xticks(xaxis, xaxis)

# Label the xaxis
plt.xlabel('Games')

# Label the yaxis
plt.ylabel('TDs Per Week by ' + player_to_find)

# Set the y axis limits to 0 and the maximum TDs in a week plus 1
plt.ylim([0, max(arr_tds) + 1])

# Save our chart to a new PNG file. The higher the dpi value, the larger the image
savefig('Aron Rodgers 2014 TDs.png',dpi=72)