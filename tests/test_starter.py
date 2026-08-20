"""Starter tests for Lab 2: Test Design Techniques.

Complete each TODO, then run from the project root with:

    pytest -v

For Part D you will also measure coverage with:

    pytest --cov=src --cov-report=term-missing
"""

import pytest

from src.pricing import ticket_price, discount
from src.scoring import bonus
from src.turnstile import Turnstile


# ---------------------------------------------------------------------------
# Part A. Equivalence partitioning for ticket_price.
# There are five partitions: age < 0 (invalid), 0 to 12 (child),
# 13 to 64 (adult), 65 to 120 (senior), age > 120 (invalid).
# One valid partition is done for you. Add the others.
# ---------------------------------------------------------------------------
def test_ticket_price_child_partition():
    assert ticket_price(8) == 50


def test_ticket_price_adult_partition():
    assert ticket_price(30) == 100


def test_ticket_price_senior_partition():
    assert ticket_price(70) == 60


def test_ticket_price_invalid_ages_raise_value_error():
    with pytest.raises(ValueError):
        ticket_price(-1)
    with pytest.raises(ValueError):
        ticket_price(121)


# ---------------------------------------------------------------------------
# Part B. Boundary value analysis for ticket_price.
# Test the values on and just beside each band edge: 0, 12, 13, 64, 65, 120,
# and the invalid neighbours -1 and 121.
# ---------------------------------------------------------------------------
def test_ticket_price_lower_boundaries():
    assert ticket_price(0) == 50
    assert ticket_price(12) == 50
    assert ticket_price(13) == 100
    assert ticket_price(64) == 100
    assert ticket_price(65) == 60
    assert ticket_price(120) == 60


def test_ticket_price_invalid_boundary_neighbours_raise_value_error():
    with pytest.raises(ValueError):
        ticket_price(-1)
    with pytest.raises(ValueError):
        ticket_price(121)


# ---------------------------------------------------------------------------
# Part C. Decision table for discount.
# Conditions: is_member (Y/N) and order_total >= 1000 (Y/N).
# Four rules, so four tests. One is done for you.
# ---------------------------------------------------------------------------
def test_discount_member_large_order():
    assert discount(True, 1500) == 15


def test_discount_member_small_order():
    assert discount(True, 500) == 10


def test_discount_non_member_large_order():
    assert discount(False, 1500) == 5


def test_discount_non_member_small_order():
    assert discount(False, 500) == 0


# ---------------------------------------------------------------------------
# Part D. Branch coverage for bonus.
# Write the smallest set of tests that reaches 100% BRANCH coverage.
# Then run:  pytest --cov=src --cov-report=term-missing
# and confirm src/scoring.py reports no missing branches.
# ---------------------------------------------------------------------------
def test_bonus_high_score_member():
    assert bonus(95, True) == 150


def test_bonus_low_score_non_member():
    assert bonus(50, False) == 0


# ---------------------------------------------------------------------------
# Part E. State transition testing for Turnstile.
# Test the two valid transitions and the two ignored events.
# One valid transition is done for you.
# ---------------------------------------------------------------------------
def test_turnstile_coin_unlocks():
    t = Turnstile()
    t.coin()
    assert t.state == "unlocked"


def test_turnstile_push_locks_when_unlocked():
    t = Turnstile()
    t.coin()
    t.push()
    assert t.state == "locked"


def test_turnstile_push_ignored_when_locked():
    t = Turnstile()
    t.push()
    assert t.state == "locked"


def test_turnstile_coin_ignored_when_unlocked():
    t = Turnstile()
    t.coin()
    t.coin()
    assert t.state == "unlocked"
