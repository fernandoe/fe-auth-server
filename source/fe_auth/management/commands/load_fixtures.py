# -*- coding:utf-8 -*-
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('loaddata', 'fe_core.User.json')
        call_command('loaddata', 'oauth2_provider.Application.json')
        call_command('loaddata', 'oauth2_provider.AccessToken.json')
