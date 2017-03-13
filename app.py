import openpyxl


##wb = openpyxl.load_workbook('example.xlsx')
##sheet = wb.get_sheet_by_name('Sheet1')
##print (sheet['A2'].value)
##
##print (sheet.cell(row=2, column=1).value)
##sheet['B2'] = 'B'
##print (sheet.cell(row=2, column=2).value)
##if sheet.cell(row=2, column=1).value == sheet.cell(row=2, column=2).value:
##    sheet['C2'] = 'Pass'
##else:
##    sheet['C2'] = 'Fail'
##wb.save('example.xlsx');


import requests
import json

def ocr_space_file(filename, overlay=True, api_key='159d75203088957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='159d75203088957', language='eng'):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()


# Use examples:
test_file = ocr_space_file(filename='example_image.png', language='pol')
json_obj = json.loads(test_file)
#print (json_obj["ParsedResults"][0]["TextOverlay"]["Lines"])
s = ""
for key in json_obj["ParsedResults"][0]["TextOverlay"]["Lines"]:
    s += key["Words"][0]["WordText"]
print (s)
#test_url = ocr_space_url(url='http://i.imgur.com/31d5L5y.jpg')
