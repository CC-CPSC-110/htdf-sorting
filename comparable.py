"""Demonstration of comparison."""
from typing import List
from typing_extensions import Self
from cs110 import expect, summarize
from dataclasses import dataclass
from gtfs import Range

@dataclass
class Latitude(Range):
    """Class to validate and normalize the latitude value."""
    lat: float

    def __init__(self, lat: float) -> None:
        self.lat = self.normalize(lat)

    def normalize(self, lat: float) -> float:
        """Normalize latitude with reflection across poles."""
        if lat > 90:
            return 90 - (lat - 90)
        elif lat < -90:
            return -90 - (lat + 90)
        return lat

    def __add__(self, other: Self) -> Self:
        """Add Latitudes."""
        return Latitude(self.normalize(self.lat + other.lat))

    def __sub__(self, other: Self) -> Self:
        """Subtract Latitudes."""
        return Latitude(self.normalize(self.lat - other.lat))

    def __abs__(self) -> float:
        """Returns the absolute value of the latitude."""
        return abs(self.lat)
    
    def __eq__(self, other: Self) -> bool:
        """Check if Latitudes are equal."""
        return self.lat == other.lat

    def __lt__(self, other: Self) -> bool:
        """Check if this Latitude is less than other."""
        return self.lat < other.lat

    def __gt__(self, other: Self) -> bool:
        """Check if this Latitude is greater than other."""
        return self.lat > other.lat

    def __le__(self, other: Self) -> bool:
        """Check if this Latitude is less than or equal to other."""
        return self.lat <= other.lat

    def __ge__(self, other: Self) -> bool:
        """Check if this Latitude is greater than or to other."""
        return self.lat >= other.lat

