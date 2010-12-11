#-*- coding: utf-8 -*-



import unittest
from stalker.models import status



########################################################################
class TestStatus(unittest.TestCase):
    """testing the status class
    """
    
    
    
    ##----------------------------------------------------------------------
    #def test_name_str_or_unicode(self):
        #"""test the name attribute if it is str or unicode
        #"""
        
        ##----------------------------------------------------------------------
        ## the name should be a str or unicode
        #self.assertRaises(ValueError, status.Status, 1, '1')
        ## check the property
        #a_status = status.Status('Complete', 'Cmpl')
        #self.assertRaises(ValueError, setattr, a_status, 'name', 1)
        
    
    ##----------------------------------------------------------------------
    #def test_name_for_being_empty(self):
        #"""testing the name attribute if it is empty
        #"""
        ##----------------------------------------------------------------------
        ## the name could not be an empty string
        #self.assertRaises(ValueError, status.Status, '', 'Cmp')
        ## check the property
        #a_status = status.Status('Complete', 'Cmpl')
        #self.assertRaises(ValueError, setattr, a_status, 'name', '')
    
    
    
    ##----------------------------------------------------------------------
    #def test_name_first_letter_lowercase(self):
        #"""testing the name attributes first letter against being a lowercase
        #letter
        #"""
        
        ##----------------------------------------------------------------------
        ## the first letter of the name should be in upper case and the other
        ## letters should be in lower case
        #status_name = 'test'
        #a_status = status.Status(status_name, 'tst')
        #self.assertEqual(status_name.title(), a_status.name)
        
        ## check the property
        #a_status = status.Status('Complete', 'Cmpl')
        #a_status.name = status_name
        #self.assertEqual(status_name.title(), a_status.name)
    
    
    
    ##----------------------------------------------------------------------
    #def test_name_first_letter_integer(self):
        #"""testing the name attributes first letter against being an integer
        #value
        #"""
        ##----------------------------------------------------------------------
        ## the first letter of the name could not be an integer
        #status_name = '1test'
        #self.assertRaises(ValueError, status.Status, status_name, \
                           #status_name)
        
        ## check the property
        #a_status = status.Status('Complete', 'Cmpl')
        #self.assertRaises(ValueError, setattr, a_status, 'name', status_name)
    
    
    
    #----------------------------------------------------------------------
    def test_shortName_str_or_unicode(self):
        """testing the shortName attribute against not being a string or
        unicode
        """
        
        #----------------------------------------------------------------------
        # the shortName should be a str or unicode
        self.assertRaises(
            ValueError,
            status.Status,
            name='Complete',
            shortName=1
        )
        
        # check the property
        a_status = status.Status(name='Complete', shortName='Cmlt')
        self.assertRaises(
            ValueError,
            setattr,
            a_status,
            'shortName',
            1
        )
    
    
    
    #----------------------------------------------------------------------
    def test_shortName_empty_string(self):
        """testing the shortName attribute against being an empty string
        """
        
        #----------------------------------------------------------------------
        # the shortName can not be an empty string
        self.assertRaises(ValueError, status.Status, 'Complete', '')
        
        # check the property
        a_status = status.Status(name='Complete', shortName='Cmlt')
        self.assertRaises(ValueError, setattr, a_status, 'shortName', '')
        
        #----------------------------------------------------------------------
        # check if the shortName is get correctly
        name = 'Complete'
        abbr = 'Cmplt'
        a_status = status.Status(name=name, shortName=abbr)
        self.assertEquals( a_status.shortName, abbr)






