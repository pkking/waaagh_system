from flask_restful import Api
from flask_restful import reqparse, Api, Resource, fields, marshal_with
from blog.models import Post, Tag, Persion

api = Api()

post_fields = {
    'name': fields.String,
    'body': fields.String,
    'created': fields.DateTime(dt_format='rfc822'),
    'modified': fields.DateTime(dt_format='rfc822'),
    'author': fields.String
}

persion_fields = {
    'name': fields.String,
    'email': fields.String,
    'created': fields.DateTime(dt_format='rfc822'),
    'last_login': fields.DateTime(dt_format='rfc822')
}

tag_fields = {
    'name': fields.String
}

class blogPosts(Resource):
    @marshal_with(post_fields)
    def get(self, blog_id=None):
        if blog_id:
            return Post.find_by_id(blog_id)
        else:
            return Post.get_all()


class blogPersions(Resource):
    @marshal_with(persion_fields)
    def get(self, persion_id=None):
        if persion_id:
            return Persion.find_by_id(persion_id)
        else:
            return Persion.get_all()

class blogTags(Resource):
    @marshal_with(tag_fields)
    def get(self, tag_id=None):
        if tag_id:
            return Tag.find_by_id(tag_id)
        else:
            return Tag.get_all()

api.add_resource(blogPosts, '/posts', '/posts/', '/posts/<int:blog_id>', endpoint="posts")
api.add_resource(blogTags, '/tags', '/tags/', '/tags/<int:tag_id>', endpoint="tags")
api.add_resource(blogPersions, '/persions', '/persions/', '/persions/<int:persion_id>', endpoint="persions")