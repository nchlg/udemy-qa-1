from blog import Blog
from post import Post

blogs = dict() # blog_mane: blog object
MENU_PROMPT = 'Enter \n[C] to Create a Blog; \n[L] to List Blogs; \n[R] to Read one; \n[P] to Create a Post; or \n[Q] to Quit.'
POST_TEMPLATE = '''
--- {} ---

{}

'''

def menu():
	# Show the user the available blogs
	print_blogs()
	# Let the user make a choice
	selection = input(MENU_PROMPT)
	# Do something with that choice
	while (selection != 'q'):
		if selection == 'c':
			ask_create_blog()
		elif selection == 'l':
			print_blogs()
		elif selection == 'r':
			ask_read_blog()
		elif selection == 'p':
			ask_create_post()
		selection = input(MENU_PROMPT)
	# Eventually exit

# def print_menu_prompt():
# 	input(MENU_PROMPT)

def print_blogs():
	for key, blog in blogs.items():
		print('- {}'.format(blog))

def ask_create_blog():
	blog_title = input('Enter blog title: ')
	blog_author = input('Enter author\'s name: ')

	blogs[blog_title] = Blog(blog_title, blog_author)

def ask_read_blog():
	blog_title = input('Which blog would you like to read? ')
	print_posts(blogs[blog_title])

def print_posts(blog):
	for post in blog.posts:
		print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
	blog_title = input('Enter the blog title: ')
	post_title = input('Enter post title: ')
	post_content = input('Enter post content: ')
	blogs[blog_title].create_post(post_title, post_content)