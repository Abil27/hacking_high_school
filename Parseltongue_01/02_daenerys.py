# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_daenerys.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahoussei <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/10 18:38:39 by ahoussei          #+#    #+#              #
#    Updated: 2018/06/10 18:38:41 by ahoussei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

longname = "Daenerys of the House Targaryen, the First of Her Name, The Unburnt, Queen of the Andals, the Rhoynar and the First Men, Queen of Meereen, Khaleesi of the Great Grass Sea, Protector of the Realm, Lady Regnant of the Seven Kingdoms, Breaker of Chains and Mother of Dragons"

daenerys = input("Who goes there?\n")

if daenerys == "DHTFHNUQARFMQMKGSPRLRSKBCMD" or daenerys == longname:
    print("Welcome, Daenerys")
elif daenerys == "Dany":
    print("Dany who?")
else:
    print("Move along, now.")
