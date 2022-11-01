# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 12:30:40 2022

@author: Emmanuel Maseruka
"""
import pandas as pd
music_data=pd.read_csv('C:/Users/Kevin Meng/OneDrive/Desktop/Python/music.csv')  #use panda to read data as data frame

##df.shape  ##shows structure of df
##df.describe() ##returns each column mean count std etc
##df.values() ##returns arrays of each row

x = music_data.drop(columns=['genre']) ##input dataset
y = music_data['genre'] ##output dataset

from sklearn.tree import DecisionTreeClassifier ##clasify data
from sklearn.model_selection import train_test_split ##split data into train & test set
from sklearn.metrics import accuracy_score ##used to test accuracy of model
import joblib ##used to store tested model
from sklearn import tree ##visualise model

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2)



model = DecisionTreeClassifier()
model.fit(x_train,y_train) #test model

joblib.dump(model, 'music-recomender.joblib') ##storing our model

model = joblib.load('music-recomender.joblib') ##loads model again


predictions = model.predict([[21,1],[22,0]])

predictions = model.predict(x_test)

score = accuracy_score(y_test, predictions)

tree.export_graphviz(model, out_file='music-recomender.dot',feature_names=['age','gender'], class_names=sorted(y.unique()),label='all',rounded=True,filled=True)

#filled--makes node have color
#rounded--makes nodes have rounded corners
#label--labels nodes
#class names--display the category of y
#feature names--see rules in nodes

##My Program that predicts

customer_age = input("What is your age? ")
customer_age = int(customer_age)

customer_gender = input("What is your gender (M/F)? ")

if customer_gender=="M":
    customer_gender = 1
else: customer_gender = 0

model = joblib.load('music-recomender.joblib')

guess=model.predict([[customer_age,customer_gender]])
print("Since you are " + str(customer_age) + " and " + str(customer_gender) + ",your music is "+ guess )



### CREDIT CARDS NOW  ##Get your credit card

import pandas as pd
#music_data=pd.read_csv('C:/Users/Kevin Meng/OneDrive/Desktop/Python/test.csv')  #use panda to read data as data frame


music_data=pd.read_csv('C:/Users/Kevin Meng/OneDrive/Desktop/Python/train.csv') 


x = music_data.drop(columns=['ID','Good0/Bad1']) ##input dataset
y = music_data['Good0/Bad1'] ##output dataset

from sklearn.tree import DecisionTreeClassifier ##clasify data
from sklearn.model_selection import train_test_split ##split data into train & test set
from sklearn.metrics import accuracy_score ##used to test accuracy of model
import joblib ##used to store tested model
from sklearn import tree ##visualise model

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.2)



model = DecisionTreeClassifier()
model.fit(x_train,y_train) #test model

joblib.dump(model, 'music-recomender.joblib') ##storing our model

model = joblib.load('music-recomender.joblib') ##loads model again


name=input("Insert your name: ")
print("Welcome to Bank of America " + name + ". Please insert your details")

gender = input("What is your gender (M/F)? ")

if gender=="M":
    gender = 1
else:gender = 0

car = input("Do you have a car (Y/N)? ")

if car=="Y":
    car = 1
else:car = 0


realty = input("Do you have realty (Y/N)? ")

if realty=="Y":
    realty = 1
else:realty = 0


children = input("How many children do you have? ")
children = int(children)

income = input("How much USD do you make a year? ")
income = int(income)


income_type = input("Choose a letter (A,B,C,D,E) that represents your income type. A: Commercial Associate B: Pensioner C: State Servant D: Student E: Working ")
if income_type=="A":
    income_type= 1
    if income_type =="B":
            income_type= 2
            if income_type =="C":
                income_type=3
                if income_type=="D":
                        income_type=4
else: income_type = 5


education= input("Choose a letter (A,B,C,D,E) that represents your Education level. A: Academic Degree B: Higher Education C: Incomplete higher D: Lower secondary E: Secondary Special ")

if education=="A":
    education= 1
    if education =="B":
            education= 2
            if education =="C":
                education=3
                if education=="D":
                        education=4
else: education = 5


family_status= input("Choose a letter (A,B,C,D,E) that represents your family status. A: Civil Marriage B: Married C: Separated D: Single/not married E: Widow ")

if family_status=="A":
    family_status= 1
    if family_status =="B":
        family_status= 2
        if family_status =="C":
            family_status=3
            if family_status=="D":
                family_status=4
else: family_status = 5


housing_type= input("Choose a letter (A,B,C,D,E,F) that represents your Housing type. A: Co-op apartment B: House/apartment C: Municipal Apartment D: Office Apartment E: Rented apartment F: With parents ")

if housing_type=="A":
    housing_type= 1
    if housing_type =="B":
        housing_type= 2
    if housing_type =="C":
        housing_type=3
    if housing_type=="D":
        housing_type=4
    if housing_type=="E":
        housing_type=5
else: housing_type = 6


mobile= input("Do you have mobile (Y/N)? ")

if mobile=="Y":
    mobile = 1
else:mobile = 0
work_phone= input("Do you have work phone (Y/N)? ")

if work_phone=="Y":
    work_phone = 1
else:work_phone = 0
phone= input("Do you have home phone (Y/N)? ")

if phone=="Y":
    phone = 1
else:phone = 0
email= input("Do you have an email (Y/N)? ")

if email=="Y":
    email = 1
else:email = 0

Num_family= input("How many family members do you have? ")
Num_family=int(Num_family)


dob=input("How old are you? ")
dob=int(dob)*365
predictions = model.predict([[gender,car,realty,children,income,income_type,education,family_status,housing_type,mobile,work_phone,phone,email,Num_family,dob]])

print("Dear "+ name+", based on your application documents, the bank considers your credit card application to be "+predictions)

predictions = model.predict(x_test)

score = accuracy_score(y_test, predictions)
print(score)
tree.export_graphviz(model, out_file='music-recomender1.dot',feature_names=["Good0/Bad1","CODE_GENDER","FLAG_OWN_CAR"
,"FLAG_OWN_REALTY"
,"CNT_CHILDREN"
,"AMT_INCOME_TOTAL"
,"NAME_INCOME_TYPE"
,"NAME_EDUCATION_TYPE"
,"NAME_FAMILY_STATUS"
,"NAME_HOUSING_TYPE"
,"FLAG_MOBIL"
,"FLAG_WORK_PHONE"
,"FLAG_PHONE"
,"FLAG_EMAIL"
,"CNT_FAM_MEMBERS"
,"DAYS_BIRTH"
], class_names=sorted(y.unique()),label='all',rounded=True,filled=True)







from turtle import d
color("red")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
turtle.done()
turtle.bye()




import turtle
wn=turtle. Screen()
wn. bgcolor("black")
wn. title("Emmanuel")






float c=0;
float n=0;
void setup() {
    size(1000,800);
    colorMode(HSB,225);
    noFill();
    }

void draw() {
    background(0);
    c +=0.2;
    float x = width/2;
    float y = height/2;
    for(int i = 0; i<100; i++) {
            float p= pow(0.92,i);
            float r = 3*noise((i+c)*0.03)*TAU;
            x+=cos(r)*8;
            y+=sin(r)*8;
            stroke((n+i*2)%255,y,x);
            strokeWeight(10*p);
            rect(x,y,p*1168,p*834,40);
            n+=0.01;
            
            }
    }




void drawRedCircle(float circleX, float circleY, float circleDiameter) {
  fill(255, 0, 0);
  ellipse(circleX, circleY, circleDiameter, circleDiameter);
}









