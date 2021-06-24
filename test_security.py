from unittest import TestCase
from security import BasePasswordManager, PasswordManager


class TestBasePasswordManager(TestCase):

    def setUp(self) -> None:
        self.bpw = BasePasswordManager()

    def test_get_password(self):
        # first test
        self.assertEqual(self.bpw.get_password(), '')

        # second test
        self.bpw.old_passwords = li = ['password', 'security']
        self.assertEqual(self.bpw.get_password(), li[-1])

    def test_is_correct(self):
        # first test
        self.assertFalse(self.bpw.is_correct('password'))

        # second test
        self.bpw.old_passwords = ['password']
        self.assertTrue(self.bpw.is_correct('password'))

    def test_get_all_passwords(self):
        # first test
        self.assertFalse(self.bpw.get_all_passwords())

        # second test
        self.bpw.old_passwords = li = ['password', 'security']
        self.assertEqual(self.bpw.get_all_passwords(), li)

    def tearDown(self) -> None:
        del self.bpw


class TestPasswordManager(TestCase):

    def setUp(self) -> None:
        # self.bpw = BasePasswordManager()
        self.pw = PasswordManager()

    def tearDown(self) -> None:
        # del self.bpw
        del self.pw

    def test_set_password(self):
        # first test
        self.assertEqual(self.pw.set_password('12345'), -1)

        # second test
        self.pw.old_passwords = ['password@123']
        self.assertEqual(self.pw.set_password('password@123'), 2)

        # third test
        self.assertEqual(self.pw.set_password('123456'), 1)

        # fourth test
        self.assertEqual(self.pw.set_password('password$123'), 0)

    def test_get_level(self):
        # first test
        self.assertEqual(self.pw.get_level(), -1)

        pwd = ['123456', 'password123', 'password@123']
        zero, one, two = 0, 1, 2
        # second test
        self.assertEqual(self.pw.get_level(pwd[zero]), zero)

        # third test
        self.assertEqual(self.pw.get_level(pwd[one]), one)

        # fourth test
        self.assertEqual(self.pw.get_level(pwd[two]), two)

        # fifth test
        self.pw.old_passwords.append(pwd[zero])
        self.assertEqual(self.pw.get_level(), zero)

        # sixth test
        self.pw.old_passwords.append(pwd[one])
        self.assertEqual(self.pw.get_level(), one)

        # seventh test
        self.pw.old_passwords.append(pwd[two])
        self.assertEqual(self.pw.get_level(), two)
