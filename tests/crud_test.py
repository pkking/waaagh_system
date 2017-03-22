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

    def test_update_post(self, post):
        p,author = post
        p.name = post_name1
        p.body = post_body1
        author.name = persion_name1
        author.email = persion_email1
        author.password = persion_pwd1
        author.save()
        p.save()
        tmp = Post.find_by_id(1)
        assert tmp == p
        assert tmp.name == post_name1
        assert tmp.body == post_body1
        assert tmp.author == author
        assert tmp.author.name == persion_name1
        assert tmp.author.email == persion_email1
        assert tmp.author.password == persion_pwd1
            
    def test_retrieve_post(self, post):
        p,_ = post
        assert Post.find_by_id(1)
        assert Post.find_by_id(1) == p

    def test_delete_tag(self, post):
        p,_ = post
        assert Post.find_by_id(1)
        assert Post.find_by_id(1) == p
        p.delete()
        assert Post.query.get(1) == None

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
    
    def test_retrieve_tag(self, tag):
        u,p,tag = tag
        assert Tag.find_by_id(1)
        assert Tag.find_by_id(1) == tag

    def test_update_tag(self, tag):
        u,p,t = tag
        t.name = tag_name1
        t.save()
        p.name = post_name1
        p.body = post_body1
        p.save()
        u.name = persion_name1
        u.email = persion_email1
        u.password = persion_pwd1
        u.save()
        tmp = Post.find_by_id(1)
        assert tmp == p
        assert tmp.name == post_name1
        assert tmp.body == post_body1
        assert tmp.author == u
        assert tmp.author.name == persion_name1
        assert tmp.author.email == persion_email1
        assert tmp.author.password == persion_pwd1
        assert tmp.tags[0] == t
        assert tmp.tags[0].name == tag_name1
    
    def test_delete_tag(self, tag):
        u,p,tag = tag
        assert Tag.find_by_id(1)
        assert Tag.find_by_id(1) == tag
        tag.delete()
        assert Tag.query.get(1) == None


@pytest.mark.usefixtures("db")
class TestPersionCRUD:
    def test_create_persion(self, user):
        assert Persion.find_by_id(1)
        assert user.name == persion_name
        assert user.email == persion_email
        assert user.password == persion_pwd
            
    def test_retrieve_persion(self, user):
        assert Persion.find_by_id(1)
        assert Persion.find_by_id(1) == user

    def test_update_persion(self, user):
        user.name = persion_name1
        user.email = persion_email1
        user.password = persion_pwd1
        user.save()
        tmp = Persion.find_by_id(1)
        assert tmp == user
        assert tmp.name == persion_name1
        assert tmp.email == persion_email1
        assert tmp.password == persion_pwd1
    
    def test_delete_persion(self, user):
        assert Persion.find_by_id(1)
        assert Persion.find_by_id(1) == user
        user.delete()
        assert Persion.query.get(1) == None