# # -*- coding:utf-8 -*-
# from unittest import TestCase
#
# import pytest
# from django.core.urlresolvers import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
#
# from fe_usuario.tests.factories import AccessTokenFactory
#
#
# @pytest.mark.django_db(transaction=False)
# class TestLogoutAPIView(TestCase):
#     def setUp(self):
#         access_token = AccessTokenFactory()
#         self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(access_token.token))
#
#     def test_get(self):
#         response = self.client.get(reverse('logout'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
