from flask import Flask, request, jsonify, render_template
from utils import FlightPrice
import config

app = Flask(__name__)

@app.route('/flight_price')
def home1():
    
    return render_template('flight_price.html')



@app.route('/predict_charges', methods = ['GET', 'POST'])
def predict_charges():

    if request.method == 'GET':
        data = request.args.get
        print("Data :",data)
        
        airline = data("airline")
        source_city = data('source_city')
        departure_time = data('departure_time')
        stops = data('stops')
        arrival_time = data('arrival_time')
        destination_city = data('destination_city')
        class_ = data ('class_')
        duration = eval(data('duration'))
        days_left = int(data('days_left'))


        Obj = FlightPrice(airline,source_city,departure_time,stops,arrival_time,destination_city,class_,duration,days_left)
        pred_price = Obj.get_predicted_price()
        
        # return jsonify({"Result":f"Predicted Flight Price is == {pred_price}"})
        return render_template('flight_price.html', prediction = pred_price)

    elif request.method == 'POST':
        data = request.form
        print("Data :",data)
       
        airline = data["airline"]
        source_city = data['source_city']
        departure_time = data['departure_time']
        stops = data['stops']
        arrival_time = data['arrival_time']
        destination_city = data['destination_city']
        class_ = data ['class_']
        duration = data['duration']
        days_left = data['days_left']

        Obj = FlightPrice(airline,source_city,departure_time,stops,arrival_time,destination_city,class_,duration,days_left)
        pred_price = Obj.get_predicted_price()
        
        # return jsonify({"Result":f"Predicted Flight Price is == {pred_price}"})
        return render_template('flight_price.html', prediction = pred_price)

    return jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)
