# AUTOMATED-COVID-19-DETECTION-USING-CHEST-X-RAY

The emerging coronavirus (SARS-CoV-2) is part of a series of coronaviruses that infect humans with respiratory diseases. The virus appeared in December of 2019 in China, and the World Health Organization announced its transformation into a global epidemic pandemic that affects many countries in the world. Coronavirus is transmitted through direct contact with an infected person or by touching a surface. Currently, patients of COVID-19 are diagnosed by reverse transcription-polymerase chain reaction (RT-PCR), this test is expensive and requires a professional medical staff to get the result correctly. Therefore, X-ray imaging is the proposed solution which is an automatic support tool that was made to be the first line to diagnose corona infection while taking (RT-PCR) test to confirm the result of the X-ray imaging.
The aim of this project is to build a website that will demonstrate the functionalities of the algorithm of this project. The wesite still on woking and not realeased yet.The dataset of X-ray images was collected from several public datasets with a total of 4658 chest X-ray images, 2329 of them were COVID-19 X-ray images and the other 2329 X-ray images were a normal chest. The models were chosen after analysis of several studies, seven models were selected which are InceptionResNetV2, InceptionV3, ResNet50, MobileNetV2, DenseNet201, and VGG19, and tested on three different datasets and one of them is our dataset. The result shows that VGG19 has the best performance with an accuracy of 99%. 



## 1. How to run the model?
- Upload the "VGG19.py" to Google Collab.

- Chang the path in line 38 and 39 to its current path either stored in Google drive or the local drive.

- Run the python code.



## 2. How to run the website?
- Open “test.py” file and change the path of three files:
  
     - line 12: change the file path to website > VGG19.h5
  
     - line 53: change the path to the directory of website > data 
      
            i. If the file did not exist then create a new empty folder with the name of "data"
  
     - line 58: change the path to the directory of the website folder
    
- Open command prompt
     
     - Chang the directory to the website folder, by typing [cd C:/<path>/wbsite]
  
     - Run the "test.py", by typing [python “test.py”]
     
            i. You may need to install flask packages on your devise before running the website by typing [pip install flask].
     
            ii. Additional python packages and libraries may be needed to be installed in order to run the code properly.

- Copy the generated HTTP link as shown in the following figure to any browser and explore the website.

    ![لقطة الشاشة 2021-04-23 024602](https://user-images.githubusercontent.com/61123403/115798093-19738380-a3de-11eb-8849-f4e31e6756de.png)
     
- To exit the virtual environment press CTRL+C


## Contact

Do not hesitate to contact with the team members if you have any questions. 

- Juwaireyya Mohammed Aljohani, `juwaireyyaaljohani@gmail.com`

- Alaa Abdullah Alotaibi

- Razan Mohammed Alsolami

