from flask import Flask ,render_template,redirect, url_for, request,jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from PIL import Image
from keras.preprocessing.image import load_img
from tensorflow import keras
import os
import zipfile
from keras.preprocessing.image import img_to_array


model = keras.models.load_model("C:/model.h5")#path to the model
UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['zip'])
alloed=set(['png','jpeg','jpg'])

app = Flask (__name__)


#home Page
@app.route("/")
def B1():
  return render_template("HomePage.html")
#yes ,No page 
@app.route("/B2")
def B2():
  return render_template("B2.html")

#uplode zip file of covid-19 image 
@app.route("/folderImg")
def folderImg():
  return render_template("folderImg.html")

def allowed_file(filename):
    return '.' in filename and \
          filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/uplo", methods = ['GET', 'POST'])
def uplo():
    error = None
    if request.method == 'POST':
        file = request.files['file']
      
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            zip_file = zipfile.ZipFile(os.path.join(UPLOAD_FOLDER, filename), 'r')
            zip_file.extractall(UPLOAD_FOLDER)
            zip_file.close()

            #count the numer of imges befor adding the new data
            dir_name='C:/Users/alaa5/Desktop/499/interface/Final_FinalInterface/FinalInterface/data'#pathe to the new dir to stor All the data
            old_file_count=sum([len(files) for r, d, files in os.walk(dir_name)])
            
            #move all data to the new dir where All the data is stored
            import shutil
            source_dir = os.path.join('C:/Users/alaa5/Desktop/499/interface/Final_FinalInterface/FinalInterface/', os.path.splitext(file.filename)[0])# pathe to the source_dir where the new data is stored
            file_names = os.listdir(source_dir)
            for file_name in file_names:
                shutil.move(os.path.join(source_dir, file_name), dir_name)
            
            #count the number of imges in the new data dir
            file_count = sum([len(files) for r, d, files in os.walk(dir_name)])
            coun=file_count - old_file_count
            
            return  render_template('B6.html',filename=filename,uplouded=coun)
            #return redirect(url_for('B6',filename=filename))
        
        error = "Please try again."
        return render_template('folderImg.html',error=error)
          
@app.route("/B6")
def B6():
  return render_template("B6.html")


#when say no from B2,return homePage 
@app.route("/HomePage")
def message():
  return render_template("HomePage.html")


#uplode one image to predict 
@app.route("/upload")
def upload_file():
   return render_template("upload.html")

@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
   error = None
   if request.method == 'POST':
        f = request.files['file']
        

        if f.filename == '':
           error = "Please try again."
           return render_template('upload.html',error=error) 
        else: 
           f.save(secure_filename(f.filename))
       
           filename = secure_filename(f.filename)
           image2 = load_img(filename, target_size=(224,224))
           from keras.preprocessing.image import img_to_array
           image = img_to_array(image2)
           image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2])) 
           predict_image=model.predict(image)
         
           if ((predict_image[0][0]) > (predict_image[0][1])):
             label="COVID-19"
             acc=str(int(predict_image[0][0]*100))+"%"#percentage
           else:
             label="NORMAL"
             acc=str(int(predict_image[0][1]*100))+"%"#percentage

           return render_template('result.html',lable=label,accuracy=acc)
     


if __name__ =="__main__":
  app.run(debug=True)