#!/usr/bin/env python3

# importing required modules
from sys import argv, exit
import requests

"""
Language Translate Application wiht google translate API
"""

def translate(sl, tl, contents):
    """Translate the input to a specified language and print the output"""
    # URL with api key
    url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=%25s&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e&"
    
    payload = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'sl': sl,
        'tl': tl,
        'q': contents
    }

    # make a request to the api
    response = requests.post(url, data=payload)

    # Format the response the print the output
    translated_data = response.json()
    translated_text = translated_data['sentences'][0]['trans']
    print(translated_text)

def usage():
    """Help or Usage"""
    print(f"Usage: {argv[0]} [-f, --file] <file-name>")
    print(f"       {argv[0]} <words-to-translate>\n")

def main():
    # Taking user input
    if len(argv) < 2 or argv[1] == "-h" or argv[1] == "--help":
        usage()
        exit(0)
    elif argv[1] == "-f" or argv[1] == "--file":
        if len(argv) != 3:
            usage()
            exit(1)
        else:
            try:
                contents = []
                with open(argv[2], "r") as file:
                    data = file.readlines()
                    for line in data:
                        contents.append(line.strip())
            except Exception as e:
                print(e)
                exit(1)

            # Input from a file
            print("\nNOTE: If you get an error then Google has blocked you for making too many requests!!")
            print("\nTo view the supported language list, check https://cloud.google.com/translate/docs/languages\n")
            sl = input("Enter the code for source language: ")
            tl = input("Enter the code for translate language: ")

            # Output the text to be translated
            print("\nOriginal Text:")
            for line in data:
                print(line.strip())

            # Make a call to translate function
            print("\nTranslated Text:")
            for content in contents:
                translate(sl, tl, content)
            print()
    else:
        # input as command line argument
        if len(argv) == 2:
            print("\nNOTE: If you get an error then Google has blocked you for making too many requests!!")
            print("To view the supported language list, check https://cloud.google.com/translate/docs/languages\n")
            sl = input("Enter the code for source language: ")
            tl = input("Enter the code for translate language: ")
            contents = argv[1]

            # Output the text to be translated
            print("\nOriginal Text:")
            print(contents)

            # Make a call to translate function
            print("\nTranslated Text:")
            translate(sl, tl, contents)
            print()

main()