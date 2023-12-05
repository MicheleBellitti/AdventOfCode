import os
from datetime import datetime
from aocd import get_data, submit

def create_solution_template(year, day, author="Michele"):
    base_dir = os.getcwd()
    day_dir = f"{base_dir}/{year}/day{str(day).zfill(2)}"
    os.makedirs(day_dir, exist_ok=True)

    solution_template = f"""\"\"\"
Advent of Code {year}
Day {day}
Author: {author}
\"\"\"
import os
from datetime import datetime
from aocd import get_data, submit

# Solution here

def p1(inp):
    pass
def p2(inp):
    pass
    

def process_input(year, day):
    inp = open(0, encoding='utf-8').read()
    # inp = get_data(day=day, year=year)
    print(inp)
    
    # code
    p_1, p_2 = p1(inp), p2(inp)
    submit(p_1, part='a', day=day, year=year)
    
    return p_1, p_2
    
if __name__ == "__main__":
    
    y = datetime.now().year
    d = int(input("Enter the day: "))
    
    # Process and output result
    print("Solution:", process_input(y, d))

"""

    with open(os.path.join(day_dir, "solution.py"), "w", encoding="utf-8") as f:
        f.write(solution_template)

    open(os.path.join(day_dir, "in.txt"), "w", encoding="utf-8").close()
    
    open(os.path.join(day_dir, "test.txt"), "w", encoding="utf-8").close()

if __name__ == "__main__":
    year = datetime.now().year
    day = int(input("Enter the day: "))
    create_solution_template(year, day)
