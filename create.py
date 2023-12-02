import os
from datetime import datetime

def create_solution_template(year, day, author="Michele"):
    base_dir = os.getcwd()
    day_dir = f"{base_dir}/{year}/day{str(day).zfill(2)}"
    os.makedirs(day_dir, exist_ok=True)

    solution_template = f"""\"\"\"
Advent of Code {year}
Day {day}
Author: {author}
\"\"\"
# Your solution here

def process_input():
    inp = open(0, encoding='utf-8 ').read().splitlines()
    # code
    pass
    
if __name__ == "__main__":
    # Read input
    input_data = input()

    # Process and output result
    print("Solution:", process_input())

"""

    with open(os.path.join(day_dir, "solution.py"), "w", encoding="utf-8") as f:
        f.write(solution_template)

    open(os.path.join(day_dir, "in.txt"), "w", encoding="utf-8").close()
    
    open(os.path.join(day_dir, "test.txt"), "w", encoding="utf-8").close()

if __name__ == "__main__":
    year = datetime.now().year
    day = int(input("Enter the day: "))
    create_solution_template(year, day)
