
## utils file
import pickle
import json
import pandas as pd
import numpy as np
import config


class SalesPrice():
    def __init__(self,Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
       Item_MRP,Outlet_Establishment_Year, Outlet_Size,
       Outlet_Location_Type,Outlet_Type,Outlet_Identifier):
        self.Item_Weight = Item_Weight
        self.Item_Fat_Content = Item_Fat_Content
        self.Item_Visibility = Item_Visibility
        self.Item_Type=Item_Type
        self.Item_MRP = Item_MRP
        self.Outlet_Establishment_Year = Outlet_Establishment_Year
        self.Outlet_Size = Outlet_Size
        self.Outlet_Location_Type = Outlet_Location_Type
        self.Outlet_Type = Outlet_Type
        self.Outlet_Identifier = "Outlet_Identifier_"+Outlet_Identifier
        
        

    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):

        self.load_model()  # Calling load_model method to get model and json_data

        Outlet_Identifier_index = self.json_data['column'].index(self.Outlet_Identifier)
        array = np.zeros(len(self.json_data['column']))
        
        

        array[0]=self.Item_Weight
        array[1]=self.json_data["Item_Fat_Content"][self.Item_Fat_Content]
        array[2]=self.Item_Visibility
        array[3]=self.json_data['Item_Type'][self.Item_Type]
        array[4]=self.Item_MRP
        array[5]=self.Outlet_Establishment_Year
        array[6]=self.json_data["Outlet_Size"][self.Outlet_Size]
        array[7]=self.json_data["Outlet_Location_Type"][self.Outlet_Location_Type]
        array[8]=self.json_data["Outlet_Type"][self.Outlet_Type]
        
        array[Outlet_Identifier_index ]=1
        

        print("Test Array -->\n",array)
        predicted_charges = self.model.predict([array])[0]
        print("predicted_sales_charges",predicted_charges)
        return np.around(predicted_charges, 2)


if __name__ == "__main__":
    Item_Weight=9.300000
    Item_Fat_Content='Low Fat'
    Item_Visibility=0.016047
    Item_Type='Household'
    Item_MRP=249.809200
    Outlet_Establishment_Year=1999.000000
    Outlet_Size='Medium'
    Outlet_Location_Type='Tier 3'
    Outlet_Type='Supermarket Type1'
    Outlet_Identifier="OUT049"
    Outlet_Identifier_col="Outlet_Identifier_"+Outlet_Identifier


    med_ins = SalesPrice(Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
       Item_MRP,Outlet_Establishment_Year, Outlet_Size,
       Outlet_Location_Type,Outlet_Type,Outlet_Identifier)
    charges = med_ins.get_predicted_price()
    print()
    print(f"Predicted sales for the item {charges}/- Rs. Only")