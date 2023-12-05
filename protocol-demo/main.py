from src.bookings.bookable import Bookable
from src.bookings.strategies import *


def process_booking(bookable: Bookable):
    bookable.handle()

strategy = TestBooking()
process_booking(strategy)