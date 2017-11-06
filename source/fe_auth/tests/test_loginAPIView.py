# # -*- coding:utf-8 -*-
# from django.core.urlresolvers import reverse
# from django.test import TestCase
#
# from fe_usuario.tests.factories import ProdutoFactory, UsuarioFactory
#
#
# class TestLoginAPIView(TestCase):
#
#     def setUp(self):
#         self.base_url = reverse('login')
#         self.email = 'test@domain.com.br'
#         self.password = 'minha-senha'
#         self.produto = ProdutoFactory()
#         self.usuario = UsuarioFactory(email=self.email, password=self.password)
#
#     def _get_produto_uuid(self):
#         return str(self.produto.uuid)
#
#     def test_405(self):
#         for method in ['get', 'put', 'patch', 'delete']:
#             response = getattr(self.client, method)(self.base_url)
#             # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#             self.assertEqual(405, response.status_code)
#
#     def test_produto_blank(self):
#         response = self.client.post(self.base_url, {
#             'email': self.email,
#             'password': self.password
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(401, response.status_code)
#
#     def test_produto_invalid(self):
#         response = self.client.post(self.base_url, {
#             'produto': 'invalid_produto',
#             'email': self.email,
#             'password': self.password
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(401, response.status_code)
#
#     def test_email_invalid(self):
#         response = self.client.post(self.base_url, {
#             'produto': self._get_produto_uuid(),
#             'email': 'invalid_email',
#             'password': self.password
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(400, response.status_code)
#         self.assertTrue('email' in response.data)
#         self.assertEqual(1, len(response.data))
#
#     def test_email_blank(self):
#         response = self.client.post(self.base_url, {
#             'produto': self._get_produto_uuid(),
#             'password': self.password
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(400, response.status_code)
#         self.assertEqual(1, len(response.data))
#         self.assertTrue('email' in response.data)
#
#     def test_password_blank(self):
#         response = self.client.post(self.base_url, {
#             'produto': self._get_produto_uuid(),
#             'email': self.email
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(400, response.status_code)
#         self.assertEqual(1, len(response.data))
#         self.assertTrue('password' in response.data)
#
#     def test_200(self):
#         response = self.client.post(self.base_url, {
#             'produto': self._get_produto_uuid(),
#             'email': self.email,
#             'password': self.password
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         data = response.data
#         self.assertEqual(200, response.status_code)
#         self.assertEquals(5, len(data))
#         self.assertTrue('access_token' in data)
#         self.assertTrue('token_type' in data)
#         self.assertTrue('expires_in' in data)
#         self.assertTrue('refresh_token' in data)
#         self.assertTrue('scope' in data)
#
#         self.assertEquals('Bearer', data['token_type'])
#         self.assertEquals(36000, data['expires_in'])
#         self.assertEquals({u'read': u'Reading scope', u'write': u'Writing scope'}, data['scope'])
