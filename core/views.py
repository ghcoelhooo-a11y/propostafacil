# core/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def cliente_list(request):
    # depois ligamos no banco; agora só pra testar o layout
    return render(request, "clientes/cliente_list.html", {"clientes": []})
