import datetime

def get_encoding_mapping(day_type):
    if day_type == 'odd':
        return {chr(i + 64): f"{i:02d}" for i in range(1, 27)}
    elif day_type == 'even':
        return {chr(i + 64): f"5{i:02d}" for i in range(1, 27)}
    return {}

def determine_day_type():
    today = datetime.date.today()
    return 'odd' if today.day % 2 != 0 else 'even'

def encode_message(message):
    day_type = determine_day_type()
    encoding_map = get_encoding_mapping(day_type)
    encoded_message = []

    for char in message.upper():
        if char in encoding_map:
            encoded_message.append(encoding_map[char])
        elif char == ' ':
            encoded_message.append(' ')
    
    return ''.join(encoded_message)
