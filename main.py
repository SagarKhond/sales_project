
from flask import Flask, jsonify, render_template, request
from model.utils import  SalesPrice
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("We are in Sales Price Prediction")
    return render_template("index.html")


@app.route('/predict_charges',methods=["POST","GET"])
def get_car_price():
    if request.method=="GET":
        print("we are in GET method")
        Item_Weight =eval(request.args.get("Item_Weight"))
        Item_Fat_Content =(request.args.get("Item_Fat_Content"))
        Item_Visibility = eval(request.args.get("Item_Visibility"))
        Item_Type =(request.args.get("Item_Type"))
        Item_MRP =(request.args.get("Item_MRP"))
        Outlet_Establishment_Year =eval(request.args.get("Outlet_Establishment_Year"))
        Outlet_Size = (request.args.get("Outlet_Size"))
        Outlet_Location_Type = (request.args.get("Outlet_Location_Type"))
        Outlet_Type =(request.args.get("Outlet_Type"))
        Outlet_Identifier =(request.args.get("Outlet_Identifier"))

        med_ins = SalesPrice(Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
       Item_MRP,Outlet_Establishment_Year, Outlet_Size,
       Outlet_Location_Type,Outlet_Type,Outlet_Identifier)
        charges = med_ins.get_predicted_price()
        return render_template("index.html",prediction=charges)

    else:
        print("we are in POST method")
        Item_Weight = eval(request.form.get("Item_Weight"))
        Item_Fat_Content =(request.form.get("Item_Fat_Content"))
        Item_Visibility = eval(request.form.get("Item_Visibility"))
        Item_Type =(request.form.get("Item_Type"))
        Item_MRP =(request.form.get("Item_MRP"))
        Outlet_Establishment_Year =eval(request.form.get("Outlet_Establishment_Year"))
        Outlet_Size = (request.form.get("Outlet_Size"))
        Outlet_Location_Type = (request.form.get("Outlet_Location_Type"))
        Outlet_Type =(request.form.get("Outlet_Type"))
        Outlet_Identifier =(request.form.get("Outlet_Identifier"))

        med_ins = SalesPrice(Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
       Item_MRP,Outlet_Establishment_Year, Outlet_Size,
       Outlet_Location_Type,Outlet_Type,Outlet_Identifier)
        charges = med_ins.get_predicted_price()
        return render_template("index.html",prediction=charges)


       

    
        
    # print("we are in car price prediction")
    # data=request.form
    # Item_Weight=eval(data["Item_Weight"])
    # Item_Fat_Content=(data["Item_Fat_Content"])
    # Item_Visibility=eval(data["Item_Visibility"])
    # Item_Type=(data["Item_Type"])
    # Item_MRP=(data["Item_MRP"])
    # Outlet_Establishment_Year=eval(data["Outlet_Establishment_Year"])
    # Outlet_Size=(data["Outlet_Size"])
    # Outlet_Location_Type=(data["Outlet_Location_Type"])
    # Outlet_Type=(data["Outlet_Type"])
    # Outlet_Identifier=(data["Outlet_Identifier"])
    

    
    # med_ins = SalesPrice(Item_Weight,Item_Fat_Content,Item_Visibility,Item_Type,
    #    Item_MRP,Outlet_Establishment_Year, Outlet_Size,
    #    Outlet_Location_Type,Outlet_Type,Outlet_Identifier)
    # charges = med_ins.get_predicted_price()
    # return jsonify({"Result" :f"Predicted Sales of Item {charges}/- Rs. Only"})

    
    # if request.method == "GET":
    #     print("we are in GET method")

    #     age = eval(request.args.get("age"))
    #     sex = request.args.get("sex")
    #     bmi = eval(request.args.get("bmi"))
    #     children = eval(request.args.get("children"))
    #     smoker = request.args.get("smoker")
    #     region =request.args.get("region")
    #     med_ins = MedicalInsurance(age, sex, bmi,children, smoker, region)
    #     charges = med_ins.get_predicted_price()
    #     return render_template("index.html",prediction=charges)

    # else:
    #     print("we are in POST method")

    #     age = eval(request.form.get("age"))
    #     sex = request.form.get("sex")
    #     bmi = eval(request.form.get("bmi"))
    #     children = eval(request.form.get("children"))
    #     smoker = request.form.get("smoker")
    #     region =request.form.get("region")
    #     med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    #     charges = med_ins.get_predicted_price()
    #     return render_template("index.html",prediction=charges)

    

      

        
if __name__=="__main__":
 app.run(host='0.0.0.0' , port=5000, debug=True)
      
          