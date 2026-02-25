from django.shortcuts import render

def calculate_total(request):
    P = 0
    G = 0
    T = 0

    if request.method == "POST":
        P = int(request.POST.get('price', 0))
        G = int(request.POST.get('gst', 0))
        T = P + (P * G / 100)

        print("Price =", P)
        print("GST =", G)
        print("Total =", T)

    return render(request, 'myapp/ssp.html', {'price': P,'gst': G,'total': T})