from app import app, db
import view


if __name__ == '__main__':
	app.run(port=8000, host='127.0.0.1', debug=True)
