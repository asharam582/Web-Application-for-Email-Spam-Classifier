from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
cv=pickle.load(open("models/cv.pkl",'rb'))
clf=pickle.load(open("models/clf.pkl","rb"))

@app.route('/')
def home():
    # text=""
    # if request.method=="POST":
    #     text=request.form.get('email-content')
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    email=request.form.get('email-content')
    vectorised_mail=cv.transform([email])
    prediction=clf.predict(vectorised_mail)
    prediction=1 if prediction==1 else -1
    return render_template('index.html',prediction=prediction,email=email)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
