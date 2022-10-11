from docx import Document
import re

file = 'DesignDoc_A3 - Copy.docx'
document = Document(file)
heading1_tracker = 1
heading2_tracker = 1
heading3_tracker = 1

for headings in document.paragraphs:
    if headings.style.name == 'Heading 1':
        heading = re.split(r'\s', headings.text)
        headings.text = str(heading1_tracker) + '. ' + str(' '.join(heading[1:]))
        heading1_tracker += 1
        heading2_tracker = 1
        heading3_tracker = 1
        print(headings.text)
    elif headings.style.name == 'Heading 2':
        heading = re.split(r'\s', headings.text)
        headings.text = str(heading1_tracker - 1) + '.' + str(heading2_tracker) + '. ' + str(' '.join(heading[1:]))
        print(headings.text)
        heading2_tracker += 1
        heading3_tracker = 1

    elif headings.style.name == 'Heading 3':
        heading = re.split(r'\s', headings.text)
        headings.text = str(heading1_tracker - 1) + '.' + str(heading2_tracker - 1) + '.' + str(heading3_tracker) + '. ' + str(' '.join(heading[1:]))
        print(headings.text)
        heading3_tracker += 1
        

document.save(file)