'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


			
	def test_is_student_removed(self): #tests to make sure removed student is not in list
		test_class = ClassList(2)
		test_class.add_student('Test Student')
		test_class.remove_student('Test Student')
		test.assertNotIn('Test Student', test_class.class_list)

		
	def test_for_error_when_student_removal_doesnt_exist(self): #tests to make sure student exists when removing
		test_class = ClassList(2)
		test_class.remove_student('Student1')
		test_class.remove_student('Test Student')
		with self.assertRaises(StudentError):
			test_class.remove_student('Test Student')


	def test_for_error_when_removing_empty_list #tests to make sure you can't remove things from empty lists
		test_class = ClassList(2)
		test_class.remove_student('Test Student')
			with self.assertRaises(StudentError):
				test_class.remove_student('Test Student')



    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


		
	def test_adds_examples(self): #verifies student that don't exist aren't enrolled and throw errors
		test_Class = ClassList(2)
		test_class.add_student('Student1')
		test_class.add_student('Student2')
		
		with self.assertRaises(StudentError):
			self.assertFalse(test_class.is_enrolled('Student3'))

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


    ## However, it would be useful to check that index_of_student returns None if a student isn't present.
	
	def test_none_when_empty #tests to return none when list is empty
		test_class = ClassList(2)
		with self.assertRaise(StudentError):	
			self.assertIsNone(test_class.index_of_student('Student1')
			
	def test_none_when_student_not_present #tests to return none when student is not present
		test_class = ClassList(2)
		test_class.add_student('Studnet 2')
		with self.assertRaise(StudentError):	
			self.assertIsNone(test_class.index_of_student('Student1')
    

	def test_is_class_full #tests if class is full
		test_class = ClassList(2)
		with self.assertRaise(StudentError):
			self.assertTrue(test_class.is_class_full)
			
	def test_is_class_full #tests if class is not full
		test_class = ClassList(2)
		with self.assertRaise(StudentError):
			self.assertFalse(test_class.is_class_full)
   