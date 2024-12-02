Flask API

Flask API is a REST API built with Python and Flask:
- Create blog posts
- Read all blog posts
- Update exitsing blog posts
- Delete blog posts
===========================================================================================================================
To use this project you have to:
- Create a virtual environment (with virtualenv)
- Activate this virtual environment (in Powershell for example)
- Download packages
- Start the project (python main.py)
  
============================================================================================================================
Example of usage:

HTTP-Method: POST
URL: localhost:5000/post

HTTP-Method: GET
URL: localhost:5000/post
Body:  {"id": 1, "title": "TikTok Blog", "author": "@anonym90" }

HTTP-Method: DELETE
URL: localhost:5000/post
Body:  {"id": 1, "title": "TikTok Blog", "author": "@anonym90" }

HTTP-Method: PUT
URL: localhost:5000/post
Body:  {"id": 1, "title": "Instagram Blog", "author": "@ziri"}



