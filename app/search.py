from flask import current_app

def add_to_index(index,model):
	if not current_app.elasticsearch:
		return
	pyaload={}
	for field in model.__searchable__:
		pyaload[field] = getattr(model,field)
	current_app.elasticsearch.index(index=index,id=model.id,body=pyaload)

def remove_from_index(index,model):
	if not current_app.elasticsearch:
		return
	current_app.elasticsearch.delete(index=index,id=model.id)


def query_index(index, query, page, per_page):

    if not current_app.elasticsearch:
        return [], 0

    ids= []
    search = current_app.elasticsearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
              'from': (page - 1) * per_page, 'size': per_page})
    
    for hit in search['hits']['hits']:
    	x = 0
    	print(hit['_id'])
    	x = int(hit['_id'])
    	ids.append(x)
    total = int(search['hits']['total'])
    return ids, total