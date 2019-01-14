###
#IMPORTS - outside scripts to be used in this file. anything not declared with "import" can't be accessed from this file. 
from PIL import Image, ImageDraw, ImageFont#Python's Image Library 
import os #used to save & load files, ensures compatability on all operating systems
import random #random number generator
#import tempfile #makes random-named files & stores only until no longer being used
import io
###
wd=os.path.abspath(os.path.dirname(__file__))#folder script is stored in, used as relative point at which to save
###
#TEMPLATE DEFINITIONS
fieldcorn=(.4,.8)
ubuntum=os.path.join(wd,"Fonts","Ubuntu","Ubuntu-M.ttf")
timesbd=os.path.join(wd,"Fonts","Times","timesbd.ttf")
TEMPLATES={
    'OLDSOLD-BACK':{
            '__IM':[{'key':"BCK",}],#@todo switch keys reliably
        'backblurb':[{'text':"Once you, the customer, have purchased an item, you are fully responsible for it. \nIf you choose to leave the item and return for it please attach this sign to it until \nyou return. Items must be picked up the same day they are purchased unless arrangements \nfor delivery through the store are made. By signing this form, you the customer \nacknowledge that Opportunity House is not responsible for any damage, re-sell, \nor loss of an item once it has been purchased, and NO REFUNDS will be given. \nDue to the minimum floor/storage space, of your item is left after close \nof the purchase date the store reserves the right to re-sell the item.",'font':(ubuntum,9),'c':(.5,.3)}],
        'backmgmt':[{'text':"Thank you for your cooperation \nManagement",'c':(.23,.7),'font':(ubuntum,9)}],
        'backfields':[{'text':"CUSTOMER NAME:",'c':fieldcorn,'font':(ubuntum,9)},
                      {'text':"CUSTOMER SIGNATURE",'c':tuple(map(sum,zip(fieldcorn,(0,.05)))),'font':(ubuntum,9)},
                      {'text':"PHONE #",'c':tuple(map(sum,zip(fieldcorn,(0,.1)))),'font':(ubuntum,9)}, 
                      {'text':"DATE",'c':tuple(map(sum,zip(fieldcorn,(.3,.1)))),'font':(ubuntum,9)}]
    },
    'OLDSOLD-FRONT':{
            '__IM':[{}],
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
     'NEWSOLD':{#box around sign, 2-3 per page,logo,underlines
         '__IM':[{'rot':90,'res':80,'nxy':(1,2)}],
         'test':[{'font':(ubuntum,12),'text':"Item Description",'c':(0.3,0.25)},
                 {'font':(ubuntum,12),'text':"Date",'c':(0.3,0.3)},
                  {'font':(ubuntum,12),'c':(0.4,.55),'text':"Associates Initials"},
                  {'c':(0.2,.6), 'font':(ubuntum,12),'text':"Customer Name"},
                  {'c':(0.25,.65),'font':(ubuntum,12),'text':"Customer Phone #"},
                   {'font':(ubuntum,12),'text':"Delivery Fee",'c':(.2,.7)},
                   {'font':(ubuntum,12),'text':"Date Paid",'c':(.6,.7)},
                  {'font':(ubuntum,12),'text':"Scheduled Delivery Date",'c':(.3,.75)},
                 {'font':(ubuntum,80),'text':'SOLD!','c':(.5,.4)},
                 {'font':(ubuntum,12),'c':(.5,.8),'text':'Please pick up your items by the end of the day \nunless you have paid for us to Deliver it to you.'},
         
                   {'font':(ubuntum,12),'text':"Delivery fees",'c':(.2,.9)},
            {'font':(ubuntum,10),'text':'Vacaville - $30.00','c':(0.5,.9)},
         {'font':(ubuntum,10),'text':'Fairfield - $45.00','c':(0.5,.935)},
     ]},
     'TAG':{'__IM':[{'imsize':(5,3.53),'nxy':(1,1),'res':80}],
                  'description':[{'c':[.5,1/8],'text':'test','font':(timesbd,60)}], 
#                  'price':[{'c':[.5,3/8],"font":"timesbd.ttf",'size':120}],
#                  'barcode':[{'c':[-.05,.65],'rot':0,'underbar':True,'shape':[5,100]}],
#                  'underbar':[{'font':'MINI 7 Bold.ttf','underdist':10,'size':20}],
#                  'month':[{'c':[.95,.9],"font":"timesbd.ttf","size":40}],
#                  'combo':[{'c':[.5,.6],'font':'timesbd.ttf','size':20,'rot':20}]
}   
    #    
# furnstyle=pandas.DataFrame({'image':{'imsize':(8.5,11),'nxy':(2,5),'res':150},
#          'description':{'c':[.15,4.5/8],'size':20,'font':'timesbd.ttf','text':'Description:'}, 
#          'price':{'c':[.5,3/8],"font":"timesbd.ttf",'size':80},
#          'barcode':{'c':[.8,.1],'underbar':False,'rot':90,'shape':[2,30]},
#          'underbar':{'font':'MINI 7 Bold.ttf','underdist':10,'size':20},
#          'month':{'c':[.95,.9],"font":"timesbd.ttf","size":10},
#          'blurb':{'c':[0.5,.1],"font":"timesbd.ttf","size":15,'text':'** Items must be picked up before 6pm on the \n  day of purchase. No Exceptions. Thank You! **'},
#          'combo':{'c':[.5,.6],'font':'timesbd.ttf','size':15}})

    #@TODO - dict-able PIL objects,  
}
#### 
#FUNCTIONS
#
ORIENTATIONS={'portrait':(8.5,11),'landscape':(11,8.5)}
def newSoldTag(res=100,n=(2,6),lbl=None,side='newsold'):
  pass
def soldTag(res=100, n=(2,6),lbl=None,side='oldsold-front',orientation='portrait'):
    o=ORIENTATIONS[orientation]
    tagsize=(round(res*o[0]/n[0]),round(res*o[1]/n[1]))    
    tag=Image.new('L',tagsize,color="white")
    dtag=ImageDraw.Draw(tag)
    print(orientation)
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
    
#    else:
#        print(side)
#    if side=='front':
#        frnt=TEMPLATES['FRONT']
##        centertext(frnt['fs'],  font=) 
##        centertext(frnt['fyn'],  font=)
##        centertext(frnt['frontbtm'],  )
##        centertext(frnt['frontfields'],  font=ImageFont.truetype(ubuntum,12))
#        centertext(frnt['lbltxt'],  font=ImageFont.truetype(ubuntum,15))
#    elif side=='back':
#        bck=TEMPLATES['BACK']
#        centertext(bck['backmgmt'],  font=ImageFont.truetype(ubuntum,9),justify='center') 
#        centertext(bck['backfields'],  font=ImageFont.truetype(ubuntum,9),justify='center') 
#        centertext(bck['backblurb'],  font=ImageFont.truetype(ubuntum,9),justify='center') 
#        
        
    else:
        return None
    
    if side.upper()=='NEWSOLD':
        corns=((.025,.05),(.975,.95))
        coords=[round(tagsize[i]*corns[j][i]) for j in range(2) for i in range(2)]
        logo=Image.open(os.path.join(wd,"Logo","NewLogoCentered.png"))
        tag.paste(logo.resize((round(tagsize[0]/2),80)),(round(tagsize[0]/4),round(tagsize[1]*.05)))
        dtag.rectangle(coords,width=2,outline='black')
    return tag 


#objfn - what to sheetify, n - number of modules in (x-direction, y-direction), lw - linewidth, res - resolution
def sheetify(objfn,n=(2,6),lw=3,res=100,lbllist=None,side='oldsold-front',orientation='portrait'):
    N=n[0]*n[1]
    o=ORIENTATIONS[orientation]
    if len(n)==2:
        nx,ny=n 
    else:
        return None
    
    if lbllist is None:
        lbllist=['' for x in range(N)]
    elif len(lbllist)<N:
        [lbllist.append('') for x in range(N-len(lbllist))]
    sheetsize=(round(res*o[0]),round(res*o[1]))#fits to 8.5"x11" sheet
    shtbox=(0,0,round(sheetsize[0]/nx),round(sheetsize[1]/ny))
    sheet=Image.new('RGB',sheetsize,color='white')#image basefile
    drsh=ImageDraw.Draw(sheet)#drawing
    for i in range(nx): 
        for j in range(ny):
            nn=i*n[1]+j#gets current index 1-dimensionally - if order of fors changes this needs to change too
            obj=objfn(res,n,lbl=lbllist[nn],side=side,orientation=orientation)
            sheet.paste(obj,[round(x) for x in [shtbox[0]+i*shtbox[2],shtbox[1]+j*shtbox[3],shtbox[0]+i*shtbox[2]+obj.size[0],shtbox[1]+j*shtbox[3]+obj.size[1]]])
            drsh.line( (0,j*sheetsize[1]/ny,sheetsize[0],j*sheetsize[1]/ny), fill=0,width=lw) #horizontals
        drsh.line( (i*sheetsize[0]/nx,0,i*sheetsize[0]/nx,sheetsize[1]), fill=0,width=lw) #vertical
    return sheet
def multiSheetRender(objfn,sides=['oldsold-front','oldsold-back'],n=(2,6),lw=3,res=100,lbllist=None,orientation='portrait'):
    sheets=[]
    for s in sides:
        sheets.append(sheetify(objfn,n,lw,res,lbllist,side=s,orientation=orientation))
    return sheets
        
#
def alphabet(rng={'upper'}):
    alph=[]
    rngs={'lower':(97,122),'upper':(65,90)}#ranges of ascii locations - inclusive
    for r in rng:
        if r not in rngs.keys():
            pass
        else:
            for loc in range(*rngs[r]):
                alph.append(chr(loc))
    return list(alph)
#
def randomLabels(n=(2,6),numspots=2):
    alph=alphabet()
    ralph=[]
    for nn in range(n[0]*n[1]):
        spots=''
        for s in range(numspots):
            r=random.randint(0,len(alph)-1)
            spots=spots+alph[r]
        
        ralph.append(spots)
            
    return ralph
#highest-level method for this file, can just run w/o arguments for good output
    #
def renderSheets(n=(2,6),lw=3,res=100,lblmethod='random',numsheets=1,sides=['oldsold-front'],lbldsides=None,orientation='portrait'):
    sheets=[]
    for sht in range(numsheets):
        if lblmethod=='random':
            lbllist=randomLabels(n=n)
        sheets.append(multiSheetRender(objfn=soldTag,n=n,lw=lw,res=res,lbllist=lbllist,sides=sides,orientation=orientation))
    return sheets
#
def saveSheets(sheets,fn=None):
    if fn is None:
        #fn=tempfile.TemporaryFile(suffix='pdf').name
        fl=io.BytesIO(fn)
        
    else:
        fl=open(os.path.join(wd,'static','renderedSigns',fn),'wb+')
        
    sheets[0][0].save(fp=fl,format='PDF',save_all=True,append_images=[pg for sht in sheets for pg in sht if pg!=sheets[0][0]]) 
    return fl,fn
###
"""
#@TODOs 
       CSS-like
"""
