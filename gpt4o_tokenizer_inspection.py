import tiktoken

# Initialize tiktoken encoding
T = tiktoken.get_encoding("o200k_base")

# Function to check if a token is Korean based on Unicode ranges
def is_korean(text):
    # Define the ranges for Korean characters
    hangul_syllables = range(0xAC00, 0xD7AF + 1)
    hangul_jamo = range(0x1100, 0x11FF + 1)
    hangul_compatibility_jamo = range(0x3130, 0x318F + 1)
    
    for char in text:
        if ord(char) in hangul_syllables or ord(char) in hangul_jamo or ord(char) in hangul_compatibility_jamo:
            return True
    return False

def main():
    # List to store Korean tokens and their lengths
    korean_tokens = []

    # Iterate through all tokens and process them
    for i in range(T.n_vocab):
        try:
            decoded_token = T.decode([i])
            if is_korean(decoded_token):
                korean_tokens.append((i, decoded_token, len(decoded_token)))
        except:
            continue

    # Sort the list by length in descending order
    korean_tokens.sort(key=lambda item: -item[2])

    # Write the Korean tokens and their lengths to a text file
    with open('korean_tokens.txt', 'w', encoding='utf-8') as file:
        for token_id, decoded_token, length in korean_tokens:
            file.write(f"{token_id}: {decoded_token} (Length: {length})\n")

if __name__ == "__main__":
    main()
