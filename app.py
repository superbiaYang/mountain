from flask import *
import file_list
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

file_list.init(app)

@app.route('/test_windows_files')
def test_windows_files():
    return redirect(url_for("get_files", target_dir=u"C:\\"))

if __name__ == '__main__':
    app.run()