########################################################################
class StatusListTest(unittest.TestCase):
    """testing the StatusList class
    """
    
    
    
    #----------------------------------------------------------------------
    def setUp(self):
        """let's create proper values for the tests
        """
        
        # proper values
        self.list_name = 'a_status_list'
        
        # should use Mocks in the list
        self.a_status_list = [
            status.Status(name='Not Available', shortName='N/A'),
            status.Status(name='Waiting To Start', shortName='WStrt'),
            status.Status(name='Started', shortName='Strt'),
            status.Status(name='Waiting For Approve', shortName='WAppr'),
            status.Status(name='Approved', shortName='Appr'),
            status.Status(name='Finished', shortName='Fnsh'),
            status.Status(name='On Hold', shortName='OH'),
            ]
    
    
    
    ##----------------------------------------------------------------------
    #def test_name_empty(self):
        #"""testing the name attribute against  being empty
        #"""
        
        ##----------------------------------------------------------------------
        ## the name couldn't be empty
        #self.assertRaises(ValueError, status.StatusList, '', self.a_status_list)
        
        ## test the name property
        #a_status_list_obj = status.StatusList(self.list_name, self.a_status_list)
        #self.assertRaises(ValueError, setattr, a_status_list_obj, 'name', '')
    
    
    
    ##----------------------------------------------------------------------
    #def test_name_for_str_or_unicode(self):
        #"""testing the name against not being a string or unicode
        #"""
        
        ##----------------------------------------------------------------------
        ## the name should be a string or unicode
        #self.assertRaises(ValueError, status.StatusList, 1, self.a_status_list)
        
        #a_status_list_obj = status.StatusList(self.list_name, self.a_status_list)
        #self.assertRaises(ValueError, setattr, a_status_list_obj, 'name', 1)
        #self.assertRaises(ValueError, setattr, a_status_list_obj, 'name', [])
        #self.assertRaises(ValueError, setattr, a_status_list_obj, 'name', {})
    
    
    
    ##----------------------------------------------------------------------
    #def test_name_property(self):
        #"""testing the name attribute property
        #"""
        
        ##----------------------------------------------------------------------
        ## it should be property
        #new_list_name = 'new status list name'
        
        ## check if we can properly assign new values to name property
        #a_status_list_obj = status.StatusList(self.list_name, self.a_status_list)
        #a_status_list_obj.name = new_list_name
        #self.assertEquals(a_status_list_obj.name, new_list_name)
    
    
    
    #----------------------------------------------------------------------
    def test_status_list_accepting_statuses(self):
        """testing the statuses list attribute
        """
        
        # the statuses attribute should be a list of statuses
        # can be empty?
        #
        
        #----------------------------------------------------------------------
        # it should only accept lists of statuses
        self.assertRaises(
            ValueError,
            status.StatusList,
            name=self.list_name,
            statuses='a str'
        )
        
        self.assertRaises(
            ValueError,
            status.StatusList,
            name=self.list_name,
            statuses={}
        )
        
        self.assertRaises(
            ValueError,
            status.StatusList,
            name=self.list_name,
            statuses=1
        )
    
    
    
    #----------------------------------------------------------------------
    def test_status_list_property_accepting_only_statuses(self):
        """testing the status_list attribute as a property and accepting
        Status objects only
        """
        new_status_list = status.StatusList(
            name=self.list_name,
            statuses=self.a_status_list
        )
        
        # check the property
        self.assertRaises(ValueError,
                          setattr,new_status_list, 'statuses', '1')
        
        self.assertRaises(ValueError,
                          setattr, new_status_list, 'statuses', ['1'])
        
        self.assertRaises(ValueError,
                          setattr, new_status_list, 'statuses', 1)
        
        self.assertRaises(ValueError,
                          setattr, new_status_list, 'statuses', [1, 'w'])
    
    
    
    #----------------------------------------------------------------------
    def test_status_list_being_empty(self):
        """testing status_list against being empty
        """
        
        #----------------------------------------------------------------------
        # the list couldn't be empty
        self.assertRaises(
            ValueError,
            status.StatusList,
            name=self.list_name,
            statuses=[]
        )
    
    
    
    #----------------------------------------------------------------------
    def test_statusList_list_elements_being_status_objects(self):
        """testing status_list elements against not being derived from Status
        class
        """
        
        #----------------------------------------------------------------------
        # every element should be an object derived from Status
        a_fake_status_list = [1, 2, 'a string', u'a unicode', 4.5]
        
        self.assertRaises(
            ValueError,
            status.StatusList,
            name=self.list_name,
            statuses=a_fake_status_list
        )
    
    
    
    #----------------------------------------------------------------------
    def test_statusList_property(self):
        """testing status_list as being property
        """
        
        #----------------------------------------------------------------------
        # it should be a property so check if it sets property correctly
        a_status_list_obj = status.StatusList(
            name=self.list_name,
            statuses=self.a_status_list
        )
        
        new_list_of_statutes = [
            status.Status(name='New Status', shortName='nsts')
        ]
        
        a_status_list_obj.statuses = new_list_of_statutes
        self.assertEquals( a_status_list_obj.statuses, new_list_of_statutes)
        
        