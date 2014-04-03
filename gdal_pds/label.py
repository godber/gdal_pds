"""
Implements the PDS Object Description Language as outlined here:

    http://pds.jpl.nasa.gov/documents/sr/Chapter12.pdf

TODO: This is still a work in progress.
"""

from collections import OrderedDict


class ParseError(Exception):
    pass


def set_value(label, key, value, in_block):
    value = str(value).strip("\'\"")
    if in_block:
        label[in_block][key] = value
    else:
        label[key] = value


def read(file_path):
    """
    Parses a PDS Label from a file, returns an ordered dict
    """

    # Characters that can open a multiline value mapped to the closing
    # characters
    MULTILINE_DICT = {'"': '"', '(': ')', '{': '}'}

    label = OrderedDict()
    in_block = None
    wrapped = False  # False or key
    multiline = False
    multiline_end = None
    #multiline_prefixes = re.compile('^["(]')
    with open(file_path) as f:
        for lineno, line in enumerate(f):
            # strip off the ^M and any trailing garbage
            line = line.rstrip()

            # the label ends with END, stop here or you're parsing binary
            # or other embedded headers
            if line.strip() == 'END':
                break

            if '=' in line:
                # Lines with = in them are essentially key value pairs
                # anything else is a wrapped line, comment, empty line or
                # continued value
                key, value = line.split('=')
                key = key.strip()
                value = value.strip()

                # Since there is an = there should be a value, if there is not
                # assume the line is wrapped.  These differ from  multiline
                # values because the value is on a single line following the
                # line which contains the key.
                #
                # Example:
                #  TELEMETRY_SOURCE_NAME            =
                #                               "025_001_p1212-009-0001_003_0345867992-031.dat"
                if value == '':
                    wrapped = key
                elif value[0] in MULTILINE_DICT.keys():
                    # Values beginning with " or ( can be multiline values, we
                    # save the key and which prefix is used
                    multiline = key
                    # make sure there's no whitespace on the first char
                    multiline_end = MULTILINE_DICT[value[0]]
                    if value.endswith(multiline_end):
                        # all on this line
                        multiline = False
                    else:
                        pass
                        #print key, multiline_end, value

                # Handle OBJECT and GROUP blocks, as well as finally setting
                # the key/value in the label
                if key in ['OBJECT', 'GROUP']:
                    in_block = value
                    label[value] = OrderedDict([('_type', key)])
                elif key in ['END_OBJECT', 'END_GROUP']:
                    in_block = None
                else:
                    set_value(label, key, value, in_block)
            else:
                # No = in line
                if wrapped:
                    key = wrapped
                    # strip off leading spaces (and trailing)
                    value = line.strip()
                    wrapped = False
                elif multiline:
                    key = multiline

                    # clean up line, remove any whitespace on the right
                    line = line.rstrip()
                    # strip the leading 37 spaces, conditional may be
                    # uneccessary
                    if line.startswith(' ' * 37):
                        line = line[37:]

                    if in_block:
                        value = label[in_block][key] + line
                    else:
                        value = label[key] + line

                    if value.endswith(multiline_end):
                        multiline = False
                elif line == '':
                    # empty lines are preserved with a special key value
                    # '_emptyline'
                    key = '_emptyline'
                    value = True
                elif line.startswith('/*'):
                    # comments are preserved with a special key value
                    # '_comment'
                    key = '_comment'
                    value = line
                else:
                    raise ParseError(
                        'Unhandled condition in label on line %s:\n%s' %
                        (str(lineno + 1), line)
                    )

                set_value(label, key, value, in_block)

    return label
