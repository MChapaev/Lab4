# Shifting
def shift_message(message):
    shifted_message = ''
    for char in message:
        if 'а' <= char <= 'я':
            shifted_message += chr(ord(char) - 1) if char != 'а' else 'я'
        elif 'А' <= char <= 'Я':
            shifted_message += chr(ord(char) - 1) if char != 'А' else 'Я'
        else:
            shifted_message += char
    return shifted_message