#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    The BaseModel class represents the base model for your application.

    Attributes:
        - id (str): A unique identifier generated using uuid4.
        - created_at (datetime): The datetime when the instance is created.
        - updated_at (datetime): The datetime when the instance is last updated.

    Methods:
        - __init__: Initializes a new instance of the BaseModel class.
        - __str__: Returns a string representation of the instance.
        - save: Updates the 'updated_at' attribute to the current datetime.
        - to_dict: Converts the instance to a dictionary for serialization.
    """

    # Define a macro for the date format
    DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        If no keyword arguments are provided, it generates a new unique ID,
        sets the 'created_at' and 'updated_at' attributes to the current datetime.

        If keyword arguments are provided, it sets the 'id' attribute to the provided
        value or generates a new ID if not provided. It also sets 'created_at' and
        'updated_at' attributes based on the provided values or to the current datetime.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            self.id = kwargs.get('id', str(uuid4()))
            self.created_at = (
                datetime.strptime(kwargs.get('created_at'), self.DATE_TIME_FORMAT)
                if 'created_at' in kwargs
                else datetime.utcnow()
            )
            self.updated_at = (
                datetime.strptime(kwargs.get('updated_at'), self.DATE_TIME_FORMAT)
                if 'updated_at' in kwargs
                else datetime.utcnow()
            )

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Example:
        [BaseModel] (45f0eab5-3312-4b84-95f6-7ca3a0a5496d)
        {'id': '45f0eab5-3312-4b84-95f6-7ca3a0a5496d',
         'created_at': datetime.datetime(2023, 11, 11, 11, 38, 10, 164618),
         'updated_at': datetime.datetime(2023, 11, 11, 11, 38, 10, 164664),
         'name': 'My First Model', 'my_number': 89}
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute to the current datetime.
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Converts the instance to a dictionary for serialization.

        Returns:
            dict: A dictionary representation of the instance.
        """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.strftime(self.DATE_TIME_FORMAT)
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects