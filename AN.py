alfabetoN = {
    'A': '¢', 'B':'+', 'C': '#', 'D': '@',
    'E': '*', 'F': '"', "G": "'", 'H': '&',
    'I': ':', 'J': ';', 'K': '(', 'L': ')',
    'M': '?', 'N': '!', 'O': '$', 'P': '_',
    'Q': '-', 'R': '~', 'S': '|', 'T': '{',
    'U': '}', 'V': '%', 'W': '=', 'X': '^',
    'Y': '×', 'Z': '£', ' ': '/'
}

AN_TO_TEXT = {value: key for key, value in alfabetoN.items()}

def traduzir_to_AN(text):
    text = text.upper()
    AN = []
    for char in text:
        char = char.replace('Á', 'A').replace('À', 'A').replace('Ã', 'A').replace('Â', 'A').replace('Ä', 'A') \
           .replace('É', 'E').replace('È', 'E').replace('Ê', 'E').replace('Ë', 'E') \
           .replace('Í', 'I').replace('Ì', 'I').replace('Î', 'I').replace('Ï', 'I') \
           .replace('Ó', 'O').replace('Ò', 'O').replace('Õ', 'O').replace('Ô', 'O').replace('Ö', 'O') \
           .replace('Ú', 'U').replace('Ù', 'U').replace('Û', 'U').replace('Ü', 'U') \
           .replace('Ç', 'C').replace('Ñ', 'N')
        if char in alfabetoN:
            AN.append(alfabetoN[char])
        else:
            return f"[ERRO]: Caractere '{char}' não suportado em AN."
    return ' '.join(AN)

def traduzir_from_AN(AN):
    AN = AN.strip()
    words = AN.split(' / ')
    decoded_text = []
    for word in words:
        letters = word.split()
        for letter in letters:
            if letter in AN_TO_TEXT:
                decoded_text.append(AN_TO_TEXT[letter])
            else:
                return f"[ERRO]: Caractere AN '{letter}' inválido."
        decoded_text.append(' ')
    return ''.join(decoded_text).strip()
