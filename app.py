from flask import Flask, escape, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

model = pickle.load(open("model.pkl", 'rb'))

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method =="POST":
        gender = request.form['gender']
        age = int(request.form['age'])
        alcoholdrinking = int(request.form['alcoholdrinking'])
        stroke = int(request.form['stroke'])
        diffwalking = int(request.form['diffwalking'])
        diabetic = int(request.form['diabetic'])
        physicalactivity = int(request.form['physicalactivity'])
        asthma = int(request.form['asthma'])
        kidneydisease = int(request.form['kidneydisease'])
        skincancer = int(request.form['skincancer'])
        work = request.form['work']
        residence = request.form['residence']
        glucose = float(request.form['glucose'])
        bmi = float(request.form['bmi'])
        smoking = request.form['smoking']

        # gender
        if (gender == "Male"):
            gender_male=1
            gender_other=0
        elif(gender == "Other"):
            gender_male = 0
            gender_other = 1
        else:
            gender_male=0
            gender_other=0
        
        # work  type
        if(work=='Self-employed'):
            work_type_Never_worked = 0
            work_type_Private = 0
            work_type_Self_employed = 1
            work_type_children=0
        elif(work == 'Private'):
            work_type_Never_worked = 0
            work_type_Private = 1
            work_type_Self_employed = 0
            work_type_children=0
        elif(work=="children"):
            work_type_Never_worked = 0
            work_type_Private = 0
            work_type_Self_employed = 0
            work_type_children=1
        elif(work=="Never_worked"):
            work_type_Never_worked = 1
            work_type_Private = 0
            work_type_Self_employed = 0
            work_type_children=0
        else:
            work_type_Never_worked = 0
            work_type_Private = 0
            work_type_Self_employed = 0
            work_type_children=0

        # residence type
        if (residence=="Urban"):
            Residence_type_Urban=1
        else:
            Residence_type_Urban=0

        # smoking status
        if(smoking=='formerly smoked'):
            smoking_status_formerly_smoked = 1
            smoking_status_never_smoked = 0
            smoking_status_smokes = 0
        elif(smoking == 'smokes'):
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 0
            smoking_status_smokes = 1
        elif(smoking=="never smoked"):
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 1
            smoking_status_smokes = 0
        else:
            smoking_status_formerly_smoked = 0
            smoking_status_never_smoked = 0
            smoking_status_smokes = 0

        feature = scaler.fit_transform([[age, alcoholdrinking, stroke,diffwalking,diabetic, physicalactivity, asthma,kidneydisease,skincancer, glucose, bmi, gender_male, gender_other, work_type_Never_worked, work_type_Private, work_type_Self_employed, work_type_children, Residence_type_Urban,smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_smokes]])

        prediction = model.predict(feature)[0]
        # print(prediction) 
        # 
        if prediction==1:
            prediction = "Yes" 
        else:
            prediction = "No" 

        return render_template("index.html", prediction_text="Chance of Heart Disease --> {}".format(prediction))   
         

    else:
        return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)