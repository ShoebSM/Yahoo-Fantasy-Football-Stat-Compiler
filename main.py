from pathlib import Path

# short application to check fantasy football records

app_name = 'mcc_ff_tracker'
game_code = 'nfl'
game_key = 449  # 2024 nfl game code
# 461 -> 2025/2026 game code szn
league_id_mcc = '327284'
league_id_fam = '421341'
league_id_waady = '693038'
app_id = '0LBIMXKi'
guid = '2ZDRVVB4GHG73J67PSROVL7XSE'

from yfpy.query import YahooFantasySportsQuery

# establish connection to server
try:
    query = YahooFantasySportsQuery(
        league_id_mcc,
        game_code,
        game_key,
        env_file_location=Path("Yahoo-Fantasy-Football-Tracker/.")
        # yahoo_consumer_key=YAHOO_CONSUMER_KEY,
        # yahoo_consumer_secret=YAHOO_CONSUMER_SECRET,
    )

finally:
    print("Successfully queried!")
    # do oAuth2 stuff
    query.save_access_token_data_to_env_file(env_file_location=Path("."))
    # print(query.get_current_game_info())
    # print(query.get_league_players(player_count_limit=20, player_count_start=0))
    # print(query.get_user_leagues_by_game_key(game_key)

    teams_json = (query.get_league_teams())
    print(teams_json)
    query2 = YahooFantasySportsQuery(
        league_id_mcc,
        game_code,
        game_key,
        env_file_location=Path(".")
        # yahoo_consumer_key=YAHOO_CONSUMER_KEY,
        # yahoo_consumer_secret=YAHOO_CONSUMER_SECRET,
    )
    teamsw_json = (query.get_league_standings())
    print(teamsw_json)
    owners = set()
try:
    """
    for item in teams_json:
        match = re.search(r'Team\((\{.*\})\)', item)
        if match:
            json_str = match.group(1)
            team_info = json.loads(json_str)
            owners.add(team_info["nickname"])
            print('adding nickname ' + team_info["nickname"])

            clinched_values = set()


    print(type(teams_json[0]))
    print(dir(teams_json[0]))
    print(vars(teams_json[0]))
    """
    # compile sets derived from json data
    for team in teams_json:
        m_info = team.managers[0].nickname
        owners.add(m_info)
finally:
    print(owners)
    print("do nothing")
"""
461 - 2025
449 - 2024
423 - 2023
414- 2022

to do: query by seasons using game code and season code and parse data

"""
seasons = (461, 449, 423, 414)
seasonsN = (2025, 2024, 2023, 2022)
for seasonNum in seasonsN:
    print("DEBUG")
    print("DEBUG2")
    queryZ = YahooFantasySportsQuery(
        league_id_mcc,
        game_code,
        seasons[0],
        env_file_location=Path(".")
    )
    print(queryZ.get_league_teams())

"""
    it = 0
    #dynamicLeagueId = query.get_league_key(seasonNum)
    print('DEBUG:' + league_id_waady)
    dynamicGameKey = query.get_game_key_by_season(seasonNum)
    print('DEBUG:' + dynamicGameKey)
    query2 = YahooFantasySportsQuery(
        league_id_waady, #queried specific key by year from initial queried league
        game_code,
        seasons[0],  # Adjust for season
        #env_file_location=Path(".")
    )
    print(query2.get_league_teams())
    it=it+1
"""

"""
from collections import defaultdict
owner_stats = defaultdict(lambda: {
    "total_wins": 0,
    "total_losses": 0,
    "total_points": 0,
    "seasons_played": 0,
    "nicknames": set(),
    "team_names": set(),
})
suffix = '.l.327284'
oauth_session = query.oauth
print(oauth_session)


for season in seasons:
    key = f'{season}{suffix}'
    print(key)
    sznQuery = YahooFantasySportsQuery(oauth_session, key)
    teams = sznQuery.get_league_teams()



    for team in standings:
        manager = team.managers[0]  # assuming one manager per team
        manager_id = manager.guid  # or manager.manager_id if you prefer

        # Aggregate
        stats = owner_stats[manager_id]
        stats["total_wins"] += getattr(team, "wins", 0)
        stats["total_losses"] += getattr(team, "losses", 0)
        stats["total_points"] += getattr(team, "points_for", 0)
        stats["seasons_played"] += 1
        stats["nicknames"].add(manager.nickname)
        stats["team_names"].add(team.name.decode() if isinstance(team.name, bytes) else team.name)


for season in seasons:
    league_key = f"{league_id}{league_suffix}"
    query = YahooFantasySportsQuery(ysession, league_key=league_key)
    teams = query.get_league_teams()

    for team in teams:
        manager = team.managers[0]  # assuming 1 manager per team
        manager_id = manager.guid

        stats = owner_stats[manager_id]
        stats["total_wins"] += getattr(team, "wins", 0)
        stats["total_losses"] += getattr(team, "losses", 0)
        stats["total_points"] += getattr(team, "points_for", 0)
        stats["seasons_played"] += 1
        stats["nicknames"].add(manager.nickname)
        stats["team_names"].add(team.name.decode() if isinstance(team.name, bytes) else team.name)

# Print results
for guid, stats in owner_stats.items():
    print(f"Manager {guid}")
    print(f"  Seasons: {stats['seasons_played']}")
    print(f"  Wins: {stats['total_wins']}")
    print(f"  Losses: {stats['total_losses']}")
    print(f"  Points For: {stats['total_points']}")
    print(f"  Nicknames: {', '.join(stats['nicknames'])}")
    print(f"  Team Names: {', '.join(stats['team_names'])}")
    print()
 """