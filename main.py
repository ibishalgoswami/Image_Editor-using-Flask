from flask import Flask,render_template,request
from PIL import Image
from PIL import ImageFilter
import os
import time

app=Flask(__name__)

app.config['UPLOAD_FOLDER']='C:\\Users\\CISPL-BISHALG\\Desktop\\Image_Editor Project\\static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['post'])
def resize_Image():
    try:
        if request.method == "POST":
            file = request.files['file']
            file_name = file.filename
            print(file_name)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            list_dir=os.listdir(app.config['UPLOAD_FOLDER'])
            print(list_dir)
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
            return render_template('resize.html', width=width, height=height, new_image=new_image)
    except:
        return render_template('error.html')

@app.route('/pngorpdf/',methods=['POST'])
def pdforpng():
    try:
        if request.method == "POST":
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
            return render_template('pngorpdf.html', new_image=new_image,option_val=option_val)
            
    except:
        return render_template('error.html')

@app.route('/imagecompress/',methods=['POST'])
def imgcompress():
    try:
        if request.method == "POST":
            file = request.files['file']
            file_name = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            file = "static/" + file_name
            img = Image.open(file)
            mywidth = img.width
            wpercent = (mywidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            base = os.path.basename(file)
            newfilename=os.path.splitext(base)[0]
            img = img.resize((mywidth,hsize), Image.ANTIALIAS)
            new_image = "static/"+'compressed'+ newfilename + '.jpg'
            img.save(new_image)
            return render_template('bb.html')
    except:
        return render_template('error.html')

@app.route('/imageFilteration/',methods=['POST'])
def imageFilteration():
    try:
        if request.method == "POST":
            file = request.files['file']
            file_name = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            file = "static/" + file_name
            option_val = request.form['options']
            base = os.path.basename(file)
            newfilename=os.path.splitext(base)[0]    
            
            Img=Image.open(file)
            if option_val == 'B&W':
                Img=Img.convert('L')
                new_image = "static/"+'filtered'+ newfilename + '.jpg'
        
            if option_val == 'BLUR':
                Img=Img.filter(ImageFilter.BoxBlur(1))
                new_image = "static/"+'filtered'+ newfilename + '.jpg'

            if option_val == 'CONTOUR':
                Img=Img.filter(ImageFilter.CONTOUR)
                new_image = "static/"+'filtered'+ newfilename + '.jpg'
            
            if option_val == 'SMOOTH':
                Img=Img.filter(ImageFilter.SMOOTH)
                new_image = "static/"+'filtered'+ newfilename + '.jpg'
            
            if option_val == 'SHARPEN':
                Img=Img.filter(ImageFilter.SHARPEN)
                new_image = "static/"+'filtered'+ newfilename + '.jpg'

            if option_val == 'EMBOSS':
                Img=Img.filter(ImageFilter.EMBOSS)
                new_image = "static/"+'filtered'+ newfilename + '.jpg'

            if option_val == 'EDGE_ENHANCE':
                Img=Img.filter(ImageFilter.EDGE_ENHANCE)
                new_image = "static/"+'filtered'+ newfilename + '.jpg'

            Img.save(new_image)
            return render_template('image_filteration.html',new_image=new_image)
    except:
        return render_template('error.html')

@app.route('/imageRotation/',methods=['POST'])
def imageRotation():
    try:
        if request.method == "POST":
            file = request.files['file']
            file_name = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            file = "static/" + file_name
            option_val = request.form['options']
            base = os.path.basename(file)
            newfilename=os.path.splitext(base)[0]    
            Img=Image.open(file)

            if option_val == 'LEFT':
                val=90
                Img=Img.rotate(val)
                # new_image = "static/"+'rotated'+ newfilename + '.jpg'

            if option_val == 'RIGHT':
                val=270
                Img=Img.rotate(val)
                # new_image = "static/"+'rotated'+ newfilename + '.jpg'
        
            if option_val == 'DOWN':
                val=180
                Img=Img.rotate(val)
                
            new_image = "static/"+'rotated'+ newfilename + '.jpg'
            Img.save(new_image)
            return render_template('image_rotation.html',new_image=new_image)
    except:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)


#Q. How to redirect according to radio button value in Flask?
#https://stackoverflow.com/questions/41845012/how-to-redirect-according-to-radio-button-value-in-flask