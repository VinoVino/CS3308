#!/bin/bash
#James Covino
#cat StudentGrades.txt | awk 'BEGIN {print "Report";}{print (($4+$5+$6)/3) " ["$1"] " $3", " $2 ;} END{;}' | sort -t' ' -k3,4
# one liner version
cat $1 | awk 'BEGIN {print "Report";}{print int(($4+$5+$6)/3) " ["$1"] " $3", " $2 ;} END{;}' | sort -t' ' -k3,4