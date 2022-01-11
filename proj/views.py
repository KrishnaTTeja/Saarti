from django.http import JsonResponse
import pip._vendor.requests as requests

def specific_book(request,name):
    url='https://www.anapioficeandfire.com/api/books?name='+name
    r=requests.get(url)
    data=r.json()
    remove=['characters',"povCharacters",'url']
    for book in data:
        for i in remove:
            book.pop(i)
        book["release_date"]=book.pop('released')
    return JsonResponse({
        "status_code":200,
        "status":'success',
        "data":data
    })
