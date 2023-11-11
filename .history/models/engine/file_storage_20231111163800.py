#!/usr/bin/python3
"""
imports
"""
import json
"""
define a class
"""
class FileStorage:
    # Define the path
    __file_path = 'file.json'
  
    __objects  = {}
    # returns all objects
    """
    The functions return all objects
    """
    def all(self):
        return FileStorage.__objects
    
    def new(self, new_object):
        obj_key = "{}.{}".format(new_object.__class__.__name__, new_object.id)
        FileStorage.__objects[obj_key] = new_object
        self.save()

    def save(self):
        convert_json = {}

        for obj_key, obj in FileStorage.__objects.items():
            convert_json[obj_key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(convert_json, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_instance = eval(class_name)(**value)
                    FileStorage.__objects[key] = class_instance
        except FileNotFoundError:
            pass
