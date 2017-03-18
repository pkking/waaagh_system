import pytest
from blog import create_app
from blog.models import db as _db, Post, Persion, Tag
import os
from blog.app import TESTING 
from tests.common import *

@pytest.fixture(scope='function')
def app(request):
    """An application for the tests."""
    os.environ['TYPE'] = TESTING
    _app = create_app()
    request.cls.app = _app.test_client()
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()

@pytest.fixture
def client(app):
    """A Flask test client. An instance of :class:`flask.testing.TestClient`
    by default.
    """
    with app.test_client() as client:
        yield client


@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)


@pytest.yield_fixture(scope='function')
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()


@pytest.fixture()
def user(db):
    """A user for the tests."""
    author = Persion.create(name=persion_name, email=persion_email, password=persion_pwd)
    return author
'''
@pytest.fixture(scope='class')
def app(request):
    os.environ['TYPE'] = TESTING
    app = create_app()
    request.cls.app = app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()
'''
@pytest.fixture()
def post(db, user):
    post = Post.create(name=post_name, body=post_body, author=user)
    return post,user

@pytest.fixture()
def tag(db, user):
    post = Post.create(name=post_name, body=post_body, author=user)
    tag = Tag.create(name=tag_name, posts=[post])
    return user,post,tag