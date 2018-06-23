from django.test import TestCase
from .models import Post
# Create your tests here.


# Testing
class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="Test1", desc="This is test case 1.")
        Post.objects.create(title="Test2", desc="This is test case 2.")

    def test_post_desc(self):
        test1 = Post.objects.get(title="Test1")
        test2 = Post.objects.get(title="Test2")

        self.assertEqual(test1.print_title_desc(), "Test1|This is test case 1.")
        self.assertEqual(test2.print_title_desc(), "Test2|This is test case 2.")


