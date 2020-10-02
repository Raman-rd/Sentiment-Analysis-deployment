from flask import Flask,render_template,request
import pickle
import sklearn
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result',methods=['GET','POST'])
def predict():
    text = [request.args.get("raw")]
    tf = cv.transform(text)
    p = model.predict(tf)
    if p ==0:
        p = "Negative"
    else:
        p="Positive"
    return render_template("result.html",p=p)

if __name__=="__main__":
    with open("countvec.pkl","rb") as f:
        cv = pickle.load(f)
    with open("model.pkl","rb") as f:
        model = pickle.load(f)
    app.run()
