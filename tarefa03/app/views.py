from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    user_list = [
        {"nome": "Anny", "matricula": "1234", "idade": 17, "cidade":"Santa Maria"},
        {"nome": "Júlia", "matricula": "1324", "idade": 43, "cidade":"São Tomé"},
        {"nome": "Gabriela", "matricula": "4767", "idade": 23, "cidade":"Natal"},
        {"nome": "Gabriel", "matricula": "8445", "idade": 8, "cidade": "Macaiba"},
        {"nome": "Alessandro", "matricula": "3453", "idade": 36, "cidade":"Sydney"},
    ]

    context = {
        "usuarios": user_list,
    }
    return render(request, "usuarios.html", context)