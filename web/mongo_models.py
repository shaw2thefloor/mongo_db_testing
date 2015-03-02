from mongokit import Document, Connection
from bson import ObjectId


connection = Connection(host="127.0.0.1", port=27017)
db = 'MONGO_TEST_1'


# ObjectId objects are used in mongodb queries where the default id object is of this type
def to_mongo_id(id):
    return ObjectId(id)


# django templates take a list or dictionary object as their context, so mongodb cursor objects
# need to be converted before being used in templates
def to_django_context(cursor):
    records = []
    for r in cursor:
        records.append(r.to_json_type())
    return records


# simple representation of a mongodb document
@connection.register
class Author(Document):
    # allows additional fields to be added to the document on the fly
    use_schemaless = True
    # shortcut to the collection these documents are store in
    __collection__ = 'authors'
    # shortcut to the database name
    __database__ = db
    # allows use of dot.notation instead of dict['notation'] (doesn't seem to work for schemaless fields)
    use_dot_notation = True
    use_autorefs = True
    structure = {
        'firstname': basestring,
        'lastname': basestring,
        'genres': [basestring],
        'address': [
            {'number': basestring, 'street': basestring, 'town': basestring}
        ],
        'phone': [
            {'type': basestring, 'number': basestring}
        ],


    }
    required_fields = ['firstname', 'lastname']
    default_values = { }


@connection.register
class Publication(Document):
    # allows additional fields to be added to the document on the fly
    use_schemaless = True
    # shortcut to the collection these documents are store in
    __collection__ = 'publications'
    # shortcut to the database name
    __database__ = db
    # allows use of dot.notation instead of dict['notation'] (doesn't seem to work for schemaless fields)
    use_dot_notation = True
    structure = {
        'title': basestring,
        # store the id of the author as a string
        'author': basestring,
    }