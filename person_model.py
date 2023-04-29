from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class NotSameClassInstance(BaseException):
    """Not Same Class Instance"""

@dataclass(frozen=True)
class House(BaseModel):
    number: int

    def __eq__(self, other):
        if not isinstance(other, House):
            raise NotSameClassInstance
        return self.number == other.number

@dataclass(frozen=True)
class Address(BaseModel):
    house: House
    street: str

    def __eq__(self, other):
        if not isinstance(other, Address):
            raise NotSameClassInstance
        return self.house == other.house and self.street == other.street

@dataclass(frozen=True)
class Person(BaseModel):
    name: str
    mobile: int
    address: Address
    city: str
    state: str
    country: str

    def __eq__(self, other):
        if not isinstance(other, Person):
            raise NotSameClassInstance(
                f"unable to compare {type(self)} with {type(other)}"
            )
        return (
            self.name == other.name
            and self.mobile == other.mobile
            and self.address == other.address
            and self.city == other.city
            and self.state == other.state
            and self.country == other.country
        )
