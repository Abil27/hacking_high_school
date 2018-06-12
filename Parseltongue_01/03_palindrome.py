# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    03_palindrome.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahoussei <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/10 20:11:52 by ahoussei          #+#    #+#              #
#    Updated: 2018/06/10 20:11:55 by ahoussei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def process_text(text):
    text = text.lower()
    forbidden = (' ', '.', '?', '!', ':', ';', '-', '—', '(', ')', '[', ']', '’', '“', '”', '/', ',', '"')
    for i in forbidden:
        text = text.replace(i, '')
    return text

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    new = process_text(text)
    return new == reverse(new)

check_palindrome = input('Enter text: ')
if (is_palindrome(check_palindrome)):
    print("Awesome, your text is a palindrome")
else:
    print("Sorry, it is not a palindrome")