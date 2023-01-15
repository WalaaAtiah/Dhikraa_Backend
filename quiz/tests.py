from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Quiz
from rest_framework.test import APITestCase
from rest_framework import status
# # Create your tests here.


class QuizTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass"
        )
        testuser2.save()

        test_quiz = Quiz.objects.create(
            owner=testuser1,
            type="testing1",
            question="Q(1)",
            choices={
                "wrong1": "1",
                "wrong2": "2",
                "wrong3": "3",
                "correct": "yes"
            }
        )
        test_quiz.save()

        test_quiz2 = Quiz.objects.create(
            owner=testuser1,
            type="testing2",
            question="Q(2)",
            choices={
                "wrong1": "1",
                "correct": "yes",
                "wrong2": "2",
                "wrong3": "3",
            }
        )
        test_quiz2.save()

        test_quiz3 = Quiz.objects.create(
            owner=testuser2,
            type="testing1",
            question="Q(3)",
            choices={
                "wrong1": "1",
                "wrong2": "2",
                "correct": "yes",
                "wrong3": "3",
            }
        )
        test_quiz3.save()

    def setUp(self):
        self.client.login(username='testuser2', password="pass")

    def test_todo_model(self):
        quiz = Quiz.objects.get(id=3)
        actual_owner = str(quiz.owner)
        actual_type = str(quiz.type)
        actual_question = str(quiz.question)
        actual_choices = (quiz.choices)
        self.assertEqual(actual_owner, "testuser2")
        self.assertEqual(actual_type, "testing1")
        self.assertEqual(actual_question, "Q(3)")
        self.assertEqual(actual_choices, {
            "wrong1": "1",
            "wrong2": "2",
            "correct": "yes",
            "wrong3": "3",
        })

    def test_user1_get_all_quizzes(self):
        self.client.logout()
        self.client.login(username='testuser1', password="pass")
        url = reverse("quiz_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        quiz = response.data
        self.assertEqual(len(quiz), 3)

    def test_user2_get_all_quizzes(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("quiz_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        quiz = response.data
        self.assertEqual(len(quiz), 3)

    def test_auth_required_list(self):
        self.client.logout()
        url = reverse("quiz_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_required_detail(self):
        self.client.logout()
        url = reverse("quiz_detail", args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_create_question(self):
        self.client.login(username='testuser2', password="pass")
        url = reverse("quiz_list")
        data=data = {
            "type": "testing",
            "question": "Q(4)",
            "choices": {
                "wrong1": "1",
                "wrong2": "2",
                "wrong3": "3",
                "correct": "yes"
            },
            "owner": 2
        }
        response= self.client.post( url ,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_update_quizzes(self):
        self.client.login(username='testuser1', password="pass")
        url = reverse("quiz_detail", args=[2])
        data = {
            "id": 2,
            "type": "testing",
            "question": "q(2)",
            "choices": {
                "wrong1": "1",
                "wrong2": "2",
                "wrong3": "3",
                "correct": "yes"
            },
            "owner": 1
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_delete_quizzes(self):
        self.client.login(username='testuser1', password="pass")
        url = reverse("quiz_detail", args=[3])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
