og_string = "hello"
rev_string = og_string[::-1]
print (rev_string)

def reverse_string(string):
   new_string = ""
   charNum = len(string) - 1
   while charNum >= 0:
      new_string += (string[charNum])
      charNum -= 1
   return new_string