from nba_api.stats.endpoints import playercareerstats
import json

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203998') 

# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]

# json
jsonFile = (career.get_json())

# dictionary
career.get_dict()
import json

# JSON data (replace this with your JSON data)

# Parse the JSON data
parsed_data = json.loads(jsonFile)

# Accessing specific elements
season_totals_regular_season = parsed_data["resultSets"][0]["rowSet"]
career_totals_regular_season = parsed_data["resultSets"][1]["rowSet"]
season_totals_post_season = parsed_data["resultSets"][2]["rowSet"]
career_totals_post_season = parsed_data["resultSets"][3]["rowSet"]

# Example: Printing the first row of "SeasonTotalsRegularSeason" data
print("SeasonTotalsRegularSeason:")
print(season_totals_regular_season[0])

# Example: Printing the first row of "CareerTotalsRegularSeason" data
print("CareerTotalsRegularSeason:")
print(career_totals_regular_season[0])

# Example: Printing the first row of "SeasonTotalsPostSeason" data
print("SeasonTotalsPostSeason:")
print(season_totals_post_season[0])

# Example: Printing the first row of "CareerTotalsPostSeason" data
print("CareerTotalsPostSeason:")
print(career_totals_post_season[0])
