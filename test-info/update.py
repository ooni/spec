import os
import codecs

from glob import glob

import markdown

for test_filename in glob("../test-specs/*"):
    input_file = codecs.open(test_filename, mode="r", encoding="utf-8")
    text = input_file.read()
    info_html = """
<html>
<head>
    <link rel="stylesheet" href="css/pure-min.css">
    <link rel="stylesheet" href="css/main.css">
</head>
<div class="content">
"""
    info_text = ""
    begin_desc = False
    inside_name = False
    for line in text.split("\n"):
        if line.startswith("# Specification name"):
            inside_name = True
            continue
        elif line.startswith("# Test description"):
            begin_desc = True
        elif begin_desc is False and inside_name is False:
            continue

        if inside_name is True:
            if line.startswith("#"):
                inside_name = False
            else:
                info_html += "<h1>" + line + "</h1>\n"

        if begin_desc:
            info_text += line + "\n"

    html = markdown.markdown(info_text,
                             extensions=["markdown.extensions.fenced_code",
                                         "markdown.extensions.nl2br"])
    info_html += html + "</div></html>"
    input_file.close()
    output_filename = os.path.basename(test_filename)
    output_filename = output_filename.replace(".md", ".html")
    with open(output_filename, "w+") as fw:
        fw.write(info_html)
