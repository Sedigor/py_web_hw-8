from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ListField, StringField, ReferenceField


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField()
    meta = {'allow_inheritance': True}