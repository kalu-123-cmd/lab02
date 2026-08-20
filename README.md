# Lab 2 Test Design Report

**Course:** Software Testing and Validation  
**Institution:** Addis Ababa University  
**Unit:** Unit 2  
**Project:** Test Design Techniques

**Report status:** Complete  
**Verification date:** 20 August 2026

## 1. Executive Summary

This laboratory exercise applies black-box and white-box test design
techniques to a small Python codebase. The test suite covers ticket pricing,
customer discounts, member bonuses, and a turnstile state machine.

The final test run produced **16 passing tests**. The bonus branch test was
corrected to call the implemented function `bonus`.

## 2. Objectives

The exercise demonstrates how to:

- Divide input data into equivalence partitions.
- Test valid and invalid boundary values.
- Derive test cases from a decision table.
- Reach branch coverage for a small function.
- Verify valid and ignored state transitions.

## 3. System Under Test

### 3.1 Ticket Pricing

Function: `src.pricing.ticket_price(age)`

| Input partition | Expected result |
|---|---:|
| Age below 0 | `ValueError` |
| Age 0 to 12 | 50 birr |
| Age 13 to 64 | 100 birr |
| Age 65 to 120 | 60 birr |
| Age above 120 | `ValueError` |

### 3.2 Discount Calculation

Function: `src.pricing.discount(is_member, order_total)`

| Member | Order total | Discount |
|---|---:|---:|
| Yes | 1000 or more | 15% |
| Yes | Less than 1000 | 10% |
| No | 1000 or more | 5% |
| No | Less than 1000 | 0% |

Negative order totals are rejected with `ValueError`.

### 3.3 Bonus Calculation

Function: `src.scoring.bonus(score, is_member)`

- Scores above 90 receive a 100-point bonus.
- Members receive an additional 50 points.
- The branch tests target the high-score/member and low-score/non-member paths.

### 3.4 Turnstile State Machine

Class: `src.turnstile.Turnstile`

The initial state is `locked`.

| Current state | Event | Next state |
|---|---|---|
| `locked` | `coin` | `unlocked` |
| `unlocked` | `push` | `locked` |
| `locked` | `push` | `locked` |
| `unlocked` | `coin` | `unlocked` |

The last two rows verify that invalid events are ignored.

## 4. Test Design Summary

The test suite in `tests/test_starter.py` contains:

- Equivalence partition tests for child, adult, senior, and invalid ages.
- Boundary tests for ages `-1`, `0`, `12`, `13`, `64`, `65`, `120`, and `121`.
- Four decision-table tests for membership and order size combinations.
- Branch tests for the `bonus` function.
- Tests for both valid and ignored turnstile events.

### Methodology summary

| Part | Technique | Main target | Result |
|---|---|---|---|
| A | Equivalence partitioning | Ticket-price input classes | Passed |
| B | Boundary value analysis | Ticket-price band edges | Passed |
| C | Decision table testing | Membership and order-total rules | Passed |
| D | Branch coverage | `bonus` decision branches | Passed |
| E | State transition testing | Turnstile events and states | Passed |

## 5. Execution Evidence

### Test command

```text
.\.venv\Scripts\python.exe -m pytest -q
```

### Result

```text
16 passed
```

### Test result

The high-score member case now calls `bonus(95, True)` and returns the
expected result of `150`.

## 6. Coverage Measurement

Run the following command to measure branch and line coverage:

```text
.\.venv\Scripts\python.exe -m pytest --cov=src --cov-report=term-missing
```

### Final coverage result

The verified run reports:

| Module | Coverage | Missing |
|---|---:|---|
| `src/pricing.py` | 94% | Negative `order_total` validation path |
| `src/scoring.py` | 100% | None |
| `src/turnstile.py` | 100% | None |
| **Total** | **97%** | 1 line |

The only uncovered line is the negative `order_total` validation path in
`src/pricing.py`.

## 7. Submission Status

- [x] Test suite executes successfully.
- [x] Equivalence partitioning tests completed.
- [x] Boundary value tests completed.
- [x] Decision table tests completed.
- [x] Branch coverage tests completed.
- [x] State transition tests completed.
- [x] Coverage results recorded.

## 8. Conclusion

The lab successfully demonstrates the required test design techniques and
contains broad coverage of the implemented behavior. All 16 tests pass, and
the final total coverage is 97%. No defect was observed in the application
functions during the executed tests.
