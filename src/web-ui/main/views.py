from django.shortcuts import render


def index(request):
    return render(request,'main/index.html')

def plk(request):
    return render(request,'main/plk.html')

def upload(request):
    for key, file in request.FILES.items():
        path = "../dcn/orchestrator/scripts/" + file.name
        dest = open(path, 'wb')
        if file.multiple_chunks:
            for c in file.chunks():
                dest.write(c)
        else:
            dest.write(file.read())
        dest.close()
    return render(request,'main/plk.html')