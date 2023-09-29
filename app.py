from flask import Flask, render_template, request
import os

app = Flask (__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/upload',
methods = ['POST'])
def upload():
    file=request.files['fileToUpload']
    if file:
        filename=file.filename; file.save(os.path.join('/Users/Polkovnikovav/Desktop/Parser-F9-art-main/tmp', filename))
        # Изменить путь при размещении в продакшн
        return 'Файл {} успешно загружен на сервер'.format(filename)
    else:
        return 'Файл не найден'


if __name__ == "__main__":
    app.debug = True # Убрать строку кода перед продакшеном
    app.run()  

# АПЛОЙ ФАЙЛА СО СПИСКОМ
# Добавление
