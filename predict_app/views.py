from django.shortcuts import render
from .predict_disease import predict_heart_disease
# Create your views here.


def index(request):
    return render(request , 'predict_app/index.html')


def predict_system(request):
    context = {'message':"See Patient's Result Here!" , 'class': 'alert-info' }
    return render(request ,'predict_app/predict_system.html' , context)

def predict_system_result(request):
    data = request.POST


    age= float(data.get('age'))
    sex= float(data.get('gender'))
    cp= float(data.get('cp'))
    trtbps =  float(data.get('trestbps'))
    chol =  float(data.get('chol'))
    fbs =  float(data.get('fbs'))
    restecg = float(data.get('restecg'))
    thalach =  float(data.get('thalach'))
    exng =  float(data.get('exang'))
    oldpeak =float(data.get('oldpeak'))
    slp = float(data.get('slope'))
    ca = float(data.get('ca'))
    thal = float(data.get('thal'))
    new_data =  [ age , sex , cp , trtbps , chol , fbs , restecg , thalach, exng , oldpeak , slp , ca, thal]

    result = predict_heart_disease(new_data)
    if result == False:
        message = "Patient Do Not Seems to have issue related to heart disease, you may proceed to other diagnostic measures!"
        cl = "alert-success"
    else:
        message = "Patient Might be in danger of heart disease, please proceed to other diagnostic measures immediately!"
        cl = "alert-danger"

    context = {
    'result': result ,
     'message': message ,
     'class': cl ,
     'firstname': data.get('firstname'),
     'lastname' : data.get('lastname'),
     'address': data.get('address'),
     'sex' :  data.get('gender')
     }


    # print(request.POST.get('ca'))
    return render(request , 'predict_app/result.html' , context)



def about(request):
    return render(request , 'predict_app/about.html')
