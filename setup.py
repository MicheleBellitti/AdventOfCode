from datetime import datetime
from create import create_solution_template  # Import the function

def setup_year(year):
    for day in range(1, 26):
        create_solution_template(year, day)

if __name__ == "__main__":
    year = datetime.now().year
    setup_year(year)
