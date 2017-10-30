import pytest


# NOTE:
# The request variable in py.test is special context of testing.
# See http://doc.pytest.org/en/latest/fixture.html#request-context

# -- Shared fixtures

# auto fixtures

@pytest.yield_fixture(autouse=True, scope='session')
def session_helper():
    yield


@pytest.yield_fixture(autouse=True, scope='module')
def module_helper():
    yield


@pytest.yield_fixture(autouse=True, scope='function')
def function_helper():
    yield


# -- unit test

@pytest.fixture(scope='session')
def config(request):
    def teardown():
        pass

    request.addfinalizer(teardown)

    return None
