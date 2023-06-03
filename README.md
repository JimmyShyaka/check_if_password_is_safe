'''
The goal of this project is to create an API that is going to check how many times a
password is found in the public database of the leaked passwords which will tell us
how safe our password is.

We use a hashing function to hash the password we want to check and
then we split the hashed value into 2 parts: The first part is the first 5 characters of the hash
and the second part is the rest of the characters of the hash that we call "tail".

We check if the first 5 characters of the hashed value of the password appeared in the public
database there and return a list of all hashes of passwords that are found to match our first five hash characters.

Why all of that process? The answer is that we don't want to query the database using all hashed
characters of our password because that would be a vulnerability if we sent to that public database
a query with the entire hashed value of the password we want to check.

It would be a vulnerability because we are sending that hashed value over the
public internet, a bad actor could find out the hashed value of the password
we are checking. That bad actor can reverse engineer the password using that hashed value.

Instead, we will query the public database using the first 5 characters
of the hashed value of our password. Then we will return a long list
of all hashed values found in the database that match our password's first 5 hashed values.

We will have the list of those hashes on our machine locally which is safe
and then count how many times the "tail" part of our password hash (which we never shared with anyone)
appeared in that list we just got from the public database. That count is how many
times our password appeared in the public database of leaked passwords.

If the password is not found in the database, then the program will exit with
a message letting you know that "the password was not found. The password is safe. Carry on!"

The goal is to avoid using a password that is on that public
list of leaked passwords.

When you run the program it will ask you to type in
the password to be checked. Alternatively, you can input a file containing
a list of passwords you want to check. I like the second method because
if you type the password in the terminal with the first method of executing
the program, the password will be saved in the history in the CLI on your computer
which is not a best security practice.

'''

# Below is an example of password checks from cli:


#type "break" to exit

#password: hello   <------------- entered this weak password

#hello was found 264691 times <--it appeared this many times in that public database

#type "break" to exit



#password: 12345  <-------entered this weak password to check again

#12345 was found 2591816 times <--it appeared this many times in that public database

#type "break" to exit

#password:
