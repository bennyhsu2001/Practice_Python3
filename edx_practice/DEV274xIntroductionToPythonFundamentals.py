# ----------------------------------<MODULE1>-------------------------------------
# phrase = input ("enter a 1 sentence quote, non-alpha separate words: ").lower()
# word = ""
# for letter in phrase:
#     if letter.isalpha():
#         word += letter
#     else:
#         if(word > "h" ):
#             print(word)
#             word = ""
#         else:
#             word = ""
# print(word)

# ----------------------------------<MODULE2>-------------------------------------
# def list_o_matic(L,s):  #L is a list; s is a string
#     if s =="":
#         L.pop()     
#     elif s in L:
#         L.remove(s)
#     else:
#         L.append(s)
#     return L 
#  
#  
# # main part
# L=['cat', 'goat', 'cat']
# while L:
#     print("look at all the animals",L)
#     s=input("enter the name of an animal: ")
#     if s == "quit":
#         break
#     else:
#         list_o_matic(L, s)
# 
# print("Goodbye!")

# ----------------------------------<MODULE3>-------------------------------------
# def word_mixer(word_list):
#     word_list.sort()
#     new_words=[]
#     while len(word_list)>5:
#         new_words.append(word_list.pop(-5))
#         new_words.append(word_list.pop(0))
#         new_words.append(word_list.pop(-1))
#     return new_words
#             
# s=input("enter a saying or poem: ")
# word_list=s.split()
# A=len(word_list)
# for index in range(A):
#     if len(word_list[index])<5:
#         word_list[index].lower()       
#     else:
#         word_list[index].upper()
#    
# print(word_mixer(word_list))

# ----------------------------------<MODULE4>-------------------------------------
# 
# get_ipython().system(u' curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt')
#         #看TM不懂第一句
# mean_temps = open('mean_temp.txt','a+')
# mean_temps.write("Rio de Janeiro,Brazil,30.0,18.0\n")
# mean_temps.seek(0)
# headings = mean_temps.readline()
# headings = headings.split(',')
# 
# city_temp = mean_temps.readline()
# 
# while city_temp:
#     city_temp = city_temp.split(',')
#     print(headings[0].title(),"of",city_temp[0],headings[2],"is",city_temp[2],"Celsius")
#     city_temp = mean_temps.readline()  
# 
# mean_temps.close()

# ----------------------------------<MODULE5>-------------------------------------

# def get_names():
# 
#     get_ipython().system(u' curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elementsl_20.txt')
# 
#     print("list any 5 of the first 20 elements in the Period table: ")
#     names = [input("Enter the name of an element: ").lower()]
# 
#     while len(names) < 5:
#         guess = input("Enter the name of an element: ").lower()
# 
#         while guess == "":
#             print("empty strings are not valid inputs")
#             guess = input("Enter the name of an element: ").lower()
#         
#         duplicate = "no"
#         
#         while guess in names:  
#             print(guess, "was already entered")
#             guess = input("Enter the name of an element: ").lower()
#        
#         names.append(guess)
#    
#     elements_file = open('elementsl_20.txt', 'r')
#     element_text = elements_file.readline().strip().lower()
#     elements_list = [ ]
#     
#     while element_text:
#         elements_list.append(element_text)
#         element_text = elements_file.readline().strip().lower()
#     
#     elements_file.close()
# 
#     Found = [ ]
#     Not_Found = [ ]
#     correct = 0
#  
#     for element in names:
#         if element in elements_list:
#             Found.append(element)
#             correct += 1
#         else:
#             Not_Found.append(element)
#   
#     print(names, "\n")
#     print(str(correct * 20) + "\% correct")  # correct
#     print("Found:", Found, "\n")
#     print("Not Found:", Not_Found)
#     
#     return names
#     
# get_names()

# ------------------------------------<END>---------------------------------------

