"""
@TODOs:
    Each mod has unique inputs from WebInterface
    Account for variables
    underlines - 
       'after','under','before','above'...
"""
from PIL import Image, ImageDraw, ImageFont#Python's Image Library 
class ModuleVar(object):
    def __init__(self):
        pass

class Module(object):#graphical object representing certain aspect of sign, can contain other modules - has css-like attributes & pseudo-elements
    def __init__(self,c,res=100,modsize=(8.5,11),bar=None,rot=0,submodules=[],parentmod=None,modname=None,*args,**kw):
        self.atts={}
        self.inputs={}
        #@TODO - make more flexible w kwargs & checking
        self.c=c
        self.res=res
        self.modsize=modsize
        self.bar=bar
        self.rot=rot
        self.submodules=submodules
        self.parentmod=parentmod
        self.modname=modname

        self.relres=res/100
        self.modpix=(round(res*modsize[0]),round(res*modsize[1]))    
        tag=Image.new('L',self.modpix,color="white")
        dtag=ImageDraw.Draw(tag)
        TEMPLATES['FRONT']['lbltxt']={str(lbl):TEMPLATES['FRONT']['lblloc']['']}

    def renderSubModules(self):
        self.renderedSubs=[]
        for s in self.submodules:
            self.renderedSubs.append(s.renderModule())

    def renderModule(self):
        self.MOD=None
        return self.MOD
class TextModule(Module):
    def __init__(self,text,font,size,justification,**kw):
        self.inputs.add({''})

    def renderModule(self):
        self.MOD=loadTexts(self.text)

class BarcodeModule(Module):
    def __init__(self,code,dims,encoding='128',**kw):
        pass
    def renderModule(self):
      self.MOD=code128.image(self.code,thickness=round(self.relres*self.dims[0]),height=round(self.relres*self.dims[1]))
      # bar=bar.convert('RGB') #convert to RGB just in case
      #       bar=bar.rotate(refdict['barcode']['rot'],expand=1) 
      #       #paste barcode onto canvas
      #       barbox=[round(dyn_look(self,"barcode.pos")[0]),round(dyn_look(self,"barcode.pos")[1]),0,0]
      #       barbox[2]=barbox[0]+bar.size[0]
      #       barbox[3]=barbox[1]+bar.size[1]
            # self.tag.paste(bar,barbox)
      return self.MOD
class ShapeModule(Module):
    def __init__(self,type,**kw):
        pass
    
class FormfieldsModule(Module):
    pass
class FrameModule(Module):
    def __init__(self,**kw):
        pass
class GridModule(Module):
    def __init__(self,N,modtosub,labels,**kw):
        pass
class SheetModule(Module):
    def __init__(self,**kw):
        pass
    def renderModule(self,objfn,n=(2,6),lw=3,res=100,lbllist=None,side='front'):
        N=n[0]*n[1]
        if len(n)==2:
            nx,ny=n 
        else:
            return None
        
        if lbllist is None:
            lbllist=['' for x in range(N)]
        elif len(lbllist)<N:
            [lbllist.append('') for x in range(N-len(lbllist))]
        sheetsize=(round(res*8.5),round(res*11.0))#fits to 8.5"x11" sheet
        shtbox=(0,0,round(sheetsize[0]/nx),round(sheetsize[1]/ny))
        sheet=Image.new('RGB',sheetsize,color='white')#image basefile
        drsh=ImageDraw.Draw(sheet)#drawing
        for i in range(nx): 
            for j in range(ny):
                nn=i*n[1]+j#gets current index 1-dimensionally - if order of fors changes this needs to change too
                obj=objfn(res,n,lbl=lbllist[nn],side=side)
                sheet.paste(obj,[round(x) for x in [shtbox[0]+i*shtbox[2],shtbox[1]+j*shtbox[3],shtbox[0]+i*shtbox[2]+obj.size[0],shtbox[1]+j*shtbox[3]+obj.size[1]]])
                drsh.line( (0,j*sheetsize[1]/ny,sheetsize[0],j*sheetsize[1]/ny), fill=0,width=lw) #horizontals
            drsh.line( (i*sheetsize[0]/nx,0,i*sheetsize[0]/nx,sheetsize[1]), fill=0,width=lw) #vertical
        return sheet
