from Pack import Startup

app = Startup()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')