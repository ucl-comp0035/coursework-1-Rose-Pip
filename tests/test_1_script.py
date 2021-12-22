from python.main import User
import pytest


@pytest.fixture(scope='function')  # the fixture executes per function
def general_user():
    g_user = User(first_name='f_name', last_name='l_name', email_address='123@email.com', username="u_name")
    yield g_user


# test 1
def test_hashed_password_is_none(general_user):
    """
    GIVEN a user
    WHEN the password hasn't been set up
    THEN the default hashed password will be None
    """

    hashpassword = general_user.password_hash
    assert hashpassword is None
