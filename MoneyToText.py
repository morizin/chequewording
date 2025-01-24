class NumberToWords:
    def __init__(self):
        self.text = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 
            8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 
            19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety",
            100: "Hundred", 1000: "Thousand", 100000: "Lakh", 10000000: "Crore"
        }
        self.powers = [10000000, 100000, 1000, 100, 10, 1]

    def convert_two_digit(self, num):
        if num <= 20:
            return self.text.get(num, "")
        tens, ones = divmod(num, 10)
        return f"{self.text.get(tens*10, '')} {self.text.get(ones, '')}".strip()

    def convert_to_words(self, num, currency='Rupees'):
        if num == 0:
            return f"Zero {currency} Only"
        
        if num < 0:
            return f"Minus {self.convert_to_words(abs(num), currency)}"

        result = []
        for power in self.powers:
            if num >= power:
                quotient, remainder = divmod(num, power)
                
                if power >= 100:
                    power_word = self.text.get(power)
                    word = self.convert_to_words(quotient) + " " + power_word
                    result.append(word.strip())
                
                num = remainder

        # Handle the last part
        if num > 0:
            result.append(self.convert_two_digit(num))

        return " ".join(result).strip() + f" {currency} Only"

def main():
    try:
        # Get input with error handling
        num = int(input('Enter amount: '))
        currency = input('Enter Currency (default: Rupees): ') or 'Rupees'
        
        # Convert and print
        converter = NumberToWords()
        print(converter.convert_to_words(num, currency))
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()