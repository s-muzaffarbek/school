from django.test import TestCase

from rest_framework.authtoken.models import Token
token = Token.objects.get(key="436db906b046cb0995fb9151a7684505d03347c2")
user = token.user
print(user.username)
