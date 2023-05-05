# DS-Project
WE WILL USE TKINTER
SYNOPSIS:
#1. we display a login page which asks for username and email id - these will be added to a table in database 
then and we ask for the number of unique players taking the quiz
we have a gui which displays the main menu with options as buttons and has online quiz as the title
1. Play    2.Leaderboard  3.Trivia   4.exit

if 1 is chosen: 
     b)then we make a landing page which displays a list of options for the area of interest of the user in which they want to take the quiz and will ask the users to play to their strengths
     areas will be : GK(mostly current affairs) , science and tech , sports , history , cultural and mixed
     c)each of the topics will have 10 questions randomly selected using the random module from a pool of 20 questions 
     #PROBLEM - HOW TO STORE QUESTIONS AND THEIR ANSWERS - mysql? ds?
     d)the answers for each question given by the user will be recorded and the user will be given marks on that basis. These final score will be added to the table in the database alongside the user name and their emailid. We will only reveal the score at the end of the quiz to the user.
     e) there will be marks depending upon difficulty of question : 3 types of questions will exist -
     1. 3 easy(+1,0,0)  2. 4 intermediate (+3,0,0)  3. 3 difficult (+5,-1,0)
     f)these questions will also be stored in the data structure acc to their difficulty and accordingly called
     g)each question will have 4 options.
     so quiz will be marked out of 30 and a percentage will be given to the user depending upon their score out of 30 and this percentage also added to the table.
     h)then we will again go back to login screen and perform same thing for the 2nd user and 3rd user depending upon the initial input
     i)now the users will be sorted acc to their percentage and a winner will be declared - we can make this into a 1V1 or tri series
     the winner's name and their score willl be displayed along with an option to view a detailed analysis of their answers. here we will display their submitted answer for each question and the correct answer of that question in case it is wrong and the marks obtained per question acc to the question number.

if 2 is chosen:
     a) we will display the table which has records of all the players till date sorted in descending order acc to percentage (name , score , percentage)
     b) and maybe a graph using pandas too if time permits

if 3 is chosen :
     a) we will select a random fact from a pool of 20 facts and display it using random module
     the page will have a DID YOU KNOW?

if 4 is chosen : 
     a)quiz terminates

DATABASE will have 2 tables :
1. the table which will consist of the current users 
2. a table with data of all users till date

contents of the tables:
name(varchar) email(varchar) score(int) percentage(int) 
