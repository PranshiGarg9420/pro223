import zipfile
import time

folderpath=input('Enter the path of folder yo want to decode: ')
zf= zipfile.ZipFile(folderpath)
global result
result=0
global tried
tried=0
c=0

if not zf:
    print('The file is not password protected. You can successfully open the file!')
else:
    startime= time.time()
    wordListFile= open('wordlist.txt','r', errors='ignore')
    body= wordListFile.read().lower()
    words=body.split('\n')
    for i in range(len(words)):
        word=words[i]
        password= word.encode('utf-8').strip()
        c+=1
        print('Trying to decode the password by: {}'.format(word))
        try:
            with zipfile.ZipFile('folderpath','r') as zipf:
                zipf.extractall(pwd=password)
                print('Success! The password is '+word)
                endttime=time.time()
                result=1
            break
        except:
            pass

if (result==0):
    print('Sorry! Password not found. A total of "+str(c)+" + possiblle combinations tried in "+str(duration)+". Password is not of 4 characters. ')
elif(result==1):
    print('Congrarulations!! Password found after trying "+str(continue;)+" in "str(duration)" seconds.')
