import bcrypt

# Create a password hash
def createPasswordHash(password):
    passwordBytes = password.encode('utf8')

    salt = bcrypt.gensalt(14)
    passwordHashBytes = bcrypt.hashpw(passwordBytes, salt)
    passwordHashString = passwordHashBytes.decode()

    return passwordHashString

# Check the user supplied password against the hashed password
def comparePassword(password,passwordHash):
    if bcrypt.checkpw(password.encode('utf8'), passwordHash.encode('utf8')):
        return True
    else:
        return False
