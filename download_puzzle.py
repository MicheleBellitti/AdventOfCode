import requests
import os
import sys
from datetime import datetime


def download_input(year, day):
    session_cookie = os.getenv("AOC_SESSION")
    if not session_cookie:
        raise ValueError("Session cookie not set in environment variables")

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session_cookie}
    response = requests.get(url, cookies=cookies, timeout=10)

    if response.status_code == 200:
        base_dir = os.getcwd()
        with open(f"{base_dir}/{year}/day{str(day).zfill(2)}/in.txt", "w") as file:
            file.write(response.text)
    else:
        print(
            f"Failed to download input for year {year}, day {day}: {response.status_code}"
        )


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        year, day = int(sys.argv[1]), int(sys.argv[2])
    else:
        # get them from the current date
        year, day = datetime.now().year, datetime.now().day
        
    
    download_input(year, day)
