#!/usr/bin/env python3

import samsungctl
import time

config = {
    "name": "samsungctl",
    "description": "PC",
    "id": "",
    "host": "192.168.1.102",
    "port": 8001,
    "method": "websocket",
    "timeout": 0,
}

with samsungctl.Remote(config) as remote:
        remote.control("KEY_UP")