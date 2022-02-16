# create a simple random story generator

import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 14th Feb']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
residence = ['Kenya','Uganda', 'Tanzania', 'Rwanda', 'South Africa']
went = ['cinema', 'university','seminar', 'school', 'laundry']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) 
+ ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
