#!/Users/hardy/Dev/buildout.python/python-2.7/bin/python
# -*- coding: utf-8 -*-


import sys

filename = sys.argv[1] + '.rst'
title = sys.argv[2]

f = open(filename, "w")

l = len(unicode(title, 'utf-8'))

soulign = '\n' + ('=' * l) + '\n'

f.write('\n.. include:: links.rst')
f.write('\n' * 3)
f.write(soulign + title + soulign + '\n' * 4)

f.close()
