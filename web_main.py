from flask import Flask,render_template,request
from PIL import Image
import os

app=Flask(__name__)

app.config['UPLOAD_FOLDER']='C:\\Users\\CISPL-BISHALG\\Desktop\\Image_Editor Project\\static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['post'])
def resize_Image():
    if request.method == "POST":
        file = request.files['file']
        file_name = file.filename
        print(file_name)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        width = int(request.form['width'])
        height = int(request.form['height'])
        file = "static/"+file_name
        print(file)
        Img = Image.open(file)
        Width = width
        Height = height
        size = (Width, Height)
        Img = Img.resize(size)
        new_image = "static/"+'new'+file_name
        Img.save(new_image)
        # Img.show()
        return render_template('val.html', width=width, height=height, new_image=new_image)

@app.route('/pngorpdf/',methods=['POST'])
def pdforpng():
    file = request.files['file']
    file_name = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    file = "static/" + file_name
    option_val = request.form['options']
    print(os.path.join(app.config['UPLOAD_FOLDER']))
    Img = Image.open(file)
    base = os.path.basename(file)
    newfilename=os.path.splitext(base)[0]
    if option_val == 'png':
        new_image = "static/"+'new'+ newfilename + '.png'
        Img.save(new_image)
    if option_val == 'pdf':
        new_image = "static/" + 'new' + newfilename + '.pdf'
    Img.save(new_image)
    return render_template('success.html', new_image=new_image,option_val=option_val)

## Download file section to do.
# @app.route('/download')
# def downloadFile ():
#     #For windows you need to use drive name [ex: F:/Example.pdf]
#     path ='static/'+new_image
#     return send_file(path)

if __name__ == '__main__':
    app.run(debug=True)

#Q. How to redirect according to radio button value in Flask?
#https://stackoverflow.com/questions/41845012/how-to-redirect-according-to-radio-button-value-in-flask