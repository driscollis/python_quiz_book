# 70_list_insanity.py

snakes = ["Python", "Garter", "Anaconda"]

def add_snake(snake_type):
    snakes.extend(snake_type)
    print(snakes)
    
add_snake("Boa")