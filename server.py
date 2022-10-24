from flask_crud import app
from flask_crud.controllers import cantidades, productos, usuarios

if __name__ == "__main__":
    app.run(debug=True)