#!/bin/bash
find test -name test.py | xargs -n1 python ipfs_loader.py
