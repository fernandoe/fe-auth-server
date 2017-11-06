# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase

from fe_core.models import User, Entity
from fe_core.tests.factories import UserFactory


class TestRegisterAPIView(TestCase):

    def setUp(self):
        self.base_url = reverse('register')
        self.email = 'test@domain.com.br'
        self.password = 'minha-senha'
        self.usuario = UserFactory()

    def test_405(self):
        for method in ['get', 'put', 'patch', 'delete']:
            response = getattr(self.client, method)(self.base_url)
            self.assertEqual(405, response.status_code)

    def test_email_invalid(self):
        response = self.client.post(self.base_url, {
            'email': 'invalid_email',
            'password': self.password
        })
        self.assertEqual(400, response.status_code)
        self.assertTrue('email' in response.data)
        self.assertEqual(1, len(response.data))

    def test_email_blank(self):
        response = self.client.post(self.base_url, {
            'password': self.password
        })
        self.assertEqual(400, response.status_code)
        self.assertEqual(1, len(response.data))
        self.assertTrue('email' in response.data)

    def test_password_blank(self):
        response = self.client.post(self.base_url, {
            'email': self.email
        })
        self.assertEqual(400, response.status_code)
        self.assertEqual(1, len(response.data))
        self.assertTrue('password' in response.data)

    def test_post_usuario_ja_cadastrado(self):
        response = self.client.post(self.base_url, {
            'email': self.usuario.email,
            'password': self.password
        })
        self.assertEqual(400, response.status_code)
        self.assertEqual(1, len(response.data))
        self.assertTrue('email' in response.data)

    def test_post_201(self):
        response = self.client.post(self.base_url, {
            'email': self.email,
            'password': self.password
        })
        self.assertEqual(201, response.status_code)
        self.assertEqual(2, User.objects.all().count())

        usuario = User.objects.get(email=self.email)
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)
        self.assertEqual(self.email, usuario.email)
        self.assertNotEquals(self.password, usuario.password)
        self.assertTrue(usuario.check_password(self.password))

        self.assertIsNone(usuario.entity)
        self.assertEquals(1, Entity.objects.all().count())
