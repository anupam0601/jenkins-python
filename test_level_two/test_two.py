#!/usr/bin/env python

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from automation_test.json_logger import Logger
log = Logger(file_id="test_two")


log.info("testing current module")