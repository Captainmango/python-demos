from src.bookings.bookable import Bookable


class PreBook(Bookable):
    def __init__(self, amount) -> None:
        self._amount = amount

    def handle(self) -> None:
        print("This is a prebook booking")
        PreBook._take_payment(self._amount)
        print("Booking placed successfully")


class PayOnArrival(Bookable):
    def __init__(self, amount) -> None:
        self._amount = amount

    def handle(self) -> None:
        print("This is a pay on arrival booking")
        PayOnArrival._take_payment(self.amount)
        print("Booking successful. Enjoy your stay.")


class PayOnExit(Bookable):
    def __init__(self, amount: int, time: int) -> None:
        self._amount = amount
        self._time = time

    def handle(self) -> None:
        print("This is a pay on exit booking")
        PayOnExit._take_payment_on_exit(amount=self._amount, time=self._time)
        print("Thanks for parking with us!")
        
    def _take_payment_on_exit(amount: int, time: int) -> None:
        print(f"Taking payment for {time} hour(s).")
        PayOnExit._take_payment(amount)

