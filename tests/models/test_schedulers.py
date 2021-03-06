# -*- coding: utf-8 -*-
# Stalker a Production Asset Management System
# Copyright (C) 2009-2017 Erkan Ozgur Yilmaz
#
# This file is part of Stalker.
#
# Stalker is free software: you can redistribute it and/or modify
# it under the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# Stalker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with Stalker.  If not, see <http://www.gnu.org/licenses/>

import unittest
import pytest
from stalker import SchedulerBase


class SchedulerBaseTester(unittest.TestCase):
    """tests the stalker.models.scheduler.SchedulerBase
    """

    def setUp(self):
        """set up the test
        """
        super(SchedulerBaseTester, self).setUp()

        from stalker import Studio
        self.test_studio = Studio(name='Test Studio')
        self.kwargs = {
            'studio': self.test_studio
        }
        self.test_scheduler_base = SchedulerBase(**self.kwargs)

    def test_studio_argument_is_skipped(self):
        """testing if the studio attribute will be None if the studio argument
        is skipped
        """
        self.kwargs.pop('studio')
        new_scheduler_base = SchedulerBase(**self.kwargs)
        assert new_scheduler_base.studio is None

    def test_studio_argument_is_None(self):
        """testing if the studio attribute will be None if the studio argument
        is None
        """
        self.kwargs['studio'] = None
        new_scheduler_base = SchedulerBase(**self.kwargs)
        assert new_scheduler_base.studio is None

    def test_studio_attribute_is_None(self):
        """testing if the studio argument can be set to None
        """
        self.test_scheduler_base.studio = None
        assert self.test_scheduler_base.studio is None

    def test_studio_argument_is_not_a_Studio_instance(self):
        """testing if a TypeError will be raised when the studio argument is
        not stalker.models.studio.Studio instance
        """
        self.kwargs['studio'] = 'not a studio instance'
        with pytest.raises(TypeError) as cm:
            SchedulerBase(**self.kwargs)

        assert str(cm.value) == \
            'SchedulerBase.studio should be an instance of ' \
            'stalker.models.studio.Studio, not str'

    def test_studio_attribute_is_not_a_Studio_instance(self):
        """testing if a TypeError will be raised when the studio attribute is
        set to a value which is not a stalker.models.studio.Studio instance
        """
        with pytest.raises(TypeError) as cm:
            self.test_scheduler_base.studio = 'not a studio instance'

        assert str(cm.value) == \
            'SchedulerBase.studio should be an instance of ' \
            'stalker.models.studio.Studio, not str'

    def test_studio_argument_is_working_properly(self):
        """testing if the studio argument value is correctly passed to the
        studio attribute
        """
        assert self.test_scheduler_base.studio == self.kwargs['studio']

    def test_studio_attribute_is_working_properly(self):
        """testing if the studio attribute is working properly
        """
        from stalker import Studio
        new_studio = Studio(name='Test Studio 2')
        self.test_scheduler_base.studio = new_studio
        assert self.test_scheduler_base.studio == new_studio

    def test_schedule_method_will_raise_not_implemented_error(self):
        """testing if the schedule() method will raise a NotImplementedError
        """
        base = SchedulerBase()
        with pytest.raises(NotImplementedError) as cm:
            base.schedule()

        assert str(cm.value) == ''
