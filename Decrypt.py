#git commit established
#import pyfiglet for creativity text art
import pyfiglet
from colored import fg

color = fg('yellow')

encrypted_string = input("Enter a encrypted text to decrypt: ")
decrypted_string = encrypted_string.replace('*','a').replace('&','e').replace('#','i').replace('+','o').replace('!','u')

print('\n', "Decrypted text: ", '\n', color + pyfiglet.figlet_format(decrypted_string, font= "digital"))
