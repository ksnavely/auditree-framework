# -*- mode:python; coding:utf-8 -*-
# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime

from compliance.check import ComplianceCheck
from compliance.evidence import with_raw_evidences

class ClockCheck(ComplianceCheck):
    """Perform analysis on world clock evidence."""

    @property
    def title(self):
        """
        Return the title of the checks.

        :returns: the title of the checks
        """
        return 'Clock'

    @with_raw_evidences('time/iso_clock_utc.txt')
    def test_day_of_year(self, evidence):
        """Check whether the day of the year is odd or even."""
        d = datetime.fromisoformat(evidence.content)
        if int(d.day) % 2 == 0:
            self.add_failures(
                'Even Day Violation', f'{d.day} in {evidence.content} is even!!'
            )
        else:
            self.add_warnings(
                'Even Day Approaching',
                f'{day} in {ordinal_dt} will be even soon!!'
            )

    @with_raw_evidences('time/iso_clock_utc.json')
    def test_day_of_week(self, evidence):
        """Check whether the day is Wednesday."""
        d = datetime.fromisoformat(evidence.content)
        day_of_week = d.strftime("%A")
        if day_of_week == 'Wednesday':
            self.add_failures('Wednesday Violation', f'It is Wednesday!!')

    def get_reports(self):
        """
        Provide the check report name.

        :returns: the report(s) generated for this check
        """
        return ['time/iso_clock_utc.md']

    def msg_day_of_year(self):
        """
        Day of year check notifier.

        :returns: notification dictionary.
        """
        return {'subtitle': 'Even Day Violation', 'body': None}

    def msg_day_of_week(self):
        """
        Day of week check notifier.

        :returns: notification dictionary.
        """
        return {'subtitle': 'Wednesday Violation', 'body': None}
