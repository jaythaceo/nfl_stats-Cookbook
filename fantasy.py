import nflgame

teams_active = 31
games = nflgame.games(2015, week=1)
players = nflgame.combine_game_stats(games)
for p in players.rushing().sort("rushing_yds").limit(teams_active):
  msg = '%s %d carries for %d yards and %d TDS'
  print msg % (p, p.rushing_att, p.rushing_yds, p.rushing_tds)