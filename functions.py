# Function calling and return statement


# u_name='sindhu'
# u_password=123
# uname=input('Enter your name:')
# pword=int(input('enterr ur password:'))
# def validate(uname,pword):
#    if uname==u_name and u_password==pword:
#       return True
#    else:
#       return False

# print(validate(uname,pword))


def family(*fam):
    print('hi'+' '+ fam[1] )

family('sindhu','priya','jaya')