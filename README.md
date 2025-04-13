# Student_Result_Analysis-
1. Project Overview
   Login Page:
   Username: admin
   Password: password
   Contains "Submit" and "Clear" buttons.

   Home Page:
   Displays an introduction about Student Result Analysis.
   Buttons for various visualizations.

   Graph Pages:
   Clicking a button redirects to a graph page displaying the respective analysis.

   Logout Option:
   Logs out the user and redirects to the login page.

2. Step-by-Step Guide to Running the Flask Project in Jupyter Notebook
   !pip install flask pandas matplotlib seaborn

   /Your_Project_Folder
   │── app.ipynb  (Your Jupyter Notebook file)
   │── app.py  (Flask application)
   │── templates/
   │   │── login.html
   │   │── home.html
   │   │── graph.html
   │── static/ 
   │   │── gender_distribution.png
   │   │── parent_education_vs_score.png
   │   │── parent_marital_status_vs_score.png
   │   │── ethnic_group_distribution.png
   │   │── math_score.png
   │   │── reading_score.png
   │   │── writing_score.png
   │── Downloads/archive (1)/Expanded_data_with_more_features.csv (Dataset)

   
