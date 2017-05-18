What is it
==========

Proof of concept for importing python modules from IPFS.

Requirements
------------

IPFS API available at `localhost:5001`.

Example
-------

Create python file (`lib.py`):

    value = 42

Add it to IPFS:

    ipfs add lib.py -q

This will output hash. Something like `QmTuqjiwi86wbQzJt6zr5q8BkfZRKWbhcKCtzA8q3mFZVk`.

Create python file that uses created module (`main.py`):

    from QmTuqjiwi86wbQzJt6zr5q8BkfZRKWbhcKCtzA8q3mFZVk import value
    import QmTuqjiwi86wbQzJt6zr5q8BkfZRKWbhcKCtzA8q3mFZVk as mod
    print(value, mod.value)

Run it:

    python ipfs_loader.py main.py

Tests
-----

Just run `./test.sh`.
