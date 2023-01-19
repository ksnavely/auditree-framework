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

import json

from compliance.check import ComplianceCheck
from compliance.evidence import evidences, with_raw_evidences

class ImageHashCheck(ComplianceCheck):
    """Perform analysis on image evidence."""

    @property
    def title(self):
        """
        Return the title of the checks.

        :returns: the title of the checks
        """
        return 'Auditree Image'

    @with_raw_evidences('hashes/auditree_logo')
    def test_image_hash_digest_with_decorator(self, evidence):
        """Check that the evidence content exists using decorator."""
        if not evidence.content:
            self.add_failures(
                'Using decorator', 'auditree_logo hash digest evidence is empty'
            )

    def test_image_hash_digest_with_ctx_mgr(self):
        """Check that the evidence content exists using context manager."""
        with evidences(self, 'raw/hashes/auditree_logo') as evidence:
            if not evidence.content:
                self.add_failures(
                    'Using context manager',
                    'auditree_logo hash digest evidence is empty'
                )

    def get_reports(self):
        """
        Provide the check report name.

        :returns: the report(s) generated for this check
        """
        return ['hashes/image_hash_digest.md']

    def msg_image_hash_digest_with_decorator(self):
        """
        Image exists using decorator check notifier.

        :returns: notification dictionary.
        """
        return {'body': None}

    def msg_image_hash_digest_with_ctx_mgr(self):
        """
        Image exists using context manager check notifier.

        :returns: notification dictionary.
        """
        return {'body': None}
