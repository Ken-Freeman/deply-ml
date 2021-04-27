Developing apps in Python:

The requirements.txt file will contain all necessary installs for the project.

Pickling ML models:
  - Load in your dataset
  - Fit a pipeline
    - use StandardScaler and SVC
  - Save the fitted pipeline/model to a     file by pickling it. Tips can be found here:  https://docs.python.org/3/library/pickle.html
  - Make sure to get some new testing data to test the pickled model with. I recomend holding out a few rows from the original dataset

Flask app:
  - To run the app use "flask run"
 

Deployed Model:
  This model is now hosted on heroku. If you would like to use this model you are now able to point at the heroku domain
   https://damp-sands-62687.herokuapp.com/