class PicModule(Module):
    def __init__(self,filepath,**kw):
        pass


def renderSign():
	pass

def loadTexts(d,font,justify='center',line=0,autopar=False):        
  
    for string in d.keys():
        locrat=d[string]
        attsize=ImageDraw.ImageDraw.multiline_textsize(dtag,text=string, font=font)

        if justify=='center':
            justamt=[.5*i for i in attsize]
        elif justify=='left':
            justamt=(attsize[0]/2,0)
        dtag.multiline_text([round(tagsize[i]*locrat[i]-justamt[i]) for i in range(2)],string,anchor='center',font=font)#takes the size of the tag, multiplies it by location ratio, then subtracts pixelsize of text - needed bc default action of text is to go from top-left corner, this ends up doing from the center

def guessMatchingModule(dictitem):
    pass

def unfoldTemplates(tempdict):
    pass
#'tagstyle':{'image':{'imsize':(5,3.53),'nxy':(1,1),'res':80},
        #          'description':{'c':[.5,1/8],'size':60,'font':'timesbd.ttf'}, 
        #          'price':{'c':[.5,3/8],"font":"timesbd.ttf",'size':120},
        #          'barcode':{'c':[-.05,.65],'rot':0,'underbar':True,'shape':[5,100]},
        #          'underbar':{'font':'MINI 7 Bold.ttf','underdist':10,'size':20},
        #          'month':{'c':[.95,.9],"font":"timesbd.ttf","size":40},
        #          'combo':{'c':[.5,.6],'font':'timesbd.ttf','size':20,'rot':20}})   
    #    

