from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Post

# Create your tests here.


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.url = reverse('post-list-create')
        self.data = {"title": "Test Post", "content": "This is a test"}

    def test_create_post(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.get()
        self.assertEqual(post.title, self.data['title'])
        self.assertEqual(post.content, self.data['content'])
        self.assertEqual(response.data['title'], self.data['title'])
        self.assertEqual(response.data['content'], self.data['content'])

    def test_list_posts(self):
        Post.objects.create(
            title=self.data['title'], content=self.data['content'])
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(response.data[0]['title'], self.data['title'])
        self.assertEqual(response.data[0]['content'], self.data['content'])
