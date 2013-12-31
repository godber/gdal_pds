from collections import OrderedDict

class PDSImage(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.label = self.parse_label()

    def parse_label(self):
        """
        Parses a PDS Label from a file, returns an ordered dict
        """
        label = OrderedDict()
        in_block = None
        with open(self.filepath) as f:
            for line in f.readlines():
                line = line.rstrip()  # strip off the ^M and any trailing garbage
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
                        if in_block:
                            label[in_block][key] = value
                        else:
                            label[key] = value

                if line.strip() == 'END':
                    break

        return label

    def print_path():
        print self.filepath
