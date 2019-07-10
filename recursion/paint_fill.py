def get_neighbours(area: list, x: int, y: int) -> list:
    height = len(area)
    width = len(area[0])
    result = []

    if x > 0:
        result.append((x - 1, y))
    if y > 0:
        result.append((x, y - 1))
    if x < height - 1:
        result.append((x + 1, y))
    if y < width - 1:
        result.append((x, y + 1))
    return result


def recursive_fill(area: list, x: int, y: int, new_color: int, original_color: int):
    if area[x][y] != original_color:
        return

    area[x][y] = new_color
    for x_, y_ in get_neighbours(area, x, y):
        recursive_fill(area, x_, y_, new_color, original_color)


def paint_fill(area: list, x: int, y: int, new_color: int):
    original_color = area[x][y]
    recursive_fill(area, x, y, new_color, original_color)
