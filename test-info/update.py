import os
import codecs

from glob import glob

import markdown

for test_filename in glob("../test-specs/*"):
    input_file = codecs.open(test_filename, mode="r", encoding="utf-8")
    text = input_file.read()
    info_text = ""
    begin = False
    for line in text.split("\n"):
        if begin is False and \
                not line.startswith("# Test description"):
            continue
        else:
            begin = True
            info_text += line + "\n"

    html = markdown.markdown(info_text)
    input_file.close()
    output_filename = os.path.basename(test_filename)
    output_filename = output_filename.replace(".md", ".html")
    with open(output_filename, "w+") as fw:
        fw.write(html)
