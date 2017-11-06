# # -*- coding:utf-8 -*-
# from django.test import TestCase
#
# from fe_usuario.tests.factories import UsuarioFactory, AplicacaoFactory
#
#
# class TestOAuthTokenAPI(TestCase):
#
#     def setUp(self):
#         self.base_url = '/o/token/'
#         self.email = 'test@domain.com.br'
#         self.password = 'minha-senha'
#         self.usuario = UsuarioFactory(email=self.email, password=self.password)
#         self.aplicacao = AplicacaoFactory(user=self.usuario)
#
#     def test_pegando_toke(self):
#         HEADERS = {
#             'grant_type': 'password',
#             'client_id': self.aplicacao.client_id
#         }
#         response = self.client.post(self.base_url, {
#             'username': self.email,
#             'password': self.password
#         }, **HEADERS)
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         data = response.json()
#         self.assertEqual(200, response.status_code)
#         self.assertEquals(5, len(data))
#         self.assertTrue('access_token' in data)
#         self.assertTrue('token_type' in data)
#         self.assertTrue('expires_in' in data)
#         self.assertTrue('refresh_token' in data)
#         self.assertTrue('scope' in data)
