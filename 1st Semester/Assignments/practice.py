#Write and run python file
#!/usr/bin/python3

# import modules used here -- sys is a very standard one
#import sys

# Gather our code in a main() function
#def main():
 #   print('Hello there', sys.argv[1])
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
#if __name__ == '__main__':
 #   main()

#$ python3 hello.py Guido
#Hello there Guido
#$ ./hello.py Alice  ## without needing 'python3' first (Unix)
#Hello there Alice





s='hi'
#print(s+ " there")

pi = 3.14
text = 'Value of pi is ' + str(pi)
#print(text)

raw = 'this \t \n is it '
#print(raw)

multi = """ multi line text is not that useful 
             and quite handy for other things
             """
#print(multi)

#String Method .lower/upper .isalpha/isdigit.isspace .replace  .strip 
# .startswith .endswith .find .split .join  

#String Slice 
#s[1:4] [:] [-1] [:-3] [-2:]

value = 2.457648
#print(f'approxiamte value = {value:.2f}')

car = {'tires':4, 'doors':2}
#print(f'car = {car}') 

address_book = [{'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
      {'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
      {'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},]
#for person in address_book:
 #   print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')


# % Operator
text = "%d little pigs out, or ill %s and ill %s or i will blow your %s out" %(3,'huff','puff','house')
#print(text)


import sys
import io

# Set the encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#Strings (Unicode vs bytes)
text2 = "Hello this it in hindi मज़ा"
#print(text2)

# Encode to UTF-8 bytes
byte_text = text2.encode('utf-8')
#print(byte_text)

# Decode back to a Unicode string
decoded_text = byte_text.decode('utf-8')
#print(decoded_text)

 #Unlike Java and C, == is overloaded to work correctly with strings.
 #*and*, *or*, *not* (Python does not use the C-style && || !).
time_hour=15
mood = 'sleepy'
if time_hour >= 0 and time_hour <= 24:
    print('Suggesting a drink option...')
    if mood == 'sleepy' and time_hour < 10:
      print('coffee')
    elif mood == 'thirsty' or time_hour < 2:
      print('lemonade')
    else:
      print('water')

if time_hour < 10: print('coffee')
else: print('water')







