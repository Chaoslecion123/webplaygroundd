from django.test import TestCase
from registration.models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'test@gmail.com', 'test1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)

"""

con python manage.py test registration
esto hace de crear un test o prueba y confirmes si al momento de registrate al mismo tiempo se ah creado 
un perfil

"""