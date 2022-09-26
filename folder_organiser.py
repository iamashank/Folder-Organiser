import os
import re
import shutil, stat, sys
if (len(sys.argv)<2):
    source = 'C:\\Users\\Ashank\\Downloads'                 #Directory to be organised
else:
    source = sys.argv[1]
#Extensions for common file types (Enter in lower-case only)
codes = ['c','cpp','java','class','py','pyc','pyw','sh','pl','vb','o']
compressed = ['zip','rar','7z','zipx','gz','tar','bz']
docs = ['pdf','doc','docx','odt','rtf','txt','csv','ppt','pptx','xml','xlr','xls','xlsx']
photos = ['jpg','jpeg','png','ico','bmp','gif','tif','pcx','tga']
video = ['mp4','avi','3gp','rmvb','wmv','mkv','mpg','vob','mov','flv','swf']
audio = ['mp3','wma','flac','aac','mmf','amr','m4a','m4r','ogg','mp2','wav','wavpack']

#Names of the folders to be created
names = ['Programs','Codes','Compressed','Documents','Photos','Video','Music','Others']

for name in names:
    s = source+'\\'+name
    os.makedirs(s,exist_ok=True)        #Python 3 only

def copy(f,folder):
    s = source+'\\'+f
    d = source+'\\'+folder+'\\'+f
    shutil.copyfile(s,d)
    os.chmod(s, stat.S_IWRITE) # Adding some random comment here
    os.remove(s)

files = [ f for f in os.listdir(source) if os.path.isfile(os.path.join(source,f)) ]
for f in files:
    q = re.split('[.]', f)
    a = str(q[len(q)-1])
    a = a.lower()
    if (a == 'exe'):
        copy(f,names[0])
    elif (a in codes):
        copy(f,names[1])
    elif (a in compressed):
        copy(f,names[2])
    elif (a in docs):
        copy(f,names[3])
    elif (a in photos):
        copy(f,names[4])
    elif (a in video):
        copy(f,names[5])
    elif (a in audio):
        copy(f,names[6])
    else:
        copy(f,names[7])
