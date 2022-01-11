from django.db.models.expressions import F
from django.http import JsonResponse,HttpResponseForbidden
from django.http.response import Http404
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
# Create your views here.
import json
from .forms import BooksForm
@csrf_exempt
def books(request):
    if(request.method == "POST"):
        book=BooksForm(request.POST)
        print(request.POST)
        if(book.is_valid()):
            book.save()
            print(book.cleaned_data)
            return JsonResponse(book.cleaned_data)
    if(request.method =='GET'):
        books=Book.objects.all().values()
        for b in books:
            b['authors']=b['authors'].split(',')
        
    return JsonResponse({"status_code": 200,"status": "success","data":list(books)},safe=False)

@csrf_exempt
def update_book(request,id):
    if(request.method=='POST'):
            
            req={}
            for i in request.POST:
                if i=='number_of_pages':
                    req[i]=request.POST[i][0]
                else:
                    req[i]=request.POST[i]
            Book.objects.filter(id=id).update(**req)
            obj=Book.objects.filter(id=id).values()
            return JsonResponse(list(obj)[0],safe=False)
    else:
        return HttpResponseForbidden()
@csrf_exempt
def delete_book(request,id):
    if request.method =='POST':
       obj=Book.objects.get(id=id) 
       Book.objects.filter(id=id).delete()
       return JsonResponse({
 "status_code": 200,
 "status": "success",
 "message": "The book "+obj.name+" was deleted successfully",
 "data": []
})

def show_book(request,id):
    obj=Book.objects.filter(id=id).values()
    return JsonResponse({
        "status_code": 200,
        "status": "success",
        "data": list(obj)[0]},safe=False)
    



