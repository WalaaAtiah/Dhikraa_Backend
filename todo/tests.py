from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import TODO
from rest_framework.test import APITestCase
from rest_framework import  status
import datetime
# Create your tests here.

class TodoTest(APITestCase):
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

        test_todo = TODO.objects.create(
            task="task1",
            owner=testuser1,
            description="testing",
            date= datetime.date(2023, 1, 15),
            time=datetime.time(6, 30, 30)
        )
        test_todo.save()

        test_todo2 = TODO.objects.create(
            task="task2",
            owner=testuser1,
            description="testuser1 testing",
            date= datetime.date(2022, 1, 30),
            time=datetime.time(2, 25, 30)
        )
        test_todo2.save()

        test_todo3 = TODO.objects.create(
            task="task3",
            owner=testuser2,
            description="testuser2 testing",
            date= datetime.date(2023, 1, 30),
            time=datetime.time(7, 15, 30)
        )
        test_todo3.save()

    def setUp(self):
        self.client.login(username='testuser1', password="pass")

    def test_todo_model(self):
        todo = TODO.objects.get(id=1)
        actual_owner = str(todo.owner)
        actual_task = str(todo.task)
        actual_description= str(todo.description)
        actual_date = (todo.date)
        actual_time = str(todo.time)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_task, "task1")
        self.assertEqual(actual_description, "testing")
        self.assertEqual(actual_date, datetime.date(2023, 1, 15))
        self.assertEqual(
            actual_time,"06:30:30"
        )

    def test_user1_get_his_tasks(self):
        url = reverse("todo_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        quiz = response.data
        self.assertEqual(len(quiz), 2)

    def test_user2_get_his_tasks(self):
        self.client.logout()
        self.client.login(username='testuser2', password="pass")
        url = reverse("todo_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        quiz = response.data
        self.assertEqual(len(quiz), 1)

    def test_user_get_others_tasks(self):
        self.client.login(username='testuser1', password="pass")
        url = reverse("todo_detail", args=[3])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_required_list(self):
        self.client.logout()
        url = reverse("todo_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_required_detail(self):
        self.client.logout()
        url = reverse("todo_detail",args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_update_his_task(self):
        self.client.login(username='testuser1', password="pass")
        url = reverse("todo_detail", args=[1])
        data={"id": 1,"task": "test","description": "test","date": "2023-02-10","time": "20:10:00","owner": 1}
        response= self.client.put( url ,data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update_others_task(self):
        self.client.login(username='testuser1', password="pass")
        url = reverse("todo_detail", args=[3])
        data={"id": 3,"task": "testing","description": "testing side","date": "2022-04-22","time": "5:40:25","owner": 2}
        response= self.client.put( url ,data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_delete_his_task(self):
        self.client.login(username='testuser1', password="pass")
        url = reverse("todo_detail", args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        url2 = reverse("todo_list")
        response = self.client.get(url2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        quiz = response.data
        self.assertEqual(len(quiz), 1)

    def test_user_delete_others_tasks(self):
        self.client.login(username='testuser1', password="pass")
        url = reverse("todo_detail", args=[3])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

