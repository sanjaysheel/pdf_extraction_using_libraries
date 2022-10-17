from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter, XMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO


def convert_pdf_to_html(path):
    rsrcmgr = PDFResourceManager()
    # if you opening as 'r' then use retstr = StringIO()
    # retstr = StringIO()

    # if you are opening the pdf as 'rb' then use retstr = BytesIO()
    retstr = BytesIO()
    # codec = 'utf-8'
    laparams = LAParams()
    # device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # device = XMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    device = HTMLConverter(rsrcmgr, retstr,pageno=1, fontscale=1.004, showpageno=False, laparams=laparams,
     layoutmode = 'exact', 
     rect_colors={ #'char': 'green',
        'figure': 'yellow',
        'textline': 'magenta',
        'textbox': 'cyan',
        'textgroup': 'red',
        'curve': 'black',
        'page': 'gray',}, text_colors={'char': 'black'})




    #  rb for BytesIO and b for StringIO
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0 #is for all
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    # when we are using password as a perameter
    # text = retstr.getvalue().decode()
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

test = convert_pdf_to_html('2009.02252.pdf')
# print(test)
Func = open("pdf_to_html.html","wb")
   
# Adding input data to the HTML file
Func.write(test)
              
# Saving the data into the HTML file
Func.close()







# # from pdfminer.high_level import extract_pages
# # for page_layout in extract_pages("2203.15177v3.pdf"):
# #     for element in page_layout:
# #             print(element)

# # from pdfminer.high_level import extract_text
# # text = extract_text('2203.15177v3.pdf')
# # print(text)



# from io import StringIO
# from pdfminer.high_level import extract_text_to_fp
# from pdfminer.layout import LAParams
# output_string = StringIO()
# with open('2203.15177v3.pdf', 'rb') as fin:
#     extract_text_to_fp(fin, output_string, laparams=LAParams(),output_type='html', codec=None)