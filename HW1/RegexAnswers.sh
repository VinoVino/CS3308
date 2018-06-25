#!/bin/bash
#James Covino

#1)How many lines end with a number?
egrep -c [0-9]$ $1

#2)How many lines do not start with a vowel?
egrep -c ^[^aeiouAEIOU] $1

#3)How many 12 letter (alphabet only) lines?
egrep -c "^[A-Za-z]{12}$"  $1

#4)How many phone numbers are in the dataset (format: ‘_ _ _ -_ _ _ - _ _ _ _’)?
# don't count numbers like this 720-848-6161/86159
egrep -c ^[0-9]{3}-[0-9]{3}-[0-9]{4}$  $1

#5)How many city of Boulder phone numbers (Eg: starting with 303-_ _ _ - _ _ _ _)?
# don't count 303-724-6577/4-6110
egrep -c ^303-[0-9]{3}-[0-9]{4}$ $1 


#6)How many begin with a vowel and end with a number?
egrep ^[aeiouAEIOU] $1 | egrep -c [0-9]$ 


#7)How many email addresses are from geocities? (Eg: end with'geocities.com')?
egrep -c .+@geocities'\.'com $1


#8) How many email addresses are in ‘first.last’ name format and involve someone who’s first name starts with a letter in the first half of the alphabet?
egrep .+'\.'.+@.+'\.'.+ $1 | cut -d'.' -f1 | egrep -c ^[a-mA-M]