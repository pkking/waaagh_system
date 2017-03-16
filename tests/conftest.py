import pytest
from blog import create_app
import os
from blog.app import TESTING


@pytest.fixture(scope='class')
def app(request):
    os.environ['TYPE'] = TESTING
    app = create_app()
    request.cls.app = app.test_client()