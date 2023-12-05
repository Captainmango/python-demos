from src.bookings.bookable import Bookable
from src.bookings.strategies import *

class TestBooking:
    def handle() -> None:
        print("Hello, World. This was a test.")


def process_booking(bookable: Bookable):
    bookable.handle()

strategy = TestBooking
process_booking(strategy)