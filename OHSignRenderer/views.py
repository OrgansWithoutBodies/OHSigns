import os 

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse,FileResponse
# from django.core.servers.basehttp import FileWrapper
from . import OHSoldSigns as signs


def loadTemplates():
    return signs.TEMPLATES.keys()

# 
def test(request):
    return request
def renderRequest(request,formobj,**kw):
    data={'n':(2,6),'lw':3,'res':100,'lblmethod':'random','numsheets':2}
    if request.method=='POST':
        form=formobj(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            data['n']=(data['nx'],data['ny'])
            data['lblmethod']='random'
        else:
            pass
    else:
        pass
    # fn=os.path.join(os.getcwd(),'renderedSigns','temp.pdf')
    f='temp.pdf'
    r=signs.renderSheets(n=data['n'],lw=data['lw'],barcode=data['barcode'],price=data['price'],orientation=data['orientation'],numrandspots=data['numrandspots'],res=data['res'],lblmethod=data['lblmethod'],numsheets=data['numsheets'],sides=data['sides'])
    fl,fn=signs.saveSheets(r,fn=f)
    
    # response=FileResponse(fl,as_attachment=True,filename='test.pdf')
    response=HttpResponse(open(fl.name,'rb+'),content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(fn)
    # response['X-Accel-Redirect'] = fn
    return response
"""
changeable filename
asynchronous waiting/ajax
    spinner while rendering
error handling
"""