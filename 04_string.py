name = 'Angel'
last_name = 'Soto Orozco'
age = 27

print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name) 

quote = "I´m Angel"
print(quote)

#format

template = "hola, mi nombre es " + name + " y mi apellido es " + last_name 
print( 'v1', template)

template = "hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2',template)

template = f"hola mi nombre es {name}, mi apellido es {last_name} y mi edad es {age} años"
print('v3',template)