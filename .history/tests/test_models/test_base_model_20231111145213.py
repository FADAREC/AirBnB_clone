import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_initialization(self):
        # Test initialization with default values
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

        # Test initialization with custom values
        custom_model = BaseModel(id='custom_id', created_at='2023-01-01T12:00:00.000000', updated_at='2023-01-01T12:00:00.000000')
        self.assertEqual(custom_model.id, 'custom_id')
        self.assertEqual(str(custom_model.created_at), '2023-01-01 12:00:00')
        self.assertEqual(str(custom_model.updated_at), '2023-01-01 12:00:00')


        

    # Add more test methods for other functionalities

if __name__ == '__main__':
    unittest.main()
