# AUTOMATED-COVID-19-DETECTION-USING-CHEST-X-RAY

**How to run the website?**
1. Open “test.py” file and change the path of three files:
  
    a. line 12: change the file path to website > VGG19.h5
  
    b. line 53: change the path to the directory of website > data 
      
        i. if the file did not exist then create a new empty folder with the name of "data"
  
    c. line 58: change the path to the directory of the website folder
    
2. Open command prompt
  a. Chang the directory to the website folder, by typing [cd C:/<path>/wbsite]
  
  b. Run the "test.py", by typing [python “test.py”]
     
     i. You may need to install flask packages on your devise before running the website by typing [pip install flask].
     
     ii. Additional python packages and libraries may be needed to be installed in order to run the code properly.

3. Copy the generated HTTP link as shown in the following figure to any browser and explore the website.


4. To exit the virtual environment press CTRL+C

**How to run the model?**
1. Upload the "VGG19.py" to Google Collab.

2. Chang the path in line 38 and 39 to its current path either stored in Google drive or the local drive.

3. Run the python code.
