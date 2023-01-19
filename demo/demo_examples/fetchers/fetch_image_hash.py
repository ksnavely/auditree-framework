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

import hashlib

from compliance.evidence import store_raw_evidence
from compliance.fetch import ComplianceFetcher

class ImageHashFetcher(ComplianceFetcher):
    """Fetch the Auditree logo image and store as evidence."""

    @store_raw_evidence('hashes/auditree_logo')
    def fetch_auditree_logo_hash(self):
        """Fetch the Auditree logo SHA512 hash digest."""
        img_bytes = open('at-logo.png', 'rb').read()
        m = hashlib.sha512()
        m.update(img_bytes)

        # We need to store evidence as a string, store the 
        # SHA512 hash digest of the file
        return m.hexdigest()
