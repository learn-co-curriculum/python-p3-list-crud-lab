from list_crud import (
    create_an_empty_list, create_a_list,
    add_element_to_end_of_list, add_element_to_start_of_list,
    remove_element_from_end_of_list, remove_element_from_start_of_list,
    retrieve_first_element_from_list, retrieve_element_from_index,
    retrieve_last_element_from_list
)

class TestListCrud:
    '''Module list_crud.py'''

    def test_creates_an_empty_list(self):
        '''contains a function "create_an_empty_list()" that creates and returns an empty list.'''
        assert(create_an_empty_list() == [])

    def test_creates_a_list_len_4(self):
        '''contains a function "create_a_list()" that creates and returns a list of length 4.'''
        assert(type(create_a_list()) == list)
        assert(len(create_a_list()) == 4)

    def test_adds_element_to_end_of_list(self):
        '''contains a function "add_element_to_end_of_list" that adds an element to the end of a list.'''
        assert(type(add_element_to_end_of_list(create_a_list(), 5)) == list)
        assert(add_element_to_end_of_list([1, 2, 3, 4], 5)[-1] == 5)

    def test_adds_element_to_start_of_list(self):
        '''contains a function "add_element_to_start_of_list" that adds an element to the start of a list.'''
        assert(type(add_element_to_start_of_list(create_a_list(), 0)) == list)
        assert(add_element_to_start_of_list([1, 2, 3, 4], 0)[0] == 0)

    def test_removes_element_from_end_of_list(self):
        '''contains a function "remove_element_from_end_of_list()" that removes an element from the end of a list.'''
        assert(type(remove_element_from_end_of_list(create_a_list())) == list)
        assert(len(remove_element_from_end_of_list(create_a_list())) == 3)
        assert(remove_element_from_end_of_list([1, 2, 3, 4])[-1] == 3)

    def test_removes_element_from_start_of_list(self):
        '''contains a function "remove_element_from_start_of_list()" that removes an element from the start of a list.'''
        assert(type(remove_element_from_start_of_list(create_a_list())) == list)
        assert(len(remove_element_from_start_of_list(create_a_list())) == 3)
        assert(remove_element_from_start_of_list([1, 2, 3, 4])[0] == 2)

    def test_retrieves_first_element_from_list(self):
        '''contains a function "retrieve_first_element_from_list()" that retrieves the first element from a list.'''
        assert(retrieve_first_element_from_list([1, 2, 3, 4]) == 1)

    def test_retrieves_element_from_index(self):
        '''contains a function "retrieve_element_from_index()" that takes a list and an index as arguments and returns the list's element at that index.'''
        assert(retrieve_element_from_index([1, 2, 3, 4], 1) == 2)
    
    def test_retrieves_last_element_from_list(self):
        '''contains a function "retrieve_last_element_from_list()" that retrieves the last element from a list.'''
        assert(retrieve_last_element_from_list([1, 2, 3, 4]) == 4)
