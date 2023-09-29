from flask import Flask, render_template, request
import os
from flask_cors import CORS
from flask_cors import cross_origin


app = Flask (__name__)
CORS(app)
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = file.filename
        file.save("/tmp", filename)
        return 'Файл успешно загружен на сервер'
    else:
        return 'Файл не найден'
#@app.route('/upload',
           
#methods = ['POST'])
#@cross_origin(origin='*', methods=['POST'], headers=['Content-Type'])
#def upload():
#    file=request.files['fileToUpload']
#    if file:
        filename=file.filename; file.save(os.path.join('/tmp', filename))
        # Изменить путь при размещении в продакшн
        return 'Файл {} успешно загружен на сервер'.format(filename)
 #   else:
        return 'Файл не найден'



if __name__ == "__main__":
    app.debug = True # Убрать строку кода перед продакшеном
    app.run()  

# АПЛОЙ ФАЙЛА СО СПИСКОМ
# Добавление