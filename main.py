# remember to fork this and push to github

# f = open('test.txt', 'r')
# print(f.readlines())
# f.close()
# with open('test.txt', 'r') as f:
#   f_contents = f.readlines()
#   print(f_contents, end='')
# employee_file = open('index.html', 'w')

# employee_file.write("<p>This is HTML</p>")

# with open('test.txt', 'r') as f:
#   f_contents = f.read()
#   print(f_contents)

# employee_file.close()

# with open('readme.txt', 'w') as f:
#   f.write('readme')
#this overwrites the original content
# with open('readme.txt', 'w') as f:
#   f.write('I dont care')
# #this appends to the original content
# with open('readme.txt', 'a') as f:
#   f.write('I dont care 3x')

# create a file through python code

# get it to accept user input

  
# to append to the content
input = input("how are you ")
with open('userinput.txt', 'a') as f:
  f.write(input)