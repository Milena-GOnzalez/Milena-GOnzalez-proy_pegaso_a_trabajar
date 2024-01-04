from django.shortcuts import render

def holamundo(request): 
    nombre = "Milena"
    apellido = "Romero"
    tel = "3106635387"
    context={
        'nombres' :nombre,
        'apellidos' : apellido,
        'telefono' : tel,
}
    
    return render(request, "index.html", context)
