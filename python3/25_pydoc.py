# !bin/bash
# Daniel OUATTARA
# 24 06 2024


"""
MetaDocumentation: A documentation for the documentation tool
------------------------------------------------------------

# 1
---

pydoc <name> ...
    Show text documentation on something.  <name> may be the name of a
    Python keyword, topic, function, module, or package, or a dotted
    reference to a class or function within a module or module in a
    package.  If <name> contains a '/', it is used as the path to a
    Python source file to document. If name is 'keywords', 'topics',
    or 'modules', a listing of these things is displayed.

python3 -m pydoc
python3 -m pydoc math
python3 -m pydoc tuple

python3 -m pydoc pow

is equivalent to: 

python3
>>> help(pow)

# 2
---

pydoc -k <keyword>
    Search for a keyword in the synopsis lines of all available modules.
    
python3 -m pydoc -k <keyword>
python3 -m pydoc -k ftp
python3 -m pydoc -k async
python3 -m pydoc -k sql

# 3
---

pydoc -p <port>
    Start an HTTP server on the given port on the local machine.  Port
    number 0 can be used to get an arbitrary unused port.

python3 -m pydoc -p <port>
python3 -m pydoc -p 3000

# 4
---

pydoc -b
    Start an HTTP server on an arbitrary unused port and open a web browser
    to interactively browse documentation.  This option can be used in
    combination with -n and/or -p.
    
python3 -m pydoc -b <port>
python3 -m pydoc -b 3000

# 5
---

pydoc -w <name> ...
    Write out the HTML documentation for a module to a file in the current
    directory.  If <name> contains a '/', it is treated as a filename; if
    it names a directory, documentation is written for all the contents.


python3 -m pydoc -m <name>
python3 -m pydoc -b 3000

-------------------------------

pydoc -n <hostname>
    Start an HTTP server with the given hostname (default: localhost).

"""
