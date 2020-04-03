MAX_ROMAN_VALUE = 3999

# Arabic to Roman conversion
def arabicToRoman(arabicNumeral):
    romanUnits = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    romanTens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    romanHundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    romanThousands = ['', 'M', 'MM', 'MMM']
    romanDigits = [romanThousands, romanHundreds, romanTens, romanUnits]
    romanNumeral = ''

    for i in range(-len(arabicNumeral), 0, 1):
        romanNumeral += romanDigits[i][int(arabicNumeral[i])]

    return romanNumeral


# Roman to Arabic conversion
def romanToArabic(romanNumeral):
    romanUnits = ['IX', 'VIII', 'VII', 'VI', 'IV', 'V', 'III', 'II', 'I']
    romanTens = ['XC', 'LXXX', 'LXX', 'LX', 'XL', 'L', 'XXX', 'XX', 'X']
    romanHundreds = ['CM', 'DCCC', 'DCC', 'DC', 'CD', 'D', 'CCC', 'CC', 'C']
    romanThousands = ['MMM', 'MM', 'M']
    romanDigits = [romanUnits, romanTens, romanHundreds, romanThousands]
    arabicNumeral = 0

    for i in range(len(romanDigits)):
        for k in range(len(romanDigits[i])):
            if romanDigits[i][k] in romanNumeral:
                if romanDigits[i][k] in ['IV', 'XL', 'CD']:
                    arabicNumeral += (len(romanDigits[i]) - k - 1) * 10 ** i
                elif romanDigits[i][k] in ['V', 'L', 'D']:
                    arabicNumeral += (len(romanDigits[i]) - k + 1) * 10 ** i
                else:
                    arabicNumeral += (len(romanDigits[i]) - k) * 10 ** i

                romanNumeral = romanNumeral.replace(romanDigits[i][k], '')
                break

    return str(int(arabicNumeral))

# Operations on Roman numerals: addition, subtraction, multiplication, and division
def romanAddition(firstRomanNumeral, secondRomanNumeral):
    if not isRomanNumeral(firstRomanNumeral) or not isRomanNumeral(secondRomanNumeral):
        print('ERROR: invalid input argument(s)')
        return -1

    result = int(romanToArabic(firstRomanNumeral)) + int(romanToArabic(secondRomanNumeral))
    if result > MAX_ROMAN_VALUE:
        print(f'ERROR: The resulting value is greater than {MAX_ROMAN_VALUE}')
        return -1

    return arabicToRoman(str(result))


def romanSubtraction(firstRomanNumeral, secondRomanNumeral):
    if not isRomanNumeral(firstRomanNumeral) or not isRomanNumeral(secondRomanNumeral):
        print('ERROR: invalid input argument(s)')
        return -1

    result = int(romanToArabic(firstRomanNumeral)) - int(romanToArabic(secondRomanNumeral))
    if result > MAX_ROMAN_VALUE:
        print(f'ERROR: The resulting value is greater than {MAX_ROMAN_VALUE}')
        return -1

    return arabicToRoman(str(result))


def romanMultiplication(firstRomanNumeral, secondRomanNumeral):
    if not isRomanNumeral(firstRomanNumeral) or not isRomanNumeral(secondRomanNumeral):
        print('ERROR: invalid input argument(s)')
        return -1

    result = int(romanToArabic(firstRomanNumeral)) * int(romanToArabic(secondRomanNumeral))
    if result > MAX_ROMAN_VALUE:
        print(f'ERROR: The resulting value is greater than {MAX_ROMAN_VALUE}')
        return -1

    return arabicToRoman(str(result))


def romanDivision(firstRomanNumeral, secondRomanNumeral):
    if not isRomanNumeral(firstRomanNumeral) or not isRomanNumeral(secondRomanNumeral):
        print('ERROR: invalid input argument(s)')
        return -1

    result = int(romanToArabic(firstRomanNumeral)) / int(romanToArabic(secondRomanNumeral))
    if result > MAX_ROMAN_VALUE:
        print(f'ERROR: The resulting value is greater than {MAX_ROMAN_VALUE}')
        return -1

    return arabicToRoman(str(int(result)))

# Checking validity of an input argument
def isRomanNumeral(romanNumeral):
    return romanNumeral == arabicToRoman(romanToArabic(romanNumeral))

# Calculator
def romanCalculator(expression):
    result = ''
    if '+' in expression:
        expression = expression.split('+')
        result = romanAddition(expression[0].strip(), expression[1].strip())
    elif '-' in expression:
        expression = expression.split('-')
        result = romanSubtraction(expression[0].strip(), expression[1].strip())
    elif '*' in expression:
        expression = expression.split('*')
        result = romanMultiplication(expression[0].strip(), expression[1].strip())
    elif '/' in expression:
        expression = expression.split('/')
        result = romanDivision(expression[0].strip(), expression[1].strip())

    return result

# main function
def main():
    while True:
        expression = input("Please enter the input expression: ")
        print(romanCalculator(expression))

        choice = input("Would you like to enter another expression (y/n)? ")
        if choice.lower() != 'y':
            print("Bye")
            break

if __name__ == "__main__":
    main()
