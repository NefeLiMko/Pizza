import sys


def valid_args(args):
    args_count = len(args)
    # Validating amount of args
    if args_count < 3:
        exit("Missing arguments. Example : 'pizzabot.py 5x5 (1,3)'")


def valid_grid(size):
    # Splitting grid
    grid = size.lower().split("x")

    # Validating grid format
    if len(grid) != 2:
        exit(f"\n{size} is not valid. Example : '1x3'")

    # Trying to convert to int. Fail if it's empty or non-numeric
    try:
        x_cord = int(grid[0])
        y_cord = int(grid[1])
    except ValueError:
        exit(f"\n{size} is not valid. Grid can't be empty or non-numeric. Example : '1x3'")

    # Validating grid size. Must be positive.
    if x_cord <= 0 or y_cord <= 0:
        exit(f"\n{size} is not valid. Grid size must be positive. Example : '1,3'")


def valid_locations(size, locations):
    x_grid = int(size.lower().split("x")[0])
    y_grid = int(size.lower().split("x")[1])

    # Validating locations
    for location in locations:
        location = location.strip("''")
        if not (location[0] == "(" and location[len(location) - 1] == ")"):
            exit(f"\n{location} is not surrounded with brackets. Example : '(1,3)'")

        try:
            # Check the number of provided cords
            if len(location.strip("()").split(",")) < 2:
                exit(f"\n{location} is not valid. Number of cords can't be less than 2. Example : '(1,3)'")
            # Trying to convert to int. Fail if it's empty or non-numeric
            current_x_cord = int(location.strip("()").split(",")[0])
            current_y_cord = int(location.strip("()").split(",")[1])
        except ValueError:
            exit(f"\n{location} is not valid. Cords can't' be empty or non-numeric. Example '(1,3)'")
        # Validating grid size
        if current_x_cord < 0 or current_y_cord < 0:
            exit(f"\n{location} is not valid. Delivery location cannot be negative. Example '(1,3)'")
        # Check if location is inside delivery area
        if current_x_cord > x_grid or current_y_cord > y_grid:
            exit(f"\n{location} is not in delivery area.")


def delivery(locations):
    delivery_list = [[0, 0]]
    x = 0
    entire_way = ""

    for location in locations:
        current_x_cord = int(location.strip("()").split(",")[0])
        current_y_cord = int(location.strip("()").split(",")[1])
        delivery_list.append([current_x_cord, current_y_cord])

    for place in delivery_list[1::]:
        previous_cord = delivery_list[x]
        # Calculating X-moves
        x_move = previous_cord[0] - place[0]
        while x_move < 0:
            entire_way += "E"
            x_move += 1
        while x_move > 0:
            entire_way += "W"
            x_move -= 1
        # Calculating Y-moves
        y_move = previous_cord[1] - place[1]
        while y_move < 0:
            entire_way += "N"
            y_move += 1
        while y_move > 0:
            entire_way += "S"
            y_move -= 1
        if x_move == 0 and y_move == 0:
            entire_way += "D"
        x = x + 1
    return entire_way


if __name__ == "__main__":
    # Validating inputs
    valid_args(sys.argv)
    valid_grid(sys.argv[1])
    valid_locations(sys.argv[1], sys.argv[2:])
    # Delivery
    print(delivery(sys.argv[2:]))