from flask import Flask, render_template
from application import create_app


app = create_app()

# Default port:
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

