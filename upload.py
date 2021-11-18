import os

import biothings, config
biothings.config_for_app(config)

import biothings.hub.dataload.uploader

# when code is exported, import becomes relative
try:
    from hgnc_family.parser import load_family as parser_func
except ImportError:
    from .parser import load_family as parser_func


class Hgnc_familyUploader(biothings.hub.dataload.uploader.BaseSourceUploader):

    name = "hgnc_family"
    __metadata__ = {
        "src_meta": {
            'url': 'https://www.genenames.org/data/genegroup/#!/',
            'license_url': 'https://www.ebi.ac.uk/about/terms-of-use/'
        }
    }
    idconverter = None
    storage_class = biothings.hub.dataload.storage.BasicStorage

    def load_data(self, data_folder):
        self.logger.info("Load data from directory: '%s'" % data_folder)
        return parser_func(data_folder)

    @classmethod
    def get_mapping(klass):
        return         {
            'hgnc_genegroup': {
                'properties': {
                    'abbr': {
                        'copy_to': ['all'],
                        'type': 'text'
                    },
                    'comments': {
                        'type': 'text'
                    },
                    'id': {
                        'normalizer': 'keyword_lowercase_normalizer',
                        'type': 'keyword'
                    },
                    'name': {
                        'type': 'text'
                    },
                    'pubmed': {
                        'type': 'integer'
                    },
                    'typical_gene': {
                        'normalizer': 'keyword_lowercase_normalizer',
                        'type': 'keyword'
                    }
                }
            }
        }

