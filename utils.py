import pickle
import json
import numpy as np
import config

class FlightPrice():
    def __init__(self,airline,source_city,departure_time,stops,arrival_time,destination_city,class_,duration,days_left):
        print("****** INIT Function *********")
        self.airline= airline
        self.source_city = source_city
        self.departure_time = departure_time
        self.stops = stops
        self.arrival_time = arrival_time
        self.destination_city = destination_city 
        self.class_ = class_
        self.duration = duration
        self.days_left = days_left
       
    
    def __load_saved_data(self):
        
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)


    def get_predicted_price(self):
        self.__load_saved_data()

        airline = self.json_data['airline'][self.airline]
        source_city = self.json_data['source_city'][self.source_city]
        departure_time = self.json_data['departure_time'][self.departure_time]
        stops = self.json_data['stops'][self.stops]
        arrival_time = self.json_data['arrival_time'][self.arrival_time]
        destination_city = self.json_data['destination_city'][self.destination_city]
        class_ = self.json_data['class_'][self.class_]
        
    
        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = airline
        test_array[0,1] = source_city
        test_array[0,2] = departure_time
        test_array[0,3] = stops
        test_array[0,4] = arrival_time
        test_array[0,5] = destination_city
        test_array[0,6] = class_
        test_array[0,7] = self.duration
        test_array[0,8] = self.days_left


        predicted_price = np.around(self.model.predict(test_array)[0],3)
        return predicted_price