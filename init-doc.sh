#!/bin/sh

mv doc_template.cfg doc.cfg
mv gulpfile_template.js gulpfile.js
mv httpd_template.py httpd.py

cd docs
mv conf_template.py conf.py
mv index_template.rst index.rst
mv content_types_template.rst content_types.rst

