# # -*- coding:utf-8 -*-
# import uuid
#
# from django.core.urlresolvers import reverse
# from django.test import TestCase
# from rest_framework.test import APIClient
#
# from fe_usuario.models import Usuario
# from fe_usuario.tests.factories import AccessTokenFactory
#
#
# class TestProfileAPIView(TestCase):
#
#     def setUp(self):
#         self.access_token = AccessTokenFactory()
#         self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token.token))
#
#     def test_get(self):
#         response = self.client.get(reverse('profile'))
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(200, response.status_code)
#
#         entity = Usuario.objects.get(pk=response.data.get('uuid'))
#         result = response.data
#
#         self.assertEqual(7, len(result))
#         self.assertEqual(str(entity.uuid), result.get('uuid'))
#         self.assertTrue(result.get('created_at', None))
#         self.assertTrue(result.get('updated_at', None))
#         self.assertEqual(entity.email, result.get('email'))
#         self.assertEqual(entity.entidade.uuid, result.get('entidade'))
#         self.assertEqual(entity.foto, result.get('foto'))
#
#     def test_patch_foto(self):
#         foto = str(uuid.uuid4())
#         response = self.client.patch(reverse('profile'), {
#             'foto': foto
#         })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(200, response.status_code)
#         self.assertEqual(foto, response.data.get('foto'))
#         usuario = Usuario.objects.get(pk=self.access_token.user.uuid)
#         self.assertEqual(str(usuario.foto), response.data.get('foto'))
#
#     def test_patch_foto_invalid(self):
#         foto = 'invalid value'
#         response = self.client.patch(reverse('profile'), { 'foto': foto })
#         # print "STATUS CODE: %s - RESPONSE: %s" % (response.status_code, response.content)
#         self.assertEqual(400, response.status_code)
#         self.assertTrue('errors' in response.data)
