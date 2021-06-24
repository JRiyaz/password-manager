from unittest import TestCase
from options import Options
from security import PasswordManager


class TestOptions(TestCase):

    def setUp(self) -> None:
        self.ops = Options()
        self.pw = PasswordManager()

    def tearDown(self) -> None:
        del self.ops
        del self.pw

    def test_check_password(self):
        # first test
        self.pw.old_passwords.append('password')

        self.assertTrue(self.ops.check_password())
