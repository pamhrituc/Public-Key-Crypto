# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:01:58 2019

@author: spamt
"""
import string
from _sre import ascii_tolower

plaintext_dict = {' ': 0}
ciphertext_dict = {' ': 0}

i = 1
for letter in string.ascii_lowercase:
    plaintext_dict[letter] = i
    i += 1

i = 1
for letter in string.ascii_uppercase:
    ciphertext_dict[letter] = i
    i += 1
    
def keyForValue(dict, value):
    for key in dict.keys():
        if dict[key] == value:
            return key
    return

def encodeText(plaintext, key):
    """
    Function that encodes a message using a key
    Input:
        plaintext => message to be encoded
        key => key used to encode the message
    Output:
        ciphertext => encoded message
    """
    ciphertext = ''
    for letter in plaintext:
       ciphertext += keyForValue(ciphertext_dict, (plaintext_dict[letter] + key) % 27)
    return ciphertext

def decodeText(ciphertext, key):
    """
    Function that decodes a message using a key
    Input:
        ciphertext => message to be decoded
        key => key used to decode the message
    Output:
        plaintext => decoded message
    """
    plaintext = ''
    for letter in ciphertext:
       plaintext += keyForValue(plaintext_dict, (ciphertext_dict[letter] - key) % 27)
    return plaintext

def validatePlaintext(input_text):
    """
    Function that validates the input given by the user for encoding
    Input:
        input_text => user input
    Output:
        true, if input contains only lowercase letters
        false, otherwise
    """
    return input_text.islower()

def validateCiphertext(input_text):
    """
    Function that validates the input given by the user for decoding
    Input:
        input_text => user input
    Output:
        true, if input contains only uppercase letters
        false, otherwise
    """
    return input_text.isupper()

def printMenu():
    menu = "1. Encode a message.\n"
    menu += "2. Decode a message.\n"
    menu += "0. Exit.\n"
    print(menu)

def run():
    print("Caeser Cipher Encoder/Decoder")
    run = True
    while (run):
        printMenu()
        option = input("Option: ")
        if option == '0':
            run = False
            print("Goodbye")
        elif option == '1':
            plaintext = ''
            while(validatePlaintext(plaintext) == False):
                plaintext = input("Plaintext: ")
            key = input("Key: ")
            while (key.isdecimal() == False or int(key) < 0):
                print("The key should be a positive number")
                key = input("Key: ")
            key = int(key)
            print("The encoded message is: " + encodeText(plaintext, key))
        elif option == '2':
            ciphertext = ''
            while(validateCiphertext(ciphertext) == False):
                ciphertext = input("Ciphertext: ")
            key = int(input("Key: "))
            print("The decoded message is: " + decodeText(ciphertext, key))
        else:
            print("Invalid option")
            