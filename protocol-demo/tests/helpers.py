from src.bookings.bookable import Bookable


def validate_strategy_is_bookable(strategy):
    assert isinstance(strategy, Bookable), f"{strategy.__class__} is not a Bookable"