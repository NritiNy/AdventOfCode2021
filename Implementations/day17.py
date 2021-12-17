from typing import List
    
def part1(lines: List[str]):
    input_data = lines[0].split(":")[1]
    x, y = input_data.split(", ")
    x_min, x_max = (int(_x) for _x in x.split("=")[1].split(".."))
    y_min, y_max = (int(_y) for _y in y.split("=")[1].split(".."))

    init_x = []
    for i in range(x_min):
        r = i *(i+1) / 2
        if r >= x_min and r <= x_max:
            init_x.append(i)
        if r > x_max:
            break

    max_y = 0
    for _x in init_x:
        for _y in range(y_min, abs(y_min)):
            hit_target = False
            highest_y = 0

            v_x = _x
            v_y = _y
            x, y = 0, 0
            while y >= y_min and x <= x_max:
                highest_y = max(highest_y, y)
                if x_min <= x <= x_max and y_min <= y <= y_max:
                    hit_target = True

                x += v_x
                y += v_y

                v_y -= 1
                v_x += 1 if v_x < 0 else (-1 if v_x > 0 else 0)

            if hit_target:
                max_y = max(max_y, highest_y)

    return max_y

def part2(lines: List[str]):
    input_data = lines[0].split(":")[1]
    x, y = input_data.split(", ")
    x_min, x_max = (int(_x) for _x in x.split("=")[1].split(".."))
    y_min, y_max = (int(_y) for _y in y.split("=")[1].split(".."))

    counter = 0
    max_y = 0
    for _x in range(x_max + 1):
        for _y in range(y_min, abs(y_min)):
            hit_target = False
            highest_y = 0

            v_x = _x
            v_y = _y
            x, y = 0, 0
            while y >= y_min and x <= x_max:
                highest_y = max(highest_y, y)
                if x_min <= x <= x_max and y_min <= y <= y_max:
                    hit_target = True

                x += v_x
                y += v_y

                v_y -= 1
                v_x += 1 if v_x < 0 else (-1 if v_x > 0 else 0)

            if hit_target:
                max_y = max(max_y, highest_y)
                counter += 1

    return counter