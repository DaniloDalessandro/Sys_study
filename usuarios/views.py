from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render(request,'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            return render('/usuarios/cadastro')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            return redirect('/usuarios/cadastro')

        try:
            User.objects.create_user(
                username=username,
                password=senha
            )
            return
        except:
            return redirect('/usuarios/cadastro')

