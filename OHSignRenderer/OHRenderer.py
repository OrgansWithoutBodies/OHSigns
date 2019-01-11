"""
@TODOs:
    Each mod has unique inputs from WebInterface
    
    underlines - 
       'after','under','before','above'...
"""
from PIL import Image, ImageDraw, ImageFont#Python's Image Library 

class Module(object):#graphical object representing certain aspect of sign, can contain other modules - has css-like attributes & pseudo-elements
    def __init__(self,c,modsize=None,bar=None,rot=None,submodules=None,modname=None,*args,**kw):
        self.c=c
        self.atts={}
        self.inputs={}



class TextModule(Module):
    def __init__(self,text,font,size,justification,**kw):
        self.inputs.add({''})

class BarcodeModule(Module):
    def __init__(self,code,dims,encoding='128',**kw):
        pass

class ShapeModule(Module):
    def __init__(self,type,**kw):
        pass
    
class subModule(Module):
    def __init__(self,N,**kw):
        pass
class FrameModule(Module):
    def __init__(self,N,**kw):
        pass
class GridModule(Module):
    def __init__(self,N,sub,labels,**kw):
        pass
class SheetModule(Module):
    def __init__(self,res,**kw):
        pass



def renderSign():
	pass

def centertext(d,font,justify='center',line=0,autopar=False):        
  
    for string in d.keys():
        locrat=d[string]
        attsize=ImageDraw.ImageDraw.multiline_textsize(dtag,text=string, font=font)

        if justify=='center':
            justamt=[.5*i for i in attsize]
        elif justify=='left':
            justamt=(attsize[0]/2,0)
        dtag.multiline_text([round(tagsize[i]*locrat[i]-justamt[i]) for i in range(2)],string,anchor='center',font=font)#takes the size of the tag, multiplies it by location ratio, then subtracts pixelsize of text - needed bc default action of text is to go from top-left corner, this ends up doing from the center
        #add line here



#'tagstyle':{'image':{'imsize':(5,3.53),'nxy':(1,1),'res':80},
        #          'description':{'c':[.5,1/8],'size':60,'font':'timesbd.ttf'}, 
        #          'price':{'c':[.5,3/8],"font":"timesbd.ttf",'size':120},
        #          'barcode':{'c':[-.05,.65],'rot':0,'underbar':True,'shape':[5,100]},
        #          'underbar':{'font':'MINI 7 Bold.ttf','underdist':10,'size':20},
        #          'month':{'c':[.95,.9],"font":"timesbd.ttf","size":40},
        #          'combo':{'c':[.5,.6],'font':'timesbd.ttf','size':20,'rot':20}})   
    #    
# furnstyle=pandas.DataFrame({'image':{'imsize':(8.5,11),'nxy':(2,5),'res':150},
#          'description':{'c':[.15,4.5/8],'size':20,'font':'timesbd.ttf','text':'Description:'}, 
#          'price':{'c':[.5,3/8],"font":"timesbd.ttf",'size':80},
#          'barcode':{'c':[.8,.1],'underbar':False,'rot':90,'shape':[2,30]},
#          'underbar':{'font':'MINI 7 Bold.ttf','underdist':10,'size':20},
#          'month':{'c':[.95,.9],"font":"timesbd.ttf","size":10},
#          'blurb':{'c':[0.5,.1],"font":"timesbd.ttf","size":15,'text':'** Items must be picked up before 6pm on the \n  day of purchase. No Exceptions. Thank You! **'},
#          'combo':{'c':[.5,.6],'font':'timesbd.ttf','size':15}})
"""
 tagsize=(round(res*8.5/n[0]),round(res*11.0/n[1]))    
    tag=Image.new('L',tagsize,color="white")
    dtag=ImageDraw.Draw(tag)
    TEMPLATES['FRONT']['lbltxt']={str(lbl):TEMPLATES['FRONT']['lblloc']['']}
    def centertext(d,font,justify='center',line=0,autopar=False):        
      
        for string in d.keys():
            locrat=d[string]
            attsize=ImageDraw.ImageDraw.multiline_textsize(dtag,text=string, font=font)

            if justify=='center':
                justamt=[.5*i for i in attsize]
            elif justify=='left':
                justamt=(attsize[0]/2,0)
            dtag.multiline_text([round(tagsize[i]*locrat[i]-justamt[i]) for i in range(2)],string,anchor='center',font=font)#takes the size of the tag, multiplies it by location ratio, then subtracts pixelsize of text - needed bc default action of text is to go from top-left corner, this ends up doing from the center
            #add line here

    if side=='front':
        frnt=TEMPLATES['FRONT']
        centertext(frnt['fs'],  font=ImageFont.truetype(ubuntum,90)) 
        centertext(frnt['fyn'],  font=ImageFont.truetype(ubuntum,12))
        centertext(frnt['frontbtm'],  font=ImageFont.truetype(ubuntum,12))
        centertext(frnt['frontfields'],  font=ImageFont.truetype(ubuntum,12))
        centertext(frnt['lbltxt'],  font=ImageFont.truetype(ubuntum,15))
    elif side=='back':
        bck=TEMPLATES['BACK']
        centertext(bck['backmgmt'],  font=ImageFont.truetype(ubuntum,9),justify='center') 
        centertext(bck['backfields'],  font=ImageFont.truetype(ubuntum,9),justify='center') 
        centertext(bck['backblurb'],  font=ImageFont.truetype(ubuntum,9),justify='center') 
        
        
    else:
        return None
    
    
    return tag 
"""