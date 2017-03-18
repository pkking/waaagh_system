import pytest
import json
from blog.models import Post, Persion, Tag
from tests.common import *

@pytest.mark.usefixtures("db")
class TestPostCRUD:
    def test_create_post(self, post):
        p,author = post
        assert Post.find_by_id(1)
        assert p.name == post_name
        assert p.body == post_body
        assert p.author == author
        assert p.author.name == persion_name
        assert p.author.email == persion_email
        assert p.author.password == persion_pwd
            
@pytest.mark.usefixtures("db")
class TestTagCRUD:
    def test_create_tag(self, tag):
        u,p,tag = tag
        assert Post.find_by_id(1)
        assert Tag.find_by_id(1)
        assert Persion.find_by_id(1)
        assert tag.posts[0] == p
        assert tag.name == tag_name
        assert p.name == post_name
        assert p.body == post_body
        assert p.author == u
        assert p.author.name == persion_name
        assert p.author.email == persion_email
        assert p.author.password == persion_pwd
    
    def test_retrieve_tag(self):
        pass

    def test_update_tag(self):
        pass
    
    def test_delete_tag(self):
        pass

@pytest.mark.usefixtures("db")
class TestPersionCRUD:
    def test_create_persion(self, user):
        assert Persion.find_by_id(1)
        assert user.name == persion_name
        assert user.email == persion_email
        assert user.password == persion_pwd
            
    def test_retrieve_persion(self):
        pass

    def test_update_persion(self):
        pass
    
    def test_delete_persion(self):
        pass