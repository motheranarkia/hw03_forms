from django.test import TestCase, Client


class StaticURLTests(TestCase):
    def setUp(self):
        # Устанавливаем данные для тестирования
        # Создаём экземпляр клиента. Он неавторизован.
        self.guest_client = Client()

    def test_homepage(self):
        # Отправляем запрос через client,
        # созданный в setUp()
        response = self.guest_client.get('/')  
        self.assertEqual(response.status_code, 200)

    def test_AboutAuthorPage(self):
        response = self.guest_client.get('/about/author/')  
        self.assertEqual(response.status_code, 200)

    def test_AboutTechPage(self):
        response = self.guest_client.get('/about/tech/')  
        self.assertEqual(response.status_code, 200)

