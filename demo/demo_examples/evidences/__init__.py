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

from compliance.config import get_config
from compliance.evidence import DAY, ReportEvidence, RawEvidence

get_config().add_evidences(
    [
        RawEvidence(
            'iso_clock_utc.txt',
            'time',
            DAY,
            'Coordinated Universal Time'
        ),
        RawEvidence(
            'auditree_logo',
            'hashes',
            DAY,
            'The Auditree logo image SHA512 hex digest',
            binary_content=False
        ),
        ReportEvidence(
            'iso_clock_utc.md',
            'time',
            DAY,
            'World Clock Analysis report.'
        ),
        ReportEvidence(
            'image_hash_digest.md',
            'hashes',
            DAY,
            'Image Hash Digest Analysis report.'
        )
    ]
)
