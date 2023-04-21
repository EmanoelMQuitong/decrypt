#case adjustment to convert all letter cases to upper case. Spaces is also removed from input data."
def plain_case(plain_text):
    plain_text = plain_text.upper()
    plain_text = plain_text.replace(" ","")
    return plain_text