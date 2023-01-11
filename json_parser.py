import json
def parse_to_json(object):
    with open('./json_data/data.json', 'w') as outfile:
        json.dump(object, outfile, indent=4, sort_keys=True)

def get_content_from_json(id):
    with open('./json_data/data.json','r', encoding='UTF-8') as f:
        data = json.load(f)
    
    for post in data:
        if post['id'] == id:
            return post['content']