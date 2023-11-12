#!usr/bin/python3
"""Definition of the BaseModel class."""
import uuid
from datetime import datetime
import models

class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel class.

        Args:
            self (BaseModel): the current instance
            args (any): not used here
            kwargs (dict): dictionary of key/value pairs attributes
        """
        # public instance attributes
        self.id = str(uuid.uuid4())  # Generate a unique identifier for the instance
        self.created_at = datetime.today()  # Set the creation timestamp to the current date and time
        self.updated_at = datetime.today()  # Set the update timestamp to the current date and time

        if len(kwargs):
            iso_format = "%Y-%m-%dT%H:%M:%S.%f"
            # If keyword arguments are provided during initialization
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    # If the key is 'created_at' or 'updated_at', convert the value to a datetime object
                    self.__dict__[key] = datetime.strptime(value, iso_format)
                else:
                    # Otherwise, set the attribute with the provided value
                    self.__dict__[key] = value
        else:
            # If no keyword arguments are provided, add the instance to the storage
            models.storage.new(self)

    # public instance methods
    def save(self):
        """Updates the public instance attribute updated_at \
            with the current datetime."""
        self.updated_at = datetime.today()  # Update the 'updated_at' attribute with the current date and time
        models.storage.save()  # Save the changes to storage

    def to_dict(self):
        """Returns a dictionary containing all \
            keys/values of __dict__ of the instance."""
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()  # Convert 'created_at' to ISO format
        dict_copy["updated_at"] = self.updated_at.isoformat()  # Convert 'updated_at' to ISO format
        dict_copy["__class__"] = self.__class__.__name__  # Add the class name to the dictionary

        return dict_copy  # Return the dictionary representation of the instance

    def __str__(self):
        """Return the string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"  # Return a formatted string representation
