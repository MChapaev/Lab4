from pathlib import Path

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


# Main
if __name__ == "__main__":
    current_folder = Path(__file__).resolve().parent / "Files"
    message = open(current_folder / "Task2.txt", "r", encoding="utf-8").readline()
    print(f"Original message: {message}")
    print(f"Decoded message: {shift_message(message)}")

