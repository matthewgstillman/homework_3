#Mini Project Help
#Length of string is not always divisible by 4
#If it is not divisible by 4, add 0 to the front until the length is divisible by 4

# def fix_string(string):
#     if len(string) % 4 != 0:
#         add_num = 4 - len( string) % 4
#         string = add_num * "0" + string
#         return string
#     else:
#         return string

# print(fix_string("12345"))


# hex = {
#     "0000": "0",
#     "0001": "1",
#     "1111": "F"
# }

# string = "000000011111"
# for i in range(0, len(string) // 4):
#     print(string[0:4])
#     print(hex["0000"])

#Dictionaries

# spanish = {
#     'one': 'uno',
#     'two': 'dos',
#     'three': 'tres',
#     'four': 'cuatro'.
#     'five': 'cinco'
# }

#for v in spanish.values():
#    print(v)

# for k in spanish.values():
#     print(k)

#Clearing
#spanish.clear()
#print(spanish.get('five'))

#spanish.pop('six', None)
#Default value is none
#print(spanish['one'])

#Pops the last item
# spanish.popitem()
# spanish.popitem()
# print(spanish)

#Printing Keys and Values
# for k, v in spanish.items():
#     print(i)

# # The dictionary below is imported froma another file called josh_spanish
# #import josh_spanish
# spanish = {
#     'one': 'uno',
#     'two': 'dos',
#     'three': 'tres',
#     'four': 'cuatro',
#     'five': 'cinco'
# }
# spanish['six'] = 'seis'
# number = len(spanish)
# print(spanish.items())
# print("The dictionary has {} items".format(number))