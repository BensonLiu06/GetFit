import bcrypt

# Create a password hash
def createPasswordHash(password):
    # Encode the password
    passwordBytes = password.encode('utf8')

    # Specify the salt
    salt = bcrypt.gensalt(14)

    # Encrypt the password using the bcrypt algorithm with the provided salt
    passwordHashBytes = bcrypt.hashpw(passwordBytes, salt)

    # Decode the hashed password
    passwordHashString = passwordHashBytes.decode()

    return passwordHashString

# Check the user supplied password against the hashed password
def comparePassword(password,passwordHash):
    if bcrypt.checkpw(password.encode('utf8'), passwordHash.encode('utf8')):
        return True
    else:
        return False