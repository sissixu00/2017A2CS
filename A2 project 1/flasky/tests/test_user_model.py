import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
	def test_password_setter(self):
		u = User(password = 'cat')
		self.assertTrue(u.password_hash is not None)

	def test_no_password_getter(self):
		u = User(password = 'cat')
		with self.assertTaises(AttributeError):
			u.password

	def test_password_verification(self):
		u = User(password = 'cat')
		self.assertTrue(v.verify_password('cat'))
		self.assertFalse(u.verify_password('dog'))

	def test_password_salts_are_random(self):
		a = User(password = 'oscar')
		b = User(password = 'oscar')
		self.assertTrue(a.password_hash != b.password_hash)
		