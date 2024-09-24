from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('random_forest_model.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('WEB API.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Lane_Type = int(request.form['Lane_Type'])
        Vehicle_Dimensions = int(request.form['Vehicle_Dimesions'])
        Amount_paid = int(request.form['Amount_paid'])
        Transaction_Amount = int(request.form['Transaction_Amount'])
        Vehicle_Speed = int(request.form['Vehicle_Speed'])

        region = request.form['Vehicle_Type']
        if (Vehicle_Type == 'Bus'):
            Bus = 1
            Car = 0
            Motorcycle = 0
            SUV = 0
            Sedan = 0
            Truck = 0
            Van = 0
        elif (Vehicle_Type == 'Car'):
            Bus = 0
            Car = 1
            Motorcycle = 0
            SUV = 0
            Sedan = 0
            Truck = 0
            Van = 0
        elif (Vehicle_Type == 'Motorcycle'):
            Bus = 0
            Car = 0
            Motorcycle = 1
            SUV = 0
            Sedan = 0
            Truck = 0
            Van = 0
        elif (Vehicle_Type == 'SUV'):
            Bus = 0
            Car = 0
            Motorcycle = 0
            SUV = 1
            Sedan = 0
            Truck = 0
            Van = 0
        elif (Vehicle_Type == 'Sedan'):
            Bus = 0
            Car = 0
            Motorcycle = 0
            SUV = 0
            Sedan = 1
            Truck = 0
            Van = 0 
        elif (Vehicle_Type == 'Truck'):
            Bus = 0
            Car = 0
            Motorcycle = 0
            SUV = 0
            Sedan = 0
            Truck = 1
            Van = 0 
        else:
            Bus = 0
            Car = 0
            Motorcycle = 0
            SUV = 0
            Sedan = 0
            Truck = 0
            Van = 1 


        values = np.array([[Lane_Type,Vehicle_Dimensions,Amount_paid,Transaction_Amount,Vehicle_Speed,Bus,Car,Motorcycle,SUV,Sedan,Truck,Van]])
        prediction = model.predict(values)
        prediction = round(prediction[0],2)


        return render_template(prediction_text='Fastag Fraud Detection cost is {}'.format(prediction))


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
    # app.run(debug=True)



