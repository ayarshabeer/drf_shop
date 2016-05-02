from accounts.models import User
from django.contrib.auth.backends import ModelBackend


class EmailAuthBackend(ModelBackend):

    def authenticate(self, username=None, email=None, password=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            if not username:
                username = email
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
