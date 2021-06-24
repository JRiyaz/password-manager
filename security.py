class BasePasswordManager:
    # list that holds all of the user's past passwords.
    old_passwords = []

    def get_password(self):
        """ This method returns the current password of the user as a string """
        pass

    def is_correct(self, password: str):
        """ This method receives a string and returns a boolean True or False
        depending on whether the string is equal to the current password or not."""
        pass


class PasswordManager(BasePasswordManager):

    def set_password(self):
        """
        This method receives the password and sets the user's password.
        Password change is successful only if:
            - Security level of the new password is greater.
             - Length of new password is minimum 6
        However, if the old password already has the highest security level,
        new password must be of the highest or equal security level for a successful password change.
        """
        pass

    def get_level(self, password: str = None):
        """
        This method returns the security level of the current password.
        It can also check and return the security level of a new password passed as a string.
        Security levels:
            level 0 - password consists of alphabets or numbers only.
            level 1 - Alphanumeric passwords.
            level 2 - Alphanumeric passwords with special characters.
        """
        pass
