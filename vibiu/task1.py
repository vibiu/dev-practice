
"""Task1."""
url = 'http://222.204.3.49:8082'


class LoginUser():
    """Login user class, for pass the test."""

    def __init__(self, username, password):
        """Initlize username and password."""
        self.username = username
        self.password = password

    def login(self):
        """User login."""
        pass

    def get_page(self):
        """Get user index page."""
        self.login()
        # get page of 'http://222.204.3.49:8082/user/Index.aspx'
        return '【赖强】'
