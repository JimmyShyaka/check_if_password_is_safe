# The goal of this project is to create this API that is going to check how many times a password is found in the public database of the leaked password which will tell us how strong our password is.

# We use hashing function to hash our password we want to check and then we split the hashed value in 2 parts: The first 5 characters of the hash and the rest of the characters of the hash that we call tail. We use the first five characters of the hash to check that public database of hacked/leaked passwords to see if our password's first 5 characters of the hashed value appeared in the public database there and return all hashed strings that if found to match our first five hashes.

# Why all of that process? Answer is because we don't want to query the database using all hashed characters of our password because that would be a vulnerability if we disclosed the hashed value of the password we want to check.

# It would be a vulnerability because we are sending that hashed value over the public internet, a bad actor could find out our hashed value of our password we are checking. That bad actor can reverse engineer the hashed value and find out our password.

# Instead, we will query the public database using the first 5 characters of our password hashed value, then we will return a long list of all hashed values found in the database that match with our password first 5 hashed values. Then we will have the list of those hashes on our machine locally and then count how many times the tail part of our password hashed value appeared in that list we just got from the public database.

# We will count how many times the tail part is found in the list and print it on the screen

# If the password is not found from the database, then the program will exit with a message letting you know that "the password was not found. The password is safe. Carry on!"

# The goal is to avoid using a password that has been found to be on that public list of leaked passwords
