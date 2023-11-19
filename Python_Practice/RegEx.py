import re
#--------------------------------------------------------------------------------------------------------------------------------
'''
.   -Any character expect new lines
\d  -Any digit (0-9)
\D  -Not a digit (0-9)
\w  -Word character (a-zA-Z0-9_) underscore also included
\W  -Not a word character
\s  -Whitespace character like space, tab, newline
\S  -Not a whitespace character

Anchors
\b  -Word Boundary
\B  -Not a Boundary
^   -Beginning of a string
$   -End of string

[]  -Match chars in brackets #calles character set
[-] -Dash creates a range from the first value to second value
[^ ]-Negates everything in that charcter set
|   -Either or
( ) _Group

Quantifiers
*   -0 or More
+   -1 or More
?   -0 or One
{3} -Exact Number
{3,4}Range of Numbers (Min, Max)

Re methods
findall()   -returns matched objs with extra info; returns iterable
findall()   -returns a list of matched expressions, but only returns the first group; returns iterable
match()     -determine if regex matches at the beginning of the string; only the first word; prints only the first match, not all
search()    -prints the first occurence of the regex in the string; searches through the entire string

FLAGS
re.ignorecase || re.I   -ignores the case


'''
#--------------------------------------------------------------------------------------------------------------------------------

text = '''
abcdefghijklmnopqrstuvqxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
!@#$%^&*()
Ha Haha

. ^ $ { } [ ] \ |

Ash Adhi

ayusnad@gmail.com
720-299-2225

Mr. Adhikari
Ms Greene
Miss Grande
Mr Black
Mr. White
Mrs Sitaula
'''
emails = '''
https://www.google.com
http://randomwebsite.com
https://youtube.com
https://www.reddit.com/trending

'''

names = re.compile(r'(Mr|Mrs|Ms|Miss)\.*\s*[a-zA-Z]+')
email = re.compile(r'https?://(www\.)?(\w+)(\.\w+)(/\w+)?')

matches = email.finditer(emails)
# for match in matches:
#     # print(match.group(2))
subbed_urls = email.sub(r'\2\3\4', emails)
print(subbed_urls)
