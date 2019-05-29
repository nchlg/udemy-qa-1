from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
	def test_create_blog(self):
		b = Blog('Test', 'Test Author')

		self.assertEqual('Test', b.title)
		self.assertEqual('Test Author', b.author)
		self.assertEqual([], b.posts)

	def test_repr(self):
		b = Blog('Test', 'Test Author')
		b2 = Blog('My Day', 'Rolf')
		b3 = Blog('My Posts', 'Dale')
		b3.create_post('Post 1', 'My first post!')

		self.assertEqual('Test by Test Author (0 posts)', b.__repr__())
		self.assertEqual('My Day by Rolf (0 posts)', b2.__repr__())
		self.assertEqual('My Posts by Dale (1 post)', b3.__repr__())

