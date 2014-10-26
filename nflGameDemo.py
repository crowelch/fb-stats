import nflgame

games = nflgame.games(2013, week=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17])
players = nflgame.combine_game_stats(games)

for player in players.rushing().sort('rushing_yds').limit(25):
	msg = '%s %d carries for %d yards and %d TDs'
	print msg % (player, player.rushing_att, player.rushing_yds, player.rushing_tds)