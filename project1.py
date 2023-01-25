from fastapi import FastAPI
import uvicorn
import pickle

app = FastAPI(debug = True)

@app.get('/')
def home( ):
    return {'text': 'chrn preduction solution'}
    

    
@app.get('/predect')
def predect(day_charge: str,evening_charge : str,night_charge:str,international_charge: str,total_charge: str,
            voice_mail_plan: str,international_plan: str,day_calls: str,evening_calls: str,night_calls: str,
            international_calls: str,customer_service_calls: str,voice_mail_messages: str,day_mins: str, 
            evening_mins: str, night_mins: str,international_mins: str,account_length: str):
    
    model = pickle.load(open('C:/Users/hp/DS_Project/model_pickle','rb'))
    makepredection = model.predict([[day_charge,evening_charge ,night_charge,international_charge,total_charge,
                                     voice_mail_plan,international_plan,day_calls,evening_calls,night_calls,
                                     international_calls,customer_service_calls,voice_mail_messages,day_mins,
                                     evening_mins, night_mins,international_mins,account_length]])
    
    output = round(makepredection[0],2)
    return {'churn'.format(output)}

if __name__ == '__main__':
    uvicorn.run(app)