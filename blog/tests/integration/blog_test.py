from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):

	def test_create_post_in_blog(self):
		b = Blog('Title', 'Author')
		b.create_post('Title', 'Content')

		self.assertEqual(len(b.posts), 1)
		self.assertEqual('Title', b.posts[0].title)
		self.assertEqual('Content', b.posts[0].content)

	def test_json(self):
		b = Blog('Title', 'Author')
		b.create_post('Title', 'Content')

		expected = { 
			'title': 'Title', 
			'author': 'Author',
			'posts': [
				{
					'title': 'Title',
					'content': 'Content'
				}
			]
		}

		self.assertEqual(expected, b.json())


	def test_json_no_posts(self):
		b = Blog('Title', 'Author')

		expected = { 
			'title': 'Title', 
			'author': 'Author',
			'posts': []
		}

		self.assertEqual(expected, b.json())