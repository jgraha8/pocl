#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2012 Pekka Jääskeläinen
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# Generate a static HTML from the given template.
#

import sys

try:
    from mako.template import Template
    from mako.lookup import TemplateLookup
except:
    print "Install Mako templates (e.g. easy_install \"Mako>=0.7.4\")"
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: generate_html.py source_template.mak destination.html"

    mylookup = TemplateLookup(directories=['.'])
    template = Template(filename=sys.argv[1], lookup=mylookup, strict_undefined=False)
    output = template.render()
    f = open(sys.argv[2], "w+")
    f.write(output)
    f.close()
