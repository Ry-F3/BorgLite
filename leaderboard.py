import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("borglite_rank")

worksheet = SHEET.worksheet("leaderboard")

# Function to update the leaderboard
def update_leaderboard(player):
    leaderboard_data = worksheet.get_all_values()
    headers = leaderboard_data[0]  # Extract headers
    
    # Extract the scores from the leaderboard data
    scores = [int(row[3]) for row in leaderboard_data[1:]]  # Assuming scores are in the 4th column
    
    # Calculate the rank based on the scores
    rank = sum(score > player.score for score in scores) + 1
    
    # Update the player's rank
    player.rank = rank
    
    # Add the player data to the leaderboard
    player_data = [player.rank, player.name, player.level, player.score]
    leaderboard_data.append(player_data)
    
    # Sort the leaderboard data based on the scores in descending order
    leaderboard_data[1:] = sorted(leaderboard_data[1:], key=lambda row: int(row[3]), reverse=True)  # Assuming scores are in the 4th column
    
    # Insert the headers back to the sorted data
    leaderboard_data[0] = headers
    
    # Write the leaderboard data to the sheet starting from cell A1
    worksheet.update('A1', leaderboard_data)

    
