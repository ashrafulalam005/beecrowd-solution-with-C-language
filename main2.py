import os
from datetime import datetime

def makeCommitsOnDate(date_str: str, commits_per_day: int):
    # Parse the specific date
    try:
        specific_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return
    
    # Format the date for the commit message and commit date
    formatted_date = specific_date.strftime("%Y-%m-%d %H:%M:%S")

    for _ in range(commits_per_day):
        # Create an empty commit with the specified date
        os.system(f'git commit --allow-empty --date="{formatted_date}" -m "Commit for {formatted_date}"')

    os.system('git push')

# Call the function with the desired date and commits per day
makeCommitsOnDate("2024-01-01", 100)  # For creating n commits on date




