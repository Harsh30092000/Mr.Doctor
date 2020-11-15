import re
#f = open('hospital_format.txt','r')
f1 = open('2nd_edited_file1.txt','r')
f2 = open('2nd_edited_file2.txt','w')
##f3 = open('2nd_edited_file3_.txt','w')
##f4 = open('2nd_edited_file4.txt','r')
##f5 = open('2nd_edited_file5.txt','r')
##f6 = open('2nd_edited_file6.txt','w')
#print(f.readline())
l = f1.readlines()
print(len(l))
last_l = 0
for i in l:
    z = i.split(' - ')
    try:
        z_temp = [0,0,0,0]
        z_temp[0] = z[2]
        z_temp[1] = z[1]
        z_temp[2] = z[0]
        z_temp[3] = z[3]
    
        z_temp[0] = '<div class="col-lg-6"><div class="listofhos"><div class="row marg"><div class="col-lg-12"><h3 class="name">' + z_temp[0]
        z_temp[1] = '</h3><hr><p>' + z_temp[1]
        z_temp[2] = ', ' + z_temp[2]
        z_temp[3] = ' | ' + z_temp[3] + '</p></div></div></div></div>'
        last_l = last_l +1
    except:
        z_temp = [0,0,0,0]
        z_temp[0] = z[1]
        z_temp[1] = ''
        z_temp[2] = z[0]
        z_temp[3] = z[2]
    
        z_temp[0] = '<div class="col-lg-6"><div class="listofhos"><div class="row marg"><div class="col-lg-12"><h3 class="name">' + z_temp[0]
        z_temp[1] = '</h3><hr><p>' + z_temp[1]
        z_temp[2] = ' ' + z_temp[2]
        z_temp[3] = ' | ' + z_temp[3] + '</p></div></div></div></div>'
        last_l = last_l +1
    x = ''.join(z_temp)
    f2.write(x)
     
f2.close()
f1.close()

#print(f.read())

##l = f1.readlines()
##for i in l:
##    rep = re.sub(' - ','</h3><hr><p>',i,1)
##    f2.write(rep)
##    z = '<div class="listofhos"><div class="row"><div class="col-lg-6"><div class="row marg"><div class="col-lg-12"><h3 class="name">' + i
##    f1.write(z)
    

#<div class="listofdoc"><div class="row"><div class="col-lg-2 l"><p>

##while(f.readline()):
##    f2.write('<div class="listofdoc"><div class="row"><div class="col-lg-2 l"><p>'\
##             +f.readline())
##    z = f5.readline()
##    try:
##        rep = re.sub('\n','</p></div><div class="col-lg-12"><hr></div></div></div>',z,1)
##        f6.write(rep+'\n')
##    except:
##        pass
#</h3><hr><p>
##while(f1.readline()):
##    z = f1.readline()
##    try:
##        rep = re.sub(' - ','</h3><hr><p>',z,1)
##        f6.write(rep+'\n')
##    except:
##        pass
