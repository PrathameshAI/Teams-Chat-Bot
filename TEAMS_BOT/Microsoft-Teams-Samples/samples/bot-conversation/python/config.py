#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "6e04b2fa-c0ad-4764-a116-b7ece0acfb3b")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "20ce8c44-76b1-44be-abf9-239d47a84939")
