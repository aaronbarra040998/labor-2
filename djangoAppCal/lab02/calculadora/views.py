from django.shortcuts import render

def formulario(request):
    return render(request, 'calculadora/formulario.html')

def resultado(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        operacion = request.POST.get('operacion')

        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        else:
            resultado = 'Operación inválida'

        return render(request, 'calculadora/resultado.html', {'resultado': resultado})
