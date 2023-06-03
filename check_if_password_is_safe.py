
# The goal of this project is to create this API that is going to check how many times a password is found in the public database of the leaked password which will tell us how strong our password is.
# We use hashing function to hash our password we want to check and then we split the hashed value in 2 parts: The first 5 characters of the hash and the rest of the characters of the hash that we call tail. We use the first five characters of the hash to check that public database of hacked/leaked passwords to see if our password's first 5 characters of the hashed value appeared in the public database there and return all hashed strings that if found to match our first five hashes.
# Why all of that process? Answer is because we don't want to query the database using all hashed characters of our password because that would be a vulnerability if we disclosed the hashed value of the password we want to check.
# It would be a vulnerability because we are sending that hashed value over the public internet, a bad actor could find out our hashed value of our password we are checking. That bad actor can reverse engineer the hashed value and find out our password.
# Instead, we will query the public database using the first 5 characters of our password hashed value, then we will return a long list of all hashed values found in the database that match with our password first 5 hashed values. Then we will have the list of those hashes on our machine locally and then count how many times the tail part of our password hashed value appeared in that list we just got from the public database.
# We will count how many times the tail part is found in the list and print it on the screen
# If the password is not found from the database, then the program will exit with a message letting you know that "the password was not found. The password is safe. Carry on!"
# The goal is to avoid using a password that has been found to be on that public list of leaked passwords


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