# DS-Project
WE WILL USE TKINTER
SYNOPSIS:
#1. we display a login page which asks for username and email id - these will be added to a table in database 
then and we ask for the number of unique players taking the quiz
we have a gui which displays the main menu with options as buttons and has online quiz as the title
1. Play    
2. Analysis  
3. Trivia   
4. Exit

if 1 is chosen: 
     b)then we make a landing page which displays a list of options for the area of interest of the user in which they want to take the quiz.
     areas will be : GK(mostly current affairs) , science and tech , sports , history , cultural and mixed
     c)each of the topics will have 10 questions randomly selected using the random module from a pool of *some very large number* of questions 
     Questions have been stored in list.
     d)the answers for each question given by the user will be recorded and the user will be given marks on that basis. These final score will be added to the table in the database alongside the user name and their emailid. We will only reveal the score at the end of the quiz to the user.
     e) there will be marks depending upon difficulty of question : 3 types of questions will exist -
     1. 3 easy(+1,0,0)  2. 4 medium (+3,0,0)  3. 3 difficult (+5,-1,0)
     f) these questions have been stored and tuple contains the difficulty level.
     g) each question will have 4 options.
     so quiz will be marked out of 30 and a percentage will be given to the user depending upon their score out of 30 and this percentage also added to the table
     h) all the data about time taken and other parameters will be stored in database and then ML and matplot to generate analysis.

if 2 is chosen:
     a) we will display the table which has records of all the players till date sorted in descending order acc to percentage (name , score , percentage)
     b) and maybe a graph using pandas too if time permits
	 c) ML?

if 3 is chosen :
     a) we will select a random fact from a pool of *very large number* of facts and display it using random module
     the page will have a DID YOU KNOW? as title.

if 4 is chosen : 
     a)quiz terminates

DATABASE will have 1 table :

1. a table with data of all users till date
2. table which store stats of the user for training model and extracting information
 
contents of the tables:
table 1 : name(varchar) email(varchar) score(int) percentage(int) 
table 2  : name(derived) question


ML INCOPORATION : 
incorporate machine learning into your quiz app to enhance the analysis of user performance. Here's a high-level overview of how you can integrate machine learning:

Collect Data: Gather data from users, including the time taken for each question, their chosen answers, and the corresponding correctness. You can store this data in a structured format such as a CSV file or a database.

Feature Engineering: Extract relevant features from the collected data that can potentially contribute to predicting user performance. This could include the time taken for each question, the difficulty level of the question, the user's previous quiz scores, or any other relevant information.

Model Training: Use the collected data and the engineered features to train a machine learning model. You can choose a suitable algorithm depending on your specific requirements, such as classification (to predict user performance level) or regression (to predict the time taken for each question).

Model Evaluation: Assess the performance of your trained model using appropriate evaluation metrics, such as accuracy, precision, recall, or mean squared error. This step helps ensure that your model is performing well and can make reliable predictions.

Predict User Performance: Apply the trained model to predict user performance based on their quiz data. For example, you can predict the time they might take to answer each question or categorize their performance as high, medium, or low.

Generate Insights: Utilize the machine learning predictions to generate personalized insights and recommendations for each user. For instance, you can provide suggestions to improve their time management skills or focus on specific question types where they tend to perform poorly.

Continuous Learning: Periodically update and retrain your machine learning model with new user data to improve its performance and adapt to changing user behaviors over time.
