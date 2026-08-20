


def bonus(score: int, is_member: bool) -> int:
 
    b = 0
    if score > 90:
        b = 100
    if is_member:
        b += 50
    return b
