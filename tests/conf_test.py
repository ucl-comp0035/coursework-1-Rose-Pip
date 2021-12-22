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


# test 2
def test_check_password(general_user):
    """
    GIVEN a user with default password
    WHEN the function check_password has a string password attribute
    THEN the the string password does not match the hashed password
    """
    check = general_user.check_password('password')
    assert check is True

