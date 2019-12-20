A Simple Coding Question:

Given a file that contains a log (timestamp, customer id, page id), please write a script to parse it and output the list of pages visited by each customer. Write this script in your preferred language, and place it in /interview in the instance once complete.

Input CSV File:

Time, Customer ID, Page ID

1, C1, P1
2, C2, P2
3, C3, P3
4, C2, P1
5, C2, P3
6, C2, P2
7, C1, P3
8, C1, P2
9, C3, P1
10, C2, P1
11, C2, P3
12, C2, P2
13, C1, P1
14, C1, P3
15, C1, P2


Example execution of script.  The Customer ID must be passed as a parameter.
./script "C1"

Output:
P1, P3, P2, P1, P3, P2