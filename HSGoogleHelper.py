from google.cloud import vision
from google.cloud.vision import types
import io

def get_text_from_google(path):
    print("### get_text_from_google")
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    for page in document.pages:
        for block in page.blocks:
            block_words = []
            for paragraph in block.paragraphs:
                block_words.extend(paragraph.words)

            block_symbols = []
            for word in block_words:
                block_symbols.extend(word.symbols)

            block_text = ''
            for symbol in block_symbols:
                block_text = block_text + symbol.text

    return document

#Methods related to Google API 


def collect_text_areas(document):
    print("### collect_text_areas")
    areas = []
    for page in document.pages:
        for block in page.blocks:
            block_words = []
            for paragraph in block.paragraphs:
                block_words.extend(paragraph.words)

            block_symbols = []
            for word in block_words:
                block_symbols.extend(word.symbols)

            block_text = ''
            for symbol in block_symbols:
                block_text = block_text + symbol.text

            area = {}
            area['text'] = block_text
            area['bounds'] = block.bounding_box
            areas.append(area)
    return areas

def count_text_areas_by_size(areas):
    low_threshold_len = 10
    high_threshold_len = 30
    
    count_low=0
    count_med=0
    count_high=0
    
    for area in areas:
        text = area['text']
        if len(text) < low_threshold_len:
            count_low+=1
        elif len(text) > high_threshold_len:
            count_high+=1
        else:
            count_med+=1
    return count_low, count_med, count_high
    
def count_text_areas_by_size(areas):
    low_threshold_len = 10
    high_threshold_len = 30
    
    count_low=0
    count_med=0
    count_high=0
    
    for area in areas:
        text = area['text']
        if len(text) < low_threshold_len:
            count_low+=1
        elif len(text) > high_threshold_len:
            count_high+=1
        else:
            count_med+=1
    return count_low, count_med, count_high