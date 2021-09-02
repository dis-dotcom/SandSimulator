def can_merge_points(left, right):
    return left.frozen and right.frozen and left.y == right.y and right.x - left.x == 1
