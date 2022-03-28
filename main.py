import sys
from myapp import create_app, db

sys.dont_write_bytecode = True

app = create_app()
db.create_all(app=create_app())

if __name__ == "__main__":
    app.run(debug=True)