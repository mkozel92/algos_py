class Box(object):
    """class representing a box"""
    def __init__(self, h: int, w: int, d: int):
        self.height = h
        self.width = w
        self.depth = d

    def __gt__(self, other):
        return self.height > other.height and \
               self.width > other.width and \
               self.depth > other.depth

    def __lt__(self, other):
        return self.height < other.height and \
               self.width < other.width and \
               self.depth < other.depth


def stack_boxes_rec(boxes: list, bottom_box: int, mem: list) -> int:
    """
    recursive function that tries all possible box stacks
    :param boxes: dimensions of boxes
    :param bottom_box: index of bottom box
    :param mem: memoized results
    :return: height of stack with given box on the bottom
    """
    if mem[bottom_box] != 0:
        return mem[bottom_box]

    height = 0
    for i, box in enumerate(boxes):
        if box < boxes[bottom_box]:
            height = max(height, stack_boxes_rec(boxes, i, mem))

    return height + boxes[bottom_box].height


def stack_boxes(boxes: list):
    """
    return the height of tallest stack that can be build by stacking given boxes
    only strictly smaller box can be put on top of another box
    complexity O(N^2)
    :param boxes: list of dimensions of boxes
    :return: max height
    """
    mem = [0] * len(boxes)
    height = 0
    for i in range(len(boxes)):
        height = max(height, stack_boxes_rec(boxes, i, mem))
    return height
