from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Noi dung muon xuat ra vao day" #Thay noi dung muon xuat ra vao day
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
