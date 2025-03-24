from pathlib import Path
import lxml.etree as etree

#python >= 3.5
files = list(Path('.').rglob('*.cod'))

for file in files:
    tree = etree.parse(file)
    etree.strip_elements(tree, 'lastLoadedTimestamp')
    
    tree.write(file, encoding='utf-8', xml_declaration=True)
