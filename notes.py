# f = open('rahul.txt', 'w')
# # f.write('wow the world, My name is Light ')
# # f.write('currently learning File I.O \nnikhil')
# day=input('\nwhich day is going on? --> ')
# f.write(f'{day}\n\n')
# f.close()
"""
when we perform an on operation with the file
and if the file is set to work on as wirte 
as soon as you hit the run button all data
in that file shall get deleted and the file shall be blank
"""

# f = open("savedFile.txt", "a")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# f.close()

f = open("savedFoal.txt",
         "a+")  # from here we are openning the file oppicially

whatText = input("> ")
f.write(f"{whatText}\n")
whatText = input("> ")
f.write(f"{whatText}\n")

f.close()  #from here we are closing the file officially
"""
basically we use file I-O to get the user data recorded in the our system file
by doing this we can further work on the data. thus creating an permanent type of memory system

in repllit when we run the progrme for the some time it get's rocded to replit
server and as soon as we stop the run the data which user had created by 
working on terminal shall get wipe out. so inorder to tackle this conditio
we can created our own memory system

thus calling it as F  I-O
"""
