#git commit established
#import pyfiglet for creativity
import pyfiglet
from colored import fg

color = fg('yellow')

encrypted_string = input("Enter a encrypted text to decrypt: ")
decrypted_string = encrypted_string.replace('*','a').replace('&','e').replace('#','i').replace('+','o').replace('!','u')