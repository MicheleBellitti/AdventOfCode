from datetime import datetime
from create import create_solution_template  # Import the function
# from setuptools import setup, find_packages

def setup_year(year):
    for day in range(9, 26):
        create_solution_template(year, day)


if __name__ == "__main__":
    year = datetime.now().year
    setup_year(year)
    # setup(name="utils", version="0.1", packages=find_packages())
