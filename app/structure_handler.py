from flask import request, jsonify
from . import app
from .utils import get_page_data, count_tags, validate_url

DEFAULT_LINK = 'http://freestylo.ru/'


@app.get('/structure')
async def get_structure():
    link = request.args.get('link')
    if not link:
        link = DEFAULT_LINK
    tags = request.args.get('tags', [])
    if len(tags) > 0:
        tags = tags.split(',')

    validated_link = validate_url(link)
    data = await get_page_data(validated_link)
    tags_counter = count_tags(data, tags)
    return jsonify(tags_counter)


@app.post('/check_structure')
async def post_structure():
    link = request.json.get('link')
    structure = request.json.get('structure')

    validated_link = validate_url(link)
    data = await get_page_data(validated_link)
    tags_counter = count_tags(data)

    if structure == tags_counter:
        return jsonify({'is_correct': True})
    diff = set(structure.items()) - set(tags_counter.items())
    return jsonify({'is_correct': False, 'difference': dict(diff)})
