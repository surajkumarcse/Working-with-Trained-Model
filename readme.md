The Model is already built at https://www.kaggle.com/emmarex/plant-disease-detection-using-keras/output

In this project, you don't need to train the model by wasting your GPU resources or computational power. We are using the model given in the above link. 

Steps to use this model: 
1. Create a folder with name 'project'
2. Go to the above link[https://www.kaggle.com/emmarex/plant-disease-detection-using-keras/output] and download cnn_model.pkl and save in your project folder in step 1.
3. Download this repo in your project folder.
4. Create an environment in your terminal:
    python -m venv myvenv
5. Download all the dependencies needed to run this repo
    pip install -r requirements.txt
6. now in other terminal run with same folder location:
    source myvenv/bin/activate
    jupyter notebook
    This will open a new tab in your browser
7. Open processingModel.ipynb in that jupyter notebook
8. go to Cell > run all.
9. I hope, at the end it will ouput 'Potato___healthy' because we have used 'potato__healthy.jpeg' as our input to this model in IN[15] of this jupyter notebook.
10. You can also use your images by pasting the image in this folder and replacing the name of the image in IN[15] of previous step.
11. If it helps you, make sure to STAR this repo.

Happy Coding
Suraj