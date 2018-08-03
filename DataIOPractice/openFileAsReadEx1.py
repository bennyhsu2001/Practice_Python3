'''
Created on 2018年7月30日

@author: Student
'''
Secret = open('secret/DoNotOpen.txt','r',encoding='utf-8');     
#the encoding type must be the same with the txt file
print(Secret);

for line in Secret:
    print(line, end="");

Secret.close();


# ------------------------------------------------
with open('secret/DoNotOpen.txt','r',encoding='utf-8') as Secret2:
#     whole_file = Secret2.read();
#     print("whole_file: ",whole_file);
    
    file_part =  Secret2.read();
    print("file_part: ",file_part);
    print("type of file_part: ",type(file_part));
    
# ------------------------------------------------    
Secret3 = open('secret/DoNotOpen.txt','r',encoding='utf-8')
result = list()
for line in open('secret/DoNotOpen.txt','r',encoding='utf-8'):
    line = Secret3.readline();
    print (line);
    result.append(line);
print (result);
Secret3.close()                

    
    
    