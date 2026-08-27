from requests import get
from pprint import PrettyPrinter

PROJECT_NAME = "F1Stats"

BASE_URL = "https://api.jolpi.ca/ergast/f1"

HEADERS = {
    "User-Agent": "F1Stats/1.0"
}

printer = PrettyPrinter()


# Get latest race results
def get_scoreboard():

    url = f"{BASE_URL}/current/last/results.json"

    data = get(url, headers=HEADERS).json()

    races = data["MRData"]["RaceTable"]["Races"]

    if not races:
        print("No race results available.")
        return

    race = races[0]

    print("------------------------------------------")
    print(f"Race: {race['raceName']}")
    print(f"Circuit: {race['Circuit']['circuitName']}")
    print("------------------------------------------")

    for result in race["Results"]:
        driver = result["Driver"]
        constructor = result["Constructor"]

        print(
            f"{result['position']}. "
            f"{driver['givenName']} {driver['familyName']} "
            f"- {constructor['name']} "
            f"- {result['points']} points"
        )


# Get current driver championship standings
def get_stats():

    url = f"{BASE_URL}/current/driverstandings.json"

    data = get(url, headers=HEADERS).json()

    standings = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

    print(f"\n========== {PROJECT_NAME.upper()} DRIVER STANDINGS ==========\n")

    for driver_data in standings:

        position = driver_data["position"]
        driver = driver_data["Driver"]
        constructor = driver_data["Constructors"][0]["name"]
        points = driver_data["points"]
        wins = driver_data["wins"]

        name = f"{driver['givenName']} {driver['familyName']}"

        print(
            f"{position}. {name} | "
            f"{constructor} | "
            f"{points} pts | "
            f"{wins} wins"
        )


# Run driver standings
get_stats()

# Uncomment to see latest race results
# get_scoreboard()