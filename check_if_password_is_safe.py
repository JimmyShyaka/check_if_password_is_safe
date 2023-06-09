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

import requests   #import these 2 libraries
import hashlib

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code} check the API')
    return res
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)
def main(args):
    count = pwned_api_check(args)
    if count:
        print(f'{args} was found {count} times')
    else:
        print(f'{args} was not found. The password is safe. Carry on!')
if __name__ == '__main__':
    while True:
        password = input('type "break" to exit\npassword: ')
        
        if password == 'break':
            break
        main(password)