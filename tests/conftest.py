import pytest
import dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env_vars():
    dotenv.load_dotenv(verbose=True)


@pytest.fixture
def common():
    from xmlrpc import client
    from os import environ

    return client.ServerProxy(f'{environ.get("ODOO_SRV")}/xmlrpc/2/common')


def api_execute_kw(model: str, func: str, args: list = None, kwargs: dict = None):
    from xmlrpc import client
    from os import environ

    if not args:
        args = []
    
    if not kwargs:
        kwargs = {}
    
    common = client.ServerProxy(f'{environ.get("ODOO_SRV")}/xmlrpc/2/common')
    
    uid = common.authenticate(environ.get("ODOO_DB"),
                              environ.get("ODOO_USER"),
                              environ.get("ODOO_PWD"),
                              {})

    api = client.ServerProxy(f'{environ.get("ODOO_SRV")}/xmlrpc/2/object',
                             allow_none=True)

    return api.execute_kw(environ.get("ODOO_DB"), uid, environ.get("ODOO_PWD"),
                          model, func, args, kwargs)


@pytest.fixture
def execute_kw() -> callable:
    return api_execute_kw
