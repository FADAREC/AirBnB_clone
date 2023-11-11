#!/bin/usr/python3
"""
Init for models module
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()