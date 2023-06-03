# The goal of this project is to create this API that is going to check how many times a password is found in the public database of the leaked password which will tell us how strong our password is.

# We use hashing function to hash our password we want to check and then we split the hashed value in 2 parts: The first part is the first 5 characters of the hash and the second part is the rest of the characters of the hash that we call tail. We use the first five characters of the hash to check that public database of hacked/leaked passwords to see if the first 5 characters of the hashed value of the password appeared in the public database there and return a list of all hashed strings that are found to match our first five hashes.

# Why all of that process? Answer is because we don't want to query the database using all hashed characters of our password because that would be a vulnerability if we disclosed the hashed value of the password we want to check.

# It would be a vulnerability because we are sending that hashed value over the public internet, a bad actor could find out our hashed value of our password we are checking. That bad actor can reverse engineer the hashed value and find out our password.

# Instead, we will query the public database using the first 5 characters of our the hashed value of our password. Then we will return a long list of all hashed values found in the database that match with our password first 5 hashed values. We will have the list of those hashes on our machine locally which is safe and then count how many times the tail part of our password hashed value appeared in that list we just got from the public database.

# We will count how many times the tail part is found in the list and print it on the screen. That count is how many times our password appeared in the database.

# If the password is not found from the database, then the program will exit with a message letting you know that "the password was not found. The password is safe. Carry on!"

# The goal is to avoid using a password that has been found to be on that public list of leaked passwords


# When you run the program it will ask you to type in the password to be checked. Alternatively you can input a file containing a list of passwords you want to check. I like the second method because if you type the password in the terminal with the first method of executing the program, the password will be saved in history on your computer which is not a best security practice.

# Below is an example of passord checks from cli:


#type "break" to exit

#password: hello

#hello was found 264691 times

#type "break" to exit


#password: 12345

#12345 was found 2591816 times

#type "break" to exit

#password: 
