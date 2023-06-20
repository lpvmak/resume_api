from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from resumes_app.models import Resume


class ResumeGetPatchTests(APITestCase):
    def setUp(self):
        self.owner_user_creds = {'username': 'testowner_user',
                                 'password': 'testpassword'}
        self.other_user_creds = {'username': 'testother_user',
                                 'password': 'testpassword'}

        self.owner_user = get_user_model().objects.create_user(
            **self.owner_user_creds)
        self.other_user = get_user_model().objects.create_user(
            **self.other_user_creds)

        self.resume_data_active = {
            'id': 1,
            'status': 'active',
            'grade': 'Senior',
            'specialty': 'Software Developer',
            'salary': 5000,
            'education': 'Bachelor of Science in Computer Science',
            'experience': '5 years of experience in web development',
            'portfolio': 'https://www.example.com/portfolio',
            'title': 'Full Stack Developer',
            'phone': '+79111234567',
            'email': 'john.doe@example.com',
        }

        self.resume_data_draft = {
            'id': 2,
            'status': 'draft',
            'grade': 'Middle',
            'specialty': 'Software Developer',
            'salary': 3000,
            'education': 'Bachelor of Science in Computer Science',
            'experience': '3 years of experience in web development',
            'portfolio': '-',
            'title': 'Full Stack Developer',
            'phone': '+79111234567',
            'email': 'john.doe@example.com',
        }

        self.resume = Resume.objects.create(user=self.owner_user,
                                            **self.resume_data_active)
        self.resume = Resume.objects.create(user=self.owner_user,
                                            **self.resume_data_draft)

    def test_anon_get_resumes(self):
        """
        Тест: Неавторизованный пользователь смотрит список резюме
        """
        url = reverse('resume-list')

        response = self.client.get(url, {}, True)
        self.assertEqual(response.status_code, 200)
        # Проверить, что получены только резюме с status=active
        self.assertEqual(len(response.data), 1)
        self.assertDictEqual(response.data[0], self.resume_data_active)

    def test_user_get_resumes(self):
        """
        Тест: Авторизованный пользователь смотрит список резюме
        """
        url = reverse('resume-list')
        self.client.login(**self.owner_user_creds)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Проверить, что получены все резюме
        self.assertEqual(len(response.data), 2)
        self.assertListEqual(response.data,
                             [self.resume_data_active, self.resume_data_draft])

        self.client.login(**self.other_user_creds)
        response = self.client.get(url, {}, True)
        self.assertEqual(response.status_code, 200)
        # Проверить, что получены только резюме с status=active
        self.assertEqual(len(response.data), 1)
        self.assertDictEqual(response.data[0], self.resume_data_active)

    def test_get_active_resume(self):
        """
        Тестируем получение активного резюме
        """
        url = reverse('resume-detail', args=(1,))
        response = self.client.get(url, {}, True)
        self.assertEqual(response.status_code, 200)
        # Проверить, что получены только резюме с status=active
        self.assertDictEqual(response.data, self.resume_data_active)

    def test_not_found_resume(self):
        """
        Тестируем получение несуществующего резюме
        """
        url = reverse('resume-detail', args=(100,))
        response = self.client.get(url, {}, True)
        self.assertEqual(
            response.status_code, 404,
            "Несуществующий объект должен быть недоступен"
        )

    def test_get_draft_resume(self):
        """
        Тестируем получение черновика Резюме
        """
        url = reverse('resume-detail', args=(2,))
        response = self.client.get(url, {}, True)
        self.assertEqual(
            response.status_code, 404,
            "Неавторизованный пользователь не может смотреть черновик"
        )

        self.client.login(**self.other_user_creds)
        response = self.client.get(url, {}, True)
        self.assertEqual(
            response.status_code, 404,
            "Не владелец не может смотреть черновик"
        )

        self.client.login(**self.owner_user_creds)
        response = self.client.get(url, {}, True)
        self.assertEqual(
            response.status_code, 200,
            "Владелец должен смотреть черновик"
        )
        self.assertDictEqual(response.data, self.resume_data_draft)

    def test_patch_resume(self):
        """
        Тест: Владелец изменяет резюме
        """
        url = reverse('resume-detail', args=(1,))
        self.client.login(**self.owner_user_creds)
        new_resume_data = {
            'id': 1,
            'status': 'draft',
            'grade': 'Senior-Pomidor',
            'specialty': 'Developer',
            'salary': 100,
            'education': 'Bachelor of Science in Computer Science',
            'experience': '5 years of experience in web development',
            'portfolio': 'https://www.example.com/portfolio',
            'title': 'Full Stack Developer',
            'phone': '',
            'email': 'john.doe@example.com',
        }
        response = self.client.patch(url, new_resume_data)
        self.assertEqual(
            response.status_code, 200,
        )
        self.assertDictEqual(response.data, new_resume_data)

        new_resume_data['title'] = 'Test'
        response = self.client.patch(url, {'title': 'Test'})
        self.assertEqual(
            response.status_code, 200,
        )
        self.assertDictEqual(response.data, new_resume_data)

        response = self.client.patch(url, {'title': ''})
        self.assertEqual(
            response.status_code, 400,
        )

        response = self.client.patch(url, {'phone': '144'})
        self.assertEqual(
            response.status_code, 400,
        )

    def test_anon_patch_resume(self):
        """
        Тест неавторизованный пользователь пытается изменить резюме
        """
        url = reverse('resume-detail', args=(1,))
        response = self.client.patch(url, {'title': 'Test'})
        self.assertEqual(
            response.status_code, 401,
        )
