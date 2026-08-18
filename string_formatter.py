first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio_messsage = input("Write a short bio about yourself: ")

# initial and surname of the user
print(f"Username is : " + first_name[0].lower() + last_name.lower())

#Fullname in camel case
full_name = print(f"Full name is :{first_name.title()} {last_name.title()} ")


#Remove leading and trailing white space.
print("Your Bio : " + bio_messsage.strip())

#length of the bio message
length = len(bio_messsage.strip())
print("Length of your bio is : " + str(length))

#Replace 'I am ' with 'I'm' in the bio message
updated_bio = bio_messsage.replace('I am', "I'm")
print("Here is your updated bio : " + updated_bio.strip())

#use if f-string method
print(f"My fullname is {first_name} {last_name} and my bio is {updated_bio.strip()}. /nThe length of the bio message is {length} characters long.")
