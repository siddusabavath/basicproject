
from flask import Flask, render_template, request
import pickle
import numpy as np
filename = 'digital_eye.pkl'
model = pickle.load(open('digital_eye.pkl', 'rb'))
app = Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form.get('age'))
        sex=int(request.form.get('sex'))
        wearables= int(request.form.get('wearables'))
        duration = int(request.form.get('duration'))
        onlinepaltforms = int(request.form.get('onlineplatforms'))
        nature = int(request.form.get('nature'))
        gadgetsused = int(request.form.get('gadgetsused'))
        screenillumination = int(request.form.get('screen'))
        workingyears = int(request.form.get('workingyears'))
        circlaur = int(request.form.get('ciruclar'))
        noncirclaur = int(request.form.get('noncirclaur'))
        levelofgadjetwithrespecttoeyes = int(request.form.get('levelofgadjetwithrespecttoeyes'))
        Distancekeptbetweeneyesandgadjet = int(request.form.get('Distancekeptbetweeneyesandgadjet'))
        Avgnighttimeusageperday = int(request.form.get('Avgnighttimeusageperday'))
        Blinkingduringscreenusage = int(request.form.get('Blinkingduringscreenusage'))
        Difficultyinfocusingafterusingscreens = int(request.form.get('Difficultyinfocusingafterusingscreens'))
        freqquencyofcomplaints = int(request.form.get('freqquencyofcomplaints'))
        Severityofcomplaints = int(request.form.get('Severityofcomplaints'))
        rvis= int(request.form.get('RVIS'))
        Ocularsymptomsobservedlately = request.form.getlist('Ocularsymptomsobservedlately')
        n=0
        for i in Ocularsymptomsobservedlately:
              n=n*10
              n+=int(i)
        Ocularsymptomsobservedlately=n
        Symptomsobservingatleasthalfofthetimes=request.form.getlist('Symptomsobservingatleasthalfofthetimes')
        n=0
        for i in Symptomsobservingatleasthalfofthetimes:
              n=n*10
              n+=int(i)
        Symptomsobservingatleasthalfofthetimes=n
        Complaintsfrequency= int(request.form['Complaintsfrequency'])
        frequencyofdryeyes= int(request.form['frequencyofdryeyes'])
        data = np.array([[age,sex,wearables, duration,onlinepaltforms,nature,screenillumination,workingyears,circlaur,noncirclaur ,gadgetsused,levelofgadjetwithrespecttoeyes ,Distancekeptbetweeneyesandgadjet,Avgnighttimeusageperday,Blinkingduringscreenusage,Difficultyinfocusingafterusingscreens,freqquencyofcomplaints,Severityofcomplaints,rvis,Ocularsymptomsobservedlately,Symptomsobservingatleasthalfofthetimes,Complaintsfrequency,frequencyofdryeyes]])
        my_prediction = model.predict(data)
        l1=["Scimers1 in Left Eye:"+str(my_prediction[0][0]),"Scimers2 in Left Eye:"+str(my_prediction[0][1]),"Scimers1 in Right Eye:"+str(my_prediction[0][2]),"Scimers2 in Right Eye:"+str(my_prediction[0][3])]
        return render_template('results.html', prediction=l1)
if __name__ == '__main__':
	app.run()