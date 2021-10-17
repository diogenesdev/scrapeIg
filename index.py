from flask import Flask, request, render_template, url_for, send_file,stream_with_context
from flask.wrappers import Response
from waitress import serve
import waitress
from werkzeug.utils import redirect
import os
import zipfile


from fun_lib import search_profile

app = Flask(__name__,template_folder='template')

@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response(render_template('index.html'))

@app.route("/home", methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        text = request.form.get('search')
        processed_text = text.lower()
        if processed_text is None:
            render_template('404.html')
        else:
            search_profile(processed_text)
        return redirect(url_for('busca_perfil'))
    else:
        return render_template('home.html')

@app.route("/search-finished")
def busca_perfil():
    imagens_zip = 'img.zip'
    zipfolder = zipfile.ZipFile(imagens_zip,'w', compression = zipfile.ZIP_STORED)

    # zip all the files which are inside in the folder
    for root,dirs, files in os.walk('images_profile/'):
        for file in files:
            zipfolder.write('images_profile/'+file)
    zipfolder.close()

    return send_file(imagens_zip,
            mimetype = 'zip',
            attachment_filename= imagens_zip,
            as_attachment = True)

@app.errorhandler(500)
def internal_error(error):
    return render_template('erro-500.html')
    
# @app.route("/404")
# def not_found():
#     return render_template('404.html')
    

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT',5000))
    # waitress.serve(app,port=port)
    app.run(host='0.0.0.0', port=port)
    # app.run()
# if __name__ == '__main__':
#     app.run(debug=True)