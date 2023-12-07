from src.bookings.strategies import *
from tests.helpers import validate_strategy_is_bookable

class TestStrategies():
    def test_prebook_implements_bookable(self):
        strategy = PreBook(amount=17)
        validate_strategy_is_bookable(strategy)
    
    def test_pay_on_arrival_implements_bookable(self):
        strategy = PayOnArrival(amount=17)
        validate_strategy_is_bookable(strategy)

    def test_pay_on_exit_implements_bookable(self):
        strategy = PayOnExit(amount=17, time=3)
        validate_strategy_is_bookable(strategy)

    def test_booking_implements_bookable(self):
        strategy = TestBooking()
        validate_strategy_is_bookable(strategy)

