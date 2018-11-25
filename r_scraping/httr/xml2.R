# Node Modification

## Modifying Existing XML
### Text Modification

if(!require(xml2)) install.packages("xml2")

# read_xml()
# xml_text()
# xml_find_all()
# xml_structrue()

x = read_xml("<p>This is some <b>text</b>. This is more.</p>")
xml_text(x)

xml_text(x) = "This is some other text."
xml_text(x)

x = read_xml("<p>This is some text. This is <b>bold!</b></p>")
text_only = xml_find_all(x, "//text()")
xml_text(text_only)

xml_text(text_only) = c("This is some other text. ", "Still bold!")
xml_structure(x)
xml_text(text_only)











