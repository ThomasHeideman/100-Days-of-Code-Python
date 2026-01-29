friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random
random_number = random.randint(0, (len(friends)-1) )
print(friends[random_number])


# or using random.choice() function
print(random.choice(friends))