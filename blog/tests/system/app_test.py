from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

class AppTest(TestCase):

	def setUp(self):
		b = Blog('Test', 'Author')
		app.blogs = {'Test' : b}	


	def test_menu_calls_print_blog(self):
		with patch('app.print_blogs') as mocked_print_blogs:
			with patch('builtins.input') as mocked_input:
				mocked_input.side_effect = ('l', 'q')
				app.menu()
				
				mocked_print_blogs.assert_called()

	def test_print_blogs(self):
		with patch('builtins.print') as mocked_print:
			app.print_blogs()
			mocked_print.assert_called_with('- Test by Author (0 posts)')

	def test_print_menu_prompt(self):
		with patch('builtins.input', return_value='q') as mocked_input:
			app.menu()

			mocked_input.assert_called_with(app.MENU_PROMPT)

	def test_ask_create_blog(self):
		with patch('builtins.input') as mocked_input:
			# Pretends to put these values as input. Returns the first param when the function is called for the first time, the second param when it is called for the second time, etc.
			mocked_input.side_effect = ('Test', 'Author')
			app.ask_create_blog()
			
			self.assertIsNotNone(app.blogs.get('Test'))

	def test_ask_read_blog(self):
		with patch('builtins.input', return_value='Test') as mocked_input:
			with patch('app.print_posts') as mocked_print_posts:
				app.ask_read_blog()

				mocked_print_posts.assert_called_with(app.blogs['Test'])

	def test_print_posts(self):
		b = app.blogs['Test']
		b.create_post('Test Post', 'Test Content')

		expected_print = '''
--- Test Post ---

Test Content

'''
		with patch('builtins.print') as mocked_print_posts:
			app.print_posts(b)

			mocked_print_posts.assert_called_with(expected_print)

	def test_ask_create_post(self):
		with patch('builtins.input') as mocked_input:
			mocked_input.side_effect = ('Test', 'Test Post', 'Test Content')

			app.ask_create_post()

			self.assertEqual(app.blogs['Test'].posts[0].title, 'Test Post')
			self.assertEqual(app.blogs['Test'].posts[0].content, 'Test Content')


	def test_menu_calls_create_blog(self):
		with patch('builtins.input') as mocked_input:
			mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
			app.menu()

			self.assertIsNotNone(app.blogs['Test Create Blog'])


