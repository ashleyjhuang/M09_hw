from booklover import BookLover

import unittest



class BookLoverTestSuite(unittest.TestCase):

    

    def test_1_add_book(self): 

        # add a book and test if it is in `book_list`.

        

        book1 = BookLover("Elysa", "whatever@gmail", "Slice of life")

        book_name = "Catch-22"

        book1.add_book(book_name, 2)

        

        self.assertTrue(book_name in book1.book_list.book_name.to_list())

        



    def test_2_add_book(self):

        # add the same book twice. Test if it's in `book_list` only once.

        

        book1 = BookLover("Elysa", "whatever@gmail", "Slice of life")

        book1.add_book("Catch-22", 2)

        expected = len(book1.book_list)

        book1.add_book("Catch-22", 2)

        actual = len(book1.book_list)

        

        self.assertEqual(expected, actual)

        

        

    def test_3_has_read(self): 

        # pass a book in the list and test if the answer is `True`.

        

        book1 = BookLover("Elysa", "whatever@gmail", "Slice of life")

        book1.add_book("Catch-22", 2)

        

        self.assertTrue(book1.has_read("Catch-22"))

        

        

    def test_4_has_read(self): 

        # pass a book NOT in the list and use `assert False` to test the answer is `True`

        

        book1 = BookLover("Elysa", "whatever@gmail", "Slice of life")

        book1.add_book("Catch-22", 2)

        

        self.assertFalse(book1.has_read("Hitch-hikers Guide to the Galaxy"))

        

        

    def test_5_num_books_read(self): 

        # add some books to the list, and test num_books matches expected.

        

        book1 = BookLover("Elysa", "whatever@gmail", "Slice of life")

        book1.add_book("Pride and Prejudice", 4)

        book1.add_book("Anna Karenina", 5)

        book1.add_book("Theb tale of despereaux", 4)

        book1.add_book("The Hobbit", 5)

        expected = 4

        actual = book1.num_books_read()

        

        self.assertEqual(expected, actual)

        

        

    def test_6_fav_books(self):

        # add some books with ratings to the list, making sure some of them have rating > 3. 

        # Your test should check that the returned books have rating  > 3

        

        book1 = BookLover("Elysa", "whatever@gmail", "Slice of life")

        book1.add_book("Pride and Prejudice", 4)

        book1.add_book("Grapes of Wrath", 1)

        book1.add_book("Things Fall Apart", 2)

        book1.add_book("Anna Karenina", 5)

        good_rating= book1.fav_books()

        

        self.assertTrue(good_rating['book_rating'].all())

                

if __name__ == '__main__':

    

    unittest.main(verbosity=3)
