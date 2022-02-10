from django.test import TestCase, Client
from posts.models import Post, Group
from django.contrib.auth import get_user_model

User = get_user_model()

class StaticURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_homepage(self):
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_AboutAuthorPage(self):
        response = self.guest_client.get('/about/author/')
        self.assertEqual(response.status_code, 200)

    def test_AboutTechPage(self):
        response = self.guest_client.get('/about/tech/')
        self.assertEqual(response.status_code, 200)


class PostURLTests(TestCase):
    def setUpClass(cls):
        super().setUpClass()
        cls.author = User.objects.create_user(username='author')
        cls.group = Group.objects.create(
            title='Тестовый заголовок',
            description='Тестовый текст',
            slug='test-slug'
        )
        cls.post = Post.objects.create(
            author=cls.author,
            group=cls.group,
            text='Тестовый заголовок',
            pub_date='22.02.2022',
        )
        cls.guest_client = Client()
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.author)


        def test_about_url_exists_at_desired_location_index(self):
            response = self.guest_client.get('/')
            self.assertEqual(response.status_code, 200)

