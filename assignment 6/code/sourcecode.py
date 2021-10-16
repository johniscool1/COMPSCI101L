
import string 
three = 0
final_list =[]

def Encrypt(string_text, int_key):
  final_list = [] 
#'''Caesar-encrypts string using specified key.'''
  list_text = list(string_text)
  count = 0
  while count < len(list_text):

    if list_text[count] != " ":
      
      three = ord(list_text[count]) + int_key
      final_list.append(chr(three))
      count += 1
    else:
      final_list.append(" ")
      count +=1

  final_string = ''.join(final_list)
  return final_string
    
  


def Decrypt(string_text, int_key): 
  final_list = []
  list_text = list(string_text)
  count = 0
  while count < len(list_text):

    if list_text[count] != " ":
      
      three = ord(list_text[count]) - int_key
      final_list.append(chr(three))
      count += 1
    else:
      final_list.append(" ")
      count +=1

  final_string = ''.join(final_list)
  return final_string
 
def Get_input(): 
  '''Interacts with user. Returns one of: '1', '2', '3', '4'.'''
  two = input("Enter your selection => ")
  return two

def Print_menu():
  '''Prints menu. No user interaction. '''
  print("1) Encode a string\n2) Decode a string\nQ) Quit")
  
def main(): 
  Again = True 
  while Again: 
    Print_menu()
    Choice = Get_input() 
    if Choice == '1': 
      Plaintext = input("Enter (brief) text to encrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext) 
    elif Choice == '2': 
      Ciphertext = input("\nEnter (brief) text to decrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext, "\n") 
   
    else: 
      print("Have an ordinary day.") 
      Again = False 
      
      
# our entire program: 
main() 
