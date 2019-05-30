from models.item import ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
	def test_crud(self):
		with self.app_context():
			item = ItemModel('test', 19.99)
			
			# Make sure it is not inserted on the DB
			self.assertIsNone(ItemModel.find_by_name('test'),
				f'Found an item with name {item.name}, but expected not to.')
			item.save_to_db()
			self.assertIsNotNone(ItemModel.find_by_name('test'),
				f'{item.name} not inserted.')
			# Delete it from DB
			item.delete_from_db()
			self.assertIsNone(ItemModel.find_by_name('test'),
				f'{item.name} not deleted.')

