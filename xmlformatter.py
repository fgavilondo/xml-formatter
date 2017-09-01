#! /usr/bin/env python
from __future__ import print_function

import glob
import os
import sys
from xml.dom import minidom


def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)


def read_xml_from_file(path):
    with open(path, 'r') as f:
        content = f.read()
    return minidom.parseString(content)


def xml_to_pretty_string(xml, indentation):
    return xml.toprettyxml(indent=' ' * indentation)


def reformat_xml_file(path, indentation):
    print('Reformatting', path)
    xml_doc = read_xml_from_file(path)
    write_file(path, xml_to_pretty_string(xml_doc, indentation))


def filter_xml_files(directory, extensions):
    paths = []
    for extension in extensions:
        paths += glob.glob(directory + '/*.' + extension)
    return paths


def process(file_or_directory, indentation, extensions):
    if os.path.isfile(file_or_directory):
        reformat_xml_file(file_or_directory, indentation)
    elif os.path.isdir(file_or_directory):
        xml_files = filter_xml_files(file_or_directory, extensions)
        if not xml_files:
            print('No files found matching extensions', extensions)
        for path in xml_files:
            reformat_xml_file(path, indentation)
    else:
        print(file_or_directory, 'is neither a file nor a directory!')


def usage():
    print()
    print('Usage:')
    print()
    print('    python xmlformatter.py file-or-directory-name indentation [extensions]')
    print()
    print('The first parameter is the name of a file or a directory that you want to reformat.')
    print('If it is a file, then the xml contents of the file are formatted and the file is updated in place.')
    print(
        'If it is a directory, then all the files in that directory with the specified extensions will be reformatted.')
    print('The parameter "indentation" indicates the number of spaces for each indentation level.')
    print('The optional parameter "extensions" is a comma separated list of file extensions'
          ' that you want to use when reformatting directories. Default is "xml".')
    print()
    print('Examples:')
    print('   python xmlformatter.py myfile.xml 2')
    print('   python xmlformatter.py myfile.xml 4')
    print('   python xmlformatter.py /tmp/mydirectory 4')
    print('   python xmlformatter.py /tmp/mydirectory 4 wsdl')
    print('   python xmlformatter.py /tmp/mydirectory 4 xml,xsd,wsdl')
    print()


def main():
    try:
        file_or_directory = sys.argv[1]
    except IndexError:
        usage()
        exit()

    try:
        indentation = int(sys.argv[2])
    except Exception:
        usage()
        exit()

    try:
        comma_separated = sys.argv[3]
        extensions = comma_separated.split(',')
    except IndexError:
        extensions = ['xml']

    process(file_or_directory, indentation, extensions)


if __name__ == "__main__":
    main()
