# 76_veritable_variables.py

def area(width, height):
    print(f"{width = } {height =}")
    return width * height

if __name__ == "__main__":
    width: int = 10
    height = 15
    area(width, height)