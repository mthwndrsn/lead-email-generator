from prompt_toolkit.shortcuts import input_dialog

first_name = input_dialog(
    title='First Name',
    text='Please type your first name:').run()

last_name = input_dialog(
    title='Last Name',
    text='Please type your last name:').run()

domain = input_dialog(
    title='Domain',
    text='Please enter the domain name:').run()

print(first_name+"."+last_name+"@"+domain)
print(first_name+last_name+"@"+domain)
print(first_name+"@"+domain)
print(first_name[0]+last_name+"@"+domain)
print(first_name[0]+"."+last_name+"@"+domain)
print(first_name[0]+last_name[0]+"@"+domain)
print(first_name+last_name[0]+"@"+domain)
print(last_name+first_name[0]+"@"+domain)
print(first_name+"_"+last_name+"@"+domain)