"""   
def soldTag(res=100, n=(2,6),lbl=None,side='front'):
    tagsize=(round(res*8.5/n[0]),round(res*11.0/n[1]))    
    tag=Image.new('L',tagsize,color="white")
    dtag=ImageDraw.Draw(tag)
#    TEMPLATES['FRONT']['lbltxt']={str(lbl):TEMPLATES['FRONT']['lblloc']['']}
    def centertext(d,justify='center',line=0,autopar=False):        
      
        for att in d:
            if 'c' in att.keys():
                locrat=att['c']
    
                font=ImageFont.truetype(*att['font'])
                attsize=ImageDraw.ImageDraw.multiline_textsize(dtag,text=att['text'], font=font)
    
                if justify=='center':
                    justamt=[.5*i for i in attsize]
                elif justify=='left':
                    justamt=(attsize[0]/2,0)
                dtag.multiline_text([round(tagsize[i]*locrat[i]-justamt[i]) for i in range(2)],att['text'],anchor='center',font=font)#takes the size of the tag, multiplies it by location ratio, then subtracts pixelsize of text - needed bc default action of text is to go from top-left corner, this ends up doing from the center
                #add line here
    if side.upper() in TEMPLATES.keys():
        for t in TEMPLATES[side.upper()].keys():
            for field in TEMPLATES[side.upper()][t]:
                centertext(TEMPLATES[side.upper()][t])
#    
                
TEMPLATES={
    'BACK':{
        'backblurb':[{'text':"Once you, the customer, have purchased an item, you are fully responsible for it. \nIf you choose to leave the item and return for it please attach this sign to it until \nyou return. Items must be picked up the same day they are purchased unless arrangements \nfor delivery through the store are made. By signing this form, you the customer \nacknowledge that Opportunity House is not responsible for any damage, re-sell, \nor loss of an item once it has been purchased, and NO REFUNDS will be given. \nDue to the minimum floor/storage space, of your item is left after close \nof the purchase date the store reserves the right to re-sell the item.",'font':(ubuntum,9),'c':(.5,.3)}],
        'backmgmt':[{'text':"Thank you for your cooperation \nManagement",'c':(.23,.7),'font':(ubuntum,9)}],
        'backfields':[{'text':"CUSTOMER NAME:",'c':fieldcorn,'font':(ubuntum,9)},
                      {'text':"CUSTOMER SIGNATURE",'c':tuple(map(sum,zip(fieldcorn,(0,.05)))),'font':(ubuntum,9)},
                      {'text':"PHONE #",'c':tuple(map(sum,zip(fieldcorn,(0,.1)))),'font':(ubuntum,9)}, 
                      {'text':"DATE",'c':tuple(map(sum,zip(fieldcorn,(.3,.1)))),'font':(ubuntum,9)}]
    },
    'FRONT':{
        'fs':[{'text':"SOLD",'c':(.5,.25),'font':(ubuntum,90)}],
        'fyn':[{'text':"YES",'c':(.35,.75),'font':(ubuntum,12)},
               {'text':"NO",'c':(.5,.75),'font':(ubuntum,12)}],
        "frontbtm":[{'text':"*Please attach receipt if paid*",'c':(.5,.85),'font': (ubuntum,12)},
                    {'text':"*All items must be picked up by end of day*",'c':(.5,.95),'font': (ubuntum,12)}],
                     
        "frontfields":[{'text':"Date:",'c':(.5,.05),'font':(ubuntum,12)},
                       {'text':'Cashier Initials:','c':(.25,.6),'font':(ubuntum,12)},
                       {'text':'Customer Initials:','c':(.65,.6),'font':(ubuntum,12)},
                       {'text':'Paid:','c':(.25,.75),'font':(ubuntum,12)}],
        'lblloc':[{'c':(.1,.1),'font':(ubuntum,15),'text':'test'}]
    },
     'NEW':{#box around sign, 2-3 per page,logo,underlines
         '__IM':[{'rot':90,'res':80,'nxy':(1,2)}],
         'test':[{'font':(ubuntum,12),'text':"Date",'c':(0.3,0)},
                  {'font':(ubuntum,12),'c':(0.3,.1),'text':"Associates Initials"},
                  {'c':(0.3,.2), 'font':(ubuntum,12),'text':"Customer Name"},
                  {'c':(0.3,0),'font':(ubuntum,12),'text':"Customer Phone #"},
                   {'font':(ubuntum,12),'text':"Delivery Fee",'c':(.5,.7)},
                   {'font':(ubuntum,12),'text':"Date Paid",'c':(.5,.4)},
                  {'font':(ubuntum,12),'text':"Scheduled Delivery Date",'c':(.5,.5)},
                 {'font':(ubuntum,80),'text':'SOLD!','c':(.3,.5)},
                 {'font':(ubuntum,12),'text':'Please pick up your items by the end of the day unless you have paid for us to Deliver it to you.'},
         {'font':(ubuntum,10),'text':'Vacaville - $30.00','c':(0,.8)},
         {'font':(ubuntum,10),'text':'Fairfield - $45.00','c':(0,.9)},
     ]},
     'TAG':{'__IM':[{'imsize':(5,3.53),'nxy':(1,1),'res':80}],
                  'description':[{'c':[.5,1/8],'text':'test','font':(timesbd,60)}], 
                  'price':[{'c':[.5,3/8],"font":"timesbd.ttf",'size':120}],
                  'barcode':[{'c':[-.05,.65],'rot':0,'underbar':True,'shape':[5,100]}],
                  'underbar':[{'font':'MINI 7 Bold.ttf','underdist':10,'size':20}],
                  'month':[{'c':[.95,.9],"font":"timesbd.ttf","size":40}],
                  'combo':[{'c':[.5,.6],'font':'timesbd.ttf','size':20,'rot':20}]
}   
        
 'FURN':{'__IM':{'imsize':(8.5,11),'nxy':(2,5),'res':150},
          'description':{'c':[.15,4.5/8],'size':20,'font':'timesbd.ttf','text':'Description:'}, 
          'price':{'c':[.5,3/8],"font":"timesbd.ttf",'size':80},
          'barcode':{'c':[.8,.1],'underbar':False,'rot':90,'shape':[2,30]},
          'underbar':{'font':'MINI 7 Bold.ttf','underdist':10,'size':20},
          'month':{'c':[.95,.9],"font":"timesbd.ttf","size":10},
          'blurb':{'c':[0.5,.1],"font":"timesbd.ttf","size":15,'text':'** Items must be picked up before 6pm on the \n  day of purchase. No Exceptions. Thank You! **'},
          'combo':{'c':[.5,.6],'font':'timesbd.ttf','size':15}}

}
"""