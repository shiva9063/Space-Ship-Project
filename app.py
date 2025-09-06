from flask import Flask,render_template,request
import pandas as pd
import joblib
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    prediction_result = None  # default

    if request.method == 'POST':
        # get all form values
        HomePlanet = request.form.get('HomePlanet')
        CryoSleep = request.form.get('CryoSleep')
        Destination = request.form.get('Destination')
        Age = request.form.get('Age')
        VIP = request.form.get('VIP')

        RoomService = request.form.get('RoomService')
        FoodCourt = request.form.get('FoodCourt')
        ShoppingMall = request.form.get('ShoppingMall')
        Spa = request.form.get('Spa')
        VRDeck = request.form.get('VRDeck')

        Deck = request.form.get('Deck')
        Num = request.form.get('Num')
        Side = request.form.get('Side')

        # values dictionary
        data = {
            'HomePlanet':[HomePlanet], 'CryoSleep':[CryoSleep],
            'Destination':[Destination], 'Age':[Age], 'VIP':[VIP],
            'RoomService':[RoomService], 'FoodCourt':[FoodCourt],
            'ShoppingMall':[ShoppingMall], 'Spa':[Spa], 'VRDeck':[VRDeck],
            'Deck':[Deck], 'Num':[Num], 'Side':[Side]
        }

        # make prediction
        try:
            df = pd.DataFrame(data)

            # Label encoding
            df['HomePlanet'] = df['HomePlanet'].map({'Earth':0,'Europa':1,'Mars':2})
            df['CryoSleep'] = df['CryoSleep'].map({'Yes':1,'No':0})
            df['VIP'] = df['VIP'].map({'Yes':1,'No':0})
            df['Destination'] = df['Destination'].map({'TRAPPIST-1e':0,'55 Cancri e':1,'PSO J318.5-22':2})
            df['Side'] = df['Side'].map({'S':0,'P':1})
            df['Deck'] = df['Deck'].map({'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'T':7})

            model = joblib.load('Model/model1')  # load model
            prediction_result = model.predict(df)[0]  # get first value 
            print(prediction_result)
        except Exception as e:
            prediction_result = f"Error: {e}"

    # render template with prediction result
    if prediction_result==0:
        return render_template('base.html', prediction='Not Transported')
    else:
        return render_template('base.html', prediction='Transported')
if __name__=='__main__':
    app.run(debug=True)