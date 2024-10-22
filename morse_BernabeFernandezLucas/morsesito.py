import char

morse_dictionary = {
    'A': '.-', 'B': '-..' , 'C' : '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' ', ',': '--..--', '.': '.-.-.-', '?': '..--..', '!': '-.-.--'
}
#Funcion para convertir texto a codigo morse
def texto_morse(text):
    text = text.upper() #Para convertir el texto en mayusculas
    morse_code = ' '.join(morse_dictionary[char] for char in text if char in morse_dictionary)
    return morse_code

#Funcion para convertir el codigo de Morse a texto
def morse_texto(morse):
    morsePalabra = morse.split('  ')
    decodificacion = ''

    for word in morsePalabra:
        morseCaracter = word.split(' ')
        for char in morseCaracter:
            for letra, codigo in morse_dictionary.items():
                if codigo == char:
                    decodificacion += letra
                    break
        decodificacion += '' #añade espacio entre palabras

    return decodificacion.strip() #Elimina espacios innecesarios

#funcion principal
def main():
    while True:
        print("\n Menu:")
        print("1. Convertir texto a morse")
        print("2. Convertir morse a texto")
        print("3. Salir")

        option = input("Elige una opción por favóh: ")

        if option == '1':
            texto = input("Introduce el texto a convertir: ")
            print("Código Morse: ", texto_morse(texto))
        elif option == '2':
            morse = input("Introduce el texto a morse a convertir: ")
            print("Texto: ", morse_texto(morse))
        elif option == '3':
            print("Saliendo...")
            break
        else:
            print("Esto...esto no vale eh")

if __name__ == "__main__":
    main()
