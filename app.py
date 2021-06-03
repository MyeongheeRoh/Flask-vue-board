from flask import Flask
from application import create_app


app = create_app()

# Default port:
if __name__ == '__main__':
    app.run()
