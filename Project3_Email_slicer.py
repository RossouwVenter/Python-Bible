word = 'supercalifragilisticexpialidocius'
word[0]

word

word[2]

word[0:5:1] 
# string[begin:end:step]

word[5:9:1]

word[5:]
#going to display from 5 onwards

word[5::2]
# going to count in 2

word[:7]
#everything up to 7
word[::-1]
#in reverse

word[-2]
#Counting from the back

word.index('cali')

word.index('fragi')

word[word.index('cali'):word.index('fragi')]

#Email Slicer

# Get user email address
email = input("what is your email address").strip()

# Slicer out user name

user = email[:email.index('@')]

# slice domain name

domain = email[email.index('@') + 1 :]
# format message 
output = "Your username is {} and your domain name is {}".format(user,domain)

print(output)
