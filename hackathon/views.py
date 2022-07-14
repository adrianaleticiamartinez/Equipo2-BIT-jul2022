
import pandas as pd

from django.http import HttpResponseRedirect
from django.http import HttpResponse 

from django.shortcuts import redirect, render

# Nos permitira conocer si hay un usuario
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required

from clientes.models import Cliente
from users.models import User


from .forms import ManageCSVForm, UploadFileForm

@login_required
def index(request):

    User_authenticated = get_user(request)

    clientes = Cliente.objects.all().order_by('-id')

    
    # User_authenticated.groups.get()



    context = {
         'message': 'Lista de productos',
         'title': 'Título',
         'user_group': str(User_authenticated.groups.get()),
         'clientes': clientes
     }

    return render(request, 'index.html', context)

@login_required
def data_view(request):

    form = UploadFileForm(request.POST, request.FILES)

    if request.method == 'POST' and form.is_valid():
        df = pd.read_csv(form.cleaned_data.get('file'), sep=',')

        for i in range(df.shape[0]):
            Cliente.objects.create(
            idCliente = df.iloc[i]['idCliente'], 
            nombre = df.iloc[i]['nombre'], 
            apellidoPaterno = df.iloc[i]['apellidoPaterno'], 
            apellidoMaterno = df.iloc[i]['apellidoMaterno'], 
            fechaNacimiento = df.iloc[i]['fechaNacimiento'], 
            sexo = df.iloc[i]['sexo'], 
            segmento = df.iloc[i]['segmento'], 
            nacionalidad = df.iloc[i]['nacionalidad'], 
            rfc = df.iloc[i]['rfc'],             
            tipoID = df.iloc[i]['tipoID'],
            numeroID = df.iloc[i]['numeroID'],
            cuenta = df.iloc[i]['cuenta'], 
            email = df.iloc[i]['email'], 
            )

        # df.iloc[:,0].apply(lambda x: Cliente.objects.create(
        #     idCliente = x.split(',')[0], 
        #     nombre = x.split(',')[1], 
        #     apellidoPaterno = x.split(',')[2], 
        #     apellidoMaterno = x.split(',')[3], 
        #     fechaNacimiento = x.split(',')[4], 
        #     sexo = x.split(',')[5], 
        #     segmento = x.split(',')[6], 
        #     nacionalidad = x.split(',')[7], 
        #     rfc = x.split(',')[8], 
        #     tipoID = x.split(',')[9], 
        #     cuenta = x.split(',')[10], 
        #     # email = x.split(',')[11],             
        # ))
        print(df)

        messages.success(request, 'Clientes agregados')
        return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'data.html', context)

def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(username=username, password=password)
        if user: 
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')   
            

    context = {}
    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada')
    return redirect('login')

