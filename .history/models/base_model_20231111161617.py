#!/usr/bin/python3
"""
Import modules
"""
from uuid import uuid4
from datetime import datetime
from models.engine.file_storage import FileStorage
"""
Define a the base model class
"""
class BaseModel:
    """
    define a macro for the date format
    """
    DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
    """
    define class constructor
    """
    def __init__(self, *args, **kwargs):
        
        # if not kwargs or "__class__" not in kwargs
        FileStorage.new(self)
        
 
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
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.utcnow()
        storage.save(self)

    @staticmethod
    def to_dict(obj):
        map_objects = {}
        for key, value in obj.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                map_objects[key] = value
        map_objects["__class__"] = obj.__class__.__name__
        return map_objects
