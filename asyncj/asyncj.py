"""
:authors: VengDevs
:licence: Apache License, Version 2.0

:copyright: (c) 2024 VengDevs
"""

from aiofiles import open
from ujson import loads, dumps


class AsyncJson:
    """A class to read and write JSON files asynchronously."""

    def __init__(self, filepath: str) -> None:
        """
        Initialize the class with the file path.

        :param filepath: Path to JSON file.
        """
        self.filepath: str = filepath

    async def read(self) -> dict:
        """Read the JSON file and return a dictionary."""
        async with open(file=self.filepath, mode="r", encoding="utf-8") as file:
            return loads(obj=await file.read())

    async def write(self, data: dict) -> None:
        """
        Write a dictionary to the JSON file.
        
        :param data: Dictionary.
        """
        async with open(file=self.filepath, mode="w", encoding="utf-8") as file:
            await file.write(dumps(obj=data, indent=4))