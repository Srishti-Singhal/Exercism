Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def convert(number):
    return (("" if number % 3 else "Pling") + ("" if number % 5 else "Plang") + ("" if number % 7 else "Plong")) or str(number)
