import pytest


@pytest.mark.smoke
def test_smoke_case():
    ...


@pytest.mark.regression
def regression_test_case():
    ...


@pytest.mark.smoke
class TestSuite:
    def test_case_1(self):
        ...

    def test_case_2(self):
        ...


@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_password_reset(self):
        ...

    def test_logout(self):
        ...


@pytest.mark.slow
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    ...


@pytest.mark.ui
class TestUserInterface:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass
