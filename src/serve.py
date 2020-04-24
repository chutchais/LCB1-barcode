from waitress import serve

from qrcode.wsgi import application

if __name__ == '__main__':
    serve(application, port='8010')