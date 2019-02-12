from flask_restful.reqparse import RequestParser

# get 请求为args， post请求为json
parser = RequestParser()
parser.add_argument('id',type=int,location='args',required=True)
