# Michael Manzella
# 01-OCT-20
# (11)  BOOK CLUB POINTS (page 134)
# 
# Serendipity Booksellers has a book club that awards points to its customers
# based on the number of books purchased each month. The points are awarded as follows:
# 
# If a customer purchases 0 books, he or she earns 0 points.
# 
# If a customer purchases 2 books, he or she earns 5 points.
# 
# If a customer purchases 4 books, he or she earns 15 points.
# 
# If a customer purchases 6 books, he or she earns 30 points.
# 
# If a customer purchases 8 or more books, he or she earns 60 points.

books = int(input('Enter amount of books: '))
    
if books >= 8:
    points = 60
elif books >= 6 and books < 8:
    points = 30
elif books >= 4 and books < 6:
    points = 15
elif books >= 2 and books < 4:
    points = 5
else:
    points = 0
    
print('You have',points,'points')

# OUTPUT
# Enter amount of books: 100
# You have 60 points
    
