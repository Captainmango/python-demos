from typing import Protocol, runtime_checkable


@runtime_checkable
class Bookable(Protocol):
    def handle(self) -> None:
        raise NotImplemented

    def _take_payment(self, amount: int) -> None:
        print(f"taking payment of ${amount}")
        print("payment taken successfully")

