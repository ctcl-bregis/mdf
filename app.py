# MDF - CTCL 2024-2025
# File: /home/ctcl/Documents/mdf/app.py
# Purpose: Main application file
# Created: June 20, 2025
# Modified: June 20, 2025

import discord
import logging
import os
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)


if not os.path.exists("./config.json"):
    logger.info("config.json does not exist in current directory, creating config.json")
    default = """
{
    "token": "",
    "modules": [
        "base"
    ]
}
"""
    with open("config.json", "w") as f:
        f.write(default)

    
with open("config.json", "r") as f:
    config = json.loads(f.read())
    

for module in config["modules"]:
    try:
        __import__("modules." + module)
    except ImportError:
        logger.error("Module " + module + " does not exist")
        continue
    except Exception as e:
        logger.error("Error importing module " + module + ": " + str(e))
        continue