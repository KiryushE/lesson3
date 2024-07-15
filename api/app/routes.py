from flask_restful import Api, Resource, request, reqparse
from app import db
from flask import jsonify
from .models import Category, Post


def initialize_routes(api: Api):
    api.add_resource(CategoryListResource, '/categories')
    api.add_resource(CategoryResource, '/categories/<int:id>')
    api.add_resource(PostListResource, '/posts')
    api.add_resource(PostResource, '/posts/<int:id>')


class CategoryListResource(Resource):

    def get(self):
        categories = db.session.query(Category).all()
        return [{"id": cat.id, "name": cat.name} for cat in categories]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help='Name cannot be blank')
        parser.add_argument('description', required=True, help='Description cannot be blank')

        args = parser.parse_args()
        category = Category(name=args['name'], description=args['description'])
        db.session.add(category)
        db.session.commit()
        return {'id': category.id, 'name': category.name}, 201


class CategoryResource(Resource):

    def get(self, id):
        category = db.session.query(Category).get_or_404(id)
        return {'id': category.id, 'name': category.name}

    def put(self, id):
        category = db.session.query(Category).get_or_404(id)
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help='Name cannot be blank')
        parser.add_argument('description', required=True, help='Description cannot be blank')
        args = parser.parse_args()

        category.name = args['name']
        category.description = args['description']
        db.session.commit()
        return {'id': category.id, 'name': category.name, 'description': category.description}

    def delete(self):
        pass


class PostListResource(Resource):
    def get(self):
        return jsonify({"id": 1})


class PostResource(Resource):
    pass


