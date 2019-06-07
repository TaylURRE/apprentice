import unittest
from milestone1.module_1 import cap_name, cap_many_names


class TestModuleOne(unittest.TestCase):
    """
        Unit test for captializing one name
        Unit test for capitalizing many names
    """
    def test_cap_name(self):
        self.assertEqual(cap_name('harRy'), 'Harry')
        self.assertEqual(cap_name('harRy Potter'), 'Harry potter')
        self.assertEqual(cap_name('harRy4'), 'Harry4')
        self.assertEqual(cap_name('hArRy!'), 'Harry!')
        self.assertEqual(cap_name(['dumbolore']), (['dumbolore'],
                                                   'Invalid input; please enter a string.'))
        self.assertEqual(cap_name({'ron'}), ({'ron'},
                                             'Invalid input; please enter a string.'))
        self.assertEqual(cap_name(('darby')), 'Darby')

    def test_cap_many_names(self):
        self.assertEqual(cap_many_names('harRy Potter'), 'Harry Potter')
        self.assertEqual(cap_many_names('harRy Potte*&r'), 'Harry Potte*&r')
        self.assertEqual(cap_many_names('HArRy P234ott9432er'),
                         'Harry P234ott9432er')
        self.assertEqual(cap_many_names(['taylor dennis']), (['taylor dennis'],
                         "Invalid, format name using string ie 'taylor dennis' "))
        self.assertEqual(cap_many_names({'taylor dennis'}), ({'taylor dennis'},
                         "Invalid, format name using string ie 'taylor dennis' "))
        self.assertEqual(cap_many_names(('taylor dennis')), "Taylor Dennis")
        self.assertEqual(cap_many_names(('taylor' 'dennis')), "Taylordennis")
        self.assertEqual(cap_many_names(('taylor' + 'dennis')), "Taylordennis")
        self.assertEqual(cap_many_names(('taylor', 'dennis')), (('taylor', 'dennis'),
                         "Invalid, format name using string ie 'taylor dennis' "))
        self.assertEqual(cap_many_names('839485'), '839485')


if __name__ == '__main__':
    unittest.main()
