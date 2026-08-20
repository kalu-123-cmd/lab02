"""Functions under test for Lab 2, part one.

``ticket_price`` is used for equivalence partitioning and boundary
value analysis. ``discount`` is used for decision table testing.
"""


def ticket_price(age: int) -> int:
    """Return the ticket price in birr for a given ``age``.

    Bands: child 0 to 12 costs 50, adult 13 to 64 costs 100, senior
    65 to 120 costs 60. Raises ``ValueError`` for an age below 0 or
    above 120.
    """
    if age < 0 or age > 120:
        raise ValueError("age must be between 0 and 120")
    if age <= 12:
        return 50
    if age <= 64:
        return 100
    return 60


def discount(is_member: bool, order_total: float) -> int:
    """Return the discount percentage for an order.

    A member spending 1000 or more gets 15, a member spending less
    gets 10, a non-member spending 1000 or more gets 5, and everyone
    else gets 0. Raises ``ValueError`` if ``order_total`` is negative.
    """
    if order_total < 0:
        raise ValueError("order_total cannot be negative")
    if is_member and order_total >= 1000:
        return 15
    if is_member:
        return 10
    if order_total >= 1000:
        return 5
    return 0
