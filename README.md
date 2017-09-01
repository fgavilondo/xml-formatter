# xml-formatter

A Python script to reformat one or multiple XML files in one go (*.xml, *.xsd, *.wsdl etc.)

Usage:

    python xmlformatter.py file-or-directory-name indentation [extensions]

The first parameter is the name of a file or a directory that you want to reformat.
If it is a file, then the xml contents of the file are formatted and the file is updated in place.
If it is a directory, then all the files in that directory with the specified extensions will be reformatted.

The parameter "indentation" indicates the number of spaces for each indentation level.

The optional parameter "extensions" is the comma separated list of XML file extensions that you want to use when reformatting directories. Default is "xml".

Examples:

   python xmlformatter.py myfile.xml 2
   python xmlformatter.py myfile.xml 4
   python xmlformatter.py /tmp/somedir 4
   python xmlformatter.py /tmp/somedir 4 wsdl
   python xmlformatter.py /tmp/somedir 4 xml,xsd,wsdl
