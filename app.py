from ocr import ocr_space_file
import json

test_file = ocr_space_file(filename='example_image.png', language='pol')
json_obj = json.loads(test_file)
#print (json_obj["ParsedResults"][0]["TextOverlay"]["Lines"])
s = ""
for key in json_obj["ParsedResults"][0]["TextOverlay"]["Lines"]:
    s += key["Words"][0]["WordText"]
print (s)
#test_url = ocr_space_url(url='http://i.imgur.com/31d5L5y.jpg')
