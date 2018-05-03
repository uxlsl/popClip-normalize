#!/bin/bash

export PATH=$PATH:/usr/local/bin
echo "$POPCLIP_TEXT" | ./normalize.py 2>/tmp/debug.txt
