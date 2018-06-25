#!/bin/bash
# James Covino
#cat StudentGrades.txt |  while read a b c d e f; do echo "$((($d+$e+$f)/3)) [$a] $c, $b "; done| sort -t' ' -k3,4
# one liner version
# script assumes txt file input ends with a newline character- following C convention
echo Report
cat $1 |  while read a b c d e f; do echo "$((($d+$e+$f)/3)) [$a] $c, $b "; done| sort -t' ' -k3,4   
