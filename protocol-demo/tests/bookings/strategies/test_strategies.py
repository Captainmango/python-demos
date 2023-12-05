from src.bookings.strategies import *
from tests.helpers import validate_strategy_has_handle_method

class TestStrategies():
    def test_prebook_implements_bookable(self):
        strategy = PreBook(amount=17)
        validate_strategy_has_handle_method(strategy)
    
    def test_pay_on_arrival_implements_bookable(self):
        strategy = PayOnArrival(amount=17)
        validate_strategy_has_handle_method(strategy)

    def test_pay_on_exit_implements_bookable(self):
        strategy = PayOnExit
        validate_strategy_has_handle_method(strategy)

