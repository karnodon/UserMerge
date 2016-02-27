from merge import Merger

__author__ = 'Frostbite'
import unittest


# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#

class TestMerge(unittest.TestCase):
    def setUp(self):
        self.m = Merger()

    def test_line_parse(self):
        self.m.parse_line('test=test_role')
        self.assertEquals(1, len(self.m.users))
        self.assertEquals('test_role', self.m.users['test'][0])
        self.assertFalse(self.m.parse_line('test'))
        self.assertEquals(1, len(self.m.users))
        self.m.parse_line('test=test_role_2')
        self.assertEquals(1, len(self.m.users))
        self.assertEquals(2, len(self.m.users['test']))
        self.assertEquals('test_role_2', self.m.users['test'][1])

    def test_convert_roles(self):
        roles = self.m.convert_roles(['beznal_role', 'beznal_role_2', 'beznal_role_3'], 'beznal_')
        self.assertEquals('role,role_2,role_3', roles)

    def test_store_errors(self):
        self.m.store_error('38.txt', 'test')
        self.m.store_error('38.txt', 'testxxx')
        self.m.store_error('38.txt', 'test111')
        self.m.store_error('40.txt', 'test40')
        self.assertEquals(2, len(self.m.errors))

