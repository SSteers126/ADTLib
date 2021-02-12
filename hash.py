# Hashes are basically a way to identify a piece of data without directly storing the original item.
# This makes hashing a good way to store passwords, as it keeps the ability to (mostly) identify the correct data,
# Without keeping the password in plaintext, which could be easily stolen.
import secrets
# secrets.token_bytes(256)  # This when unhashed will give a secure salt that can be used in place of the current one. You can try it by printing it and copying the new one into the function.
import hashlib  # You may need to install pyopenssl to use this

def fold_hash(pw, salt=None):
    list_vals = []
    comb_vals = []
    hashed = 0
    counter = 0
    for i in pw:
        list_vals.append(ord(i))
    for i in list_vals:
        if counter == (len(list_vals) - 1):
            comb_vals.append(i)
        if counter % 2 == 0 and counter < (len(list_vals) - 1):
            combine = str(list_vals[counter]) + str(list_vals[(counter + 1)])
            comb_vals.append(int(combine))
            counter = counter + 1
        elif counter % 2 != 0:
            counter = counter + 1
    for i in comb_vals:
        hashed = hashed + i
    if salt is not None:
        list_vals = []
        comb_vals = []

        for i in salt:
            list_vals.append(ord(i))
        for i in list_vals:
            if counter == (len(list_vals) - 1):
                comb_vals.append(i)
            if counter % 2 == 0 and counter < (len(list_vals) - 1):
                combine = str(list_vals[counter]) + str(list_vals[(counter + 1)])
                comb_vals.append(int(combine))
                counter = counter + 1
            elif counter % 2 != 0:
                counter = counter + 1
        for i in comb_vals:
            hashed = hashed + i
    return hashed

# This is a hash function similar to fold. The way it combines the numbers is slightly different, however the basic function is similar.
# Note that salting is not available in a normal fold hash. Salting here adds the number to the output differently, so
# That it isn't *as* predictable. Although for the NEA this is good, in actual practice it is not good, as it collides
# Considerably.

# For a more secure way to hash, sha is a popular and well performing way round this.



def hash_SHA(pw):
    # This is a secure salt which is used to alter the hash in a repeatable way, which cannot be replicated without it
    salt = 'uD\xd0f\x91#\xe7E\x00^\xcf\xeeW\xb8\xaaq[\xe3\x94>\x11\x0b5J~!\xa2\xf1z\x8e\xe1\x96\xf5\xf8v\xfb\x1c/eqj\xf3u{\x89M{\xdf\x04\xdb\xef\xe1oV\xd2ww\'\'\x05R)\x8f)\x13>b`j\x87\xaa\x133p\xdc\xff\xb3o\x8d\xdaTD\x1b\xcb\xbc\x0fX\x04)\xab\xcd\xd0\x86\x9f\xfb\x98\x95Oze\xf6\x15\xc2J)\xda"\n\x00\n\xc6*\xf8B\xde\x88\xf4\xbe\xc3\xf2?\xf4=~\x9e^ss~\x0cE{\xf3\x8e\xa69\xd0\x93E\xdf\x9f\x90\x86/\xc7\x1fu\x0e\xf1\x04\xa3\x12\xcf\x88Y,\xbdEdI\x15\xa2#m\xa6\nl\tnwp\xb3e\xb9\x11\xa9\x99i\xce$\x00\xd4\x8a\xf9c\xb7\x9d]\xf5\x9b\x87{I<\xe0\x91a\x9a\xbe\x11\x10a\x89\r\xf3\xf0\x04{\nN`\xf3C\x9bKA\x8ef\x12\xc7\x94\xb0\x9fS\xef\x80\x89\xe7\x82!B\x83X~\xc9n\xe6\xc0\x84\x15\x8b\x93^\x00\xcf`v\xc7WY\xe4\x9fRj\x9ce'
    salte = salt.encode("utf-8")
    pwe = pw.encode("utf-8")
    hashed = hashlib.pbkdf2_hmac('sha512', pwe, salte, 250000)  # (method, password, salt, iterations)
    # Remember that the amount of iterations directly affects time taken. The minimum secure amount of itertions is 100000.
    hashed = hashed.hex()  # Converting to hex is not mandatory, however note that not doing so will give a bytes-like object, not a string.
    return hashed

print(hash_SHA("hello"))