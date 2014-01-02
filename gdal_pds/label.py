"""
Known Issues::

    [ ] Doesn't handle multiline values
"""

from collections import OrderedDict


def read(file_path):
    """
    Parses a PDS Label from a file, returns an ordered dict
    """
    label = OrderedDict()
    in_block = None
    with open(file_path) as f:
        for line in f.readlines():
            # strip off the ^M and any trailing garbage
            line = line.rstrip()
            if '=' in line:
                key, value = line.split('=')
                key = key.strip()
                value = value.strip()
                if key in ['OBJECT', 'GROUP']:
                    in_block = value
                    label[value] = OrderedDict([('_type', key)])
                elif key in ['END_OBJECT', 'END_GROUP']:
                    in_block = None
                else:
                    value = value.strip("\'\"")
                    if in_block:
                        label[in_block][key] = value
                    else:
                        label[key] = value

            if line.strip() == 'END':
                break

    return label
