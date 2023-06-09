import gspread
from google.oauth2.service_account import Credentials  # Google Api
from tabulate import tabulate  # Table module

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json") 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("borglite_rank")

worksheet = SHEET.worksheet("leaderboard")  # Code above has been taken from the demo project

def update_leaderboard(player):
    """
    Update the leaderboard with the player's rank, name, level and score.
    """
    leaderboard_data = worksheet.get_all_values()
    headers = leaderboard_data[0]  # Extract headers

    # Extract the scores from the leaderboard data
    scores = [int(row[3]) for row in leaderboard_data[1:]]  # Assuming scores are in the 4th column of the spreadsheet
    ranks = [int(row[0]) for row in leaderboard_data[1:]]   # Assuming ranks are in the 1st column of the spreadsheet

    # Calculate the rank based on the scores
    rank = sum(score > player.score for score in scores) + 1

    # Update the player's rank
    player.rank = rank

    for i, row in enumerate(leaderboard_data[1:], start=1):
        if ranks[i-1] > rank or (ranks[i-1] == rank and int(row[3]) > player.score):
            row[0] = str(ranks[i-1] + 1)  # Increment the rank by 1
        elif ranks[i-1] == rank and int(row[3]) == player.score:
            rank -= 1  # Decrement the rank by 1 for subsequent entries with the same score
            row[0] = str(rank)  # Update the rank for the current entry
        else:
            break

    # Check if the player's score already exists in the leaderboard
    existing_entry_index = next((i for i, row in enumerate(leaderboard_data[1:], start=1) if int(row[3]) == player.score), None)

    if existing_entry_index is not None:
        # Update the existing entry
        leaderboard_data[existing_entry_index] = [player.rank, player.name, player.level, player.score]
    elif player.score != 0:
        # Add the player data as a new entry if the score is not 0
        new_entry = [player.rank, player.name, player.level, player.score]
        leaderboard_data.insert(rank, new_entry)

        # Update the ranks after the current player's rank
        for i, row in enumerate(leaderboard_data[rank+1:], start=rank+1):
            row[0] = str(int(row[0]) + 1)

    # Sort the leaderboard data based on the scores in descending order
    leaderboard_data[1:] = sorted(leaderboard_data[1:], key=lambda row: int(row[3]), reverse=True)  # Assuming scores are in the 4th column of the spreadsheet

    # Update the ranks based on the sorted order
    for i, row in enumerate(leaderboard_data[1:], start=1):
        row[0] = str(i)

    # Insert the headers back to the sorted data
    leaderboard_data[0] = headers

    # Write the leaderboard data to the sheet starting from cell A1
    worksheet.update('A1', leaderboard_data)

def display_leaderboard(player):
    """
    Display the leaderboard if te player selects to see it using the game interface.
    """
    leaderboard_data = worksheet.get_all_values()
    # Display the leaderboard data in a table
    headers = leaderboard_data[0]  # Show the headers
    table_data = leaderboard_data[1:11]  # Exclude the headers from the table data and show the top 10 scores, but the api will store all of the data

    print(f"\n{tabulate(table_data, headers=headers)}")

    
