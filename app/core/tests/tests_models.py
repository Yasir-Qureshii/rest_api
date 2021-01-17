from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()


class ModelTests(TestCase):
	def test_create_user_with_email_successful(self):
		"""Test creating a new user with email is successful"""
		email = 'qureshi@gmail.com'
		password = 'admin'
		user = User.objects.create_user(email=email, password=password)
		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))

	def test_new_user_email_normalized(self):
		"""Test the email for a new user is normalized"""
		email = 'qureshi@GMAIL.COM'
		user = User.objects.create_user(email, 'admin')

		self.assertEqual(user.email, email.lower())

	def test_new_user_invalid_email(self):
		"""Test creating user with no email raises error"""
		with self.assertRaises(ValueError):
			User.objects.create_user(None, 'qaaa')

	def test_create_new_superuser(self):
		"""Test creating a new user"""
		user = User.objects.create_superuser('admin@admin.com', 'admin')
		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)
