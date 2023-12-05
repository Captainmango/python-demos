from src.bookings.bookable import Bookable


def validate_strategy_has_handle_method(strategy: Bookable):
    try:
        strategy.handle
    except NotImplemented as ex:
        assert False, f"Bookable protocol is not implemented for {strategy.__class__} raised {ex}"