from src.bookings.bookable import Bookable


class PreBook(Bookable):
    def __init__(self, amount) -> None:
        self._amount = amount

    def handle(self) -> None:
        print("This is a prebook booking")
        self._take_payment(self._amount)
        print("Booking placed successfully")


class PayOnArrival(Bookable):
    def __init__(self, amount) -> None:
        self._amount = amount

    def handle(self) -> None:
        print("This is a pay on arrival booking")
        self._take_payment(self._amount)
        print("Booking successful. Enjoy your stay.")


class PayOnExit(Bookable):
    def __init__(self, amount: int, time: int) -> None:
        self._amount = amount
        self._time = time

    def handle(self) -> None:
        print("This is a pay on exit booking")
        self._take_payment_on_exit(amount=self._amount, time=self._time)
        print("Thanks for parking with us!")
        
    def _take_payment_on_exit(self, amount: int, time: int) -> None:
        print(f"Taking payment for {time} hour(s).")
        self._take_payment(amount)


class TestBooking:
    def handle(self) -> None:
        print("Hello, world. This is a test")
    
    def _take_payment(self, amount: int) -> None:
        ...
