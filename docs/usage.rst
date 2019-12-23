*****
Usage
*****


Basic usage
===========

The example here is to show how to build basic form

.. code-block:: python
 
 from pyfield import Text
 from pyfield import Integer

 # for password
 from getpass import getpass

 # create all field object
 username = Text('Username')
 email = Text('Email')
 age = Integer('Age')
 password = Text('Password')

 # get value by asking user from input or getpass on password
 username(input(username.prompt_input()))
 email(input(email.prompt_input()))
 password(getpass(password.prompt_input()))
 age(input(age.prompt_input()))

 # print result
 print('----------------------------')
 print(f'Your name is {username.get}')
 print(f'Your email address is {email.get}')
 print(f'You are {age.get} years old')
 print(f'Your password is stored in plain text "{password.get}"')
 print('----------------------------')


Advanced usage
==============

The example here is to show how to build advanced form with transfomator and
validator.

.. code-block:: python
 
 from pyfield import Text
 from pyfield import Integer

 from pyfield.validator.text import is_email_addr

 from pyfield.error import InvalidError

 # for password
 import hashlib
 from getpass import getpass

 ###### transformator ######
 def hasher(pw):
     '''hash password'''
     crypt = hashlib.sha1()
     crypt.update(pw.encode())

     return crypt.hexdigest()

 def unicoder(name):
     '''change to unicode'''
     return name.replace(' ', '_')

 def trans_name(name):
     '''Name transformation'''
     return name.title()

 ###### validator ######
 def normal_age(age_num):
     from pyfield.error import InvalidError

     if age_num > 200:
         raise InvalidError('You are too old')


 # create all field object with transformator and validator
 # transformator and validator are defined above but some validator is from builting
 # ex: is_email_addr
 username = Text('Username', transformator=[unicoder, trans_name], )
 email    = Text('Email',    validator=[is_email_addr], )
 age      = Integer('Age',   validator=[normal_age], )
 password = Text('Password', transformator=[hasher], )

 try:
     username(input(username.prompt_input()))
     email(input(email.prompt_input()))
     password(getpass(password.prompt_input()))
     age(input(age.prompt_input()))
 except InvalidError as e:
     print(e)

 print('----------------------------')
 print(f'Your name is {username.get}')
 print(f'Your email address is {email.get}')
 print(f'You are {age.get} years old')
 print(f'Your password is crypted "{password.get}"')
 print('----------------------------')

