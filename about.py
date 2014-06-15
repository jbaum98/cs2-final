#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
print "<!DOCTYPE html>"

import cgi
import cgitb
cgitb.enable()
fs = cgi.FieldStorage()

# = fs[''].value

from play_lib import *

print '''
<html>
    <head>
        <link href="./vendor/font.woff" rel='stylesheet' type='text/css'>
        <link rel="stylesheet" type="text/css" href="./frontend/about.css">
    </head>
    <body>
        <h1>About Tic-Tac-Toe</h1>
'''

# current date and time information

print '''
<p>This page is a study of machine learning, using the model game of Tic-Tac-Toe. Each time the user plays a game, data about the success of chosen moves is added to the computer's memory. The computer then uses this memory to choose future moves, becoming more intelligent about the game as it plays more often. Data below displays statistics about the computer's gameplay for both its entire memory, and the current date. Note that wins are considered successful, ties are considered half as successful, and losses are not considered successful.</p>
        
        <h2>Current Statistics</h2>
        <table>
            <tr>
                <th>Number of Games</th>
                <th>Wins</th>
                <th>Losses</th>
                <th>Ties</th>
                <th><font color="#CC66FF">Success Rate</font></th>
                <th>Difference from Today's Rate</th>
            </tr>
'''

# table row with cumulative information

print '''
</table>
        <br>
        <h2>Today's Statistics</h2>
        <table>
            <tr>
                <th>Number of Games</th>
                <th>Wins</th>
                <th>Losses</th>
                <th>Ties</th>
                <th><font color="#CC66FF">Success Rate</font></th>
                <th>Difference from Today's Rate</th>
            </tr>
'''

# table row with daily statistics