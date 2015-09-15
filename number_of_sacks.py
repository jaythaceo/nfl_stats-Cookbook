
import nflgame

def total_sacks_given(s,w,t):
  games = nflgame.games_gen(s,w,t,t)
  plays = nflgame.combine_plays(games)

  sks = 0
  for p in plays.filter(team=t):
    if p.defense_sk > 0:
      sks += 1
  return sks

def total_sacks_earned(s,w,t):
  games = nflgame.games_gen(s,w,t,t)
  plays = nflgame.combine_plays(games)

  sks = 0
  for p in plays.filter(team_ne=t):
    if p.defense_sk > 0:
      sks += 1
  return sks

print total_sacks_earned(2013, None, "GB")
print total_sacks_given(2013, None, "GB")
print total_sacks_earned(2013, q10, "GB")
print total_sacks_earned(2013, [1,2,3,4,5,6,7], "GB")