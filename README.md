# gtfobins
Script to search SUID binaries in GTFO bins

Input : Accepts text file as input

Output : Prints all binaries where exploit is found in GTFObins

Steps to run 

1. Run find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
2. Copy the output of the above command in txt file.
3. Run this script & provide the above txt file as input.
