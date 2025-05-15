from Demos.RegCreateKeyTransacted import keyname

programming_dictionary={
    'Bug': 'An error in a program that prevents the program from running as expected.',
    'Function': 'A piece of code that you can easily call over and over again.',
    'Loop': 'The action of doing something over and over again.'
}

print(programming_dictionary['Bug'])

#add
print('*'*50)
programming_dictionary['New Key'] = 'New Value'
print(programming_dictionary['New Key'])

#wipe
# programming_dictionary={}

#edit
print('*'*50)
programming_dictionary['Bug']= 'Edited a new entry of value'
print(programming_dictionary['Bug'])

#Loop through a dictionary
print('*'*50)
for thing in programming_dictionary:
    print(thing)  #will print key
    print(programming_dictionary[thing]) #will print value
