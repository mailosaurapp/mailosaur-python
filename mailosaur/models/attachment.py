# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Attachment(Model):
    """Attachment.

    :param id:
    :type id: str
    :param content_type:
    :type content_type: str
    :param file_name:
    :type file_name: str
    :param content_id:
    :type content_id: str
    :param length:
    :type length: int
    :param url:
    :type url: str
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'content_id': {'key': 'contentId', 'type': 'str'},
        'length': {'key': 'length', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, id, content_type=None, file_name=None, content_id=None, length=None, url=None):
        super(Attachment, self).__init__()
        self.id = id
        self.content_type = content_type
        self.file_name = file_name
        self.content_id = content_id
        self.length = length
        self.url = url