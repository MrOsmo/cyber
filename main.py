from flask import Flask, jsonify, request
from model.post import Post
import json

posts = []

app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Post):
            return {'id': obj.id, 'title': obj.title, 'author': obj.author}
        else:
            return super().default(obj)

@app.route('/post', methods=['POST'])
def create_post():
    '''
    {
    "id": 1, 
    "title": "TikTok Blog", 
    "author": "@mrosmo"
    }
    '''
    post_json = request.get_json()
    post = Post(post_json['id'], post_json['title'], post_json['author'])
    posts.append(post)
    return jsonify({'status': '200'})

@app.route('/post', methods=['GET'])
def get_post():
    serialized_posts = [{'id': post.id, 'title': post.title, 'author': post.author} for post in posts]
    return jsonify({'posts': serialized_posts})

@app.route('/post', methods=['PUT'])
def put_post():
    '''
    {
    "id": 1, 
    "title": "Instagram Blog", 
    "author": "@ziri"
    }
    '''
    post_json = request.get_json()

    for post in posts:
        if post.id == post_json['id']:
            post.title = post_json.get('title', post.title)
            post.author = post_json.get('author', post.author)
            return jsonify({'status': '200'})
    return jsonify({'status': '400'})

@app.route('/post', methods=['DELETE'])
def delete_post():
    '''
    {
    "id": 1, 
    "title": "Instagram Blog", 
    "author": "@ziri"
    }
    '''

    post_json = request.get_json()
    trash_post = None

    for post in posts:
        if post.id == post_json['id']:
            trash_post = post
            posts.remove(trash_post)
            return jsonify({'status': '200'})
    return jsonify({'status': '400'})

if __name__ == '__main__':
    app.run(debug=True)