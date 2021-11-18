import os

import biothings, config
biothings.config_for_app(config)
from config import DATA_ARCHIVE_ROOT

from biothings.utils.common import uncompressall

import biothings.hub.dataload.dumper


class Hgnc_familyDumper(biothings.hub.dataload.dumper.LastModifiedHTTPDumper):

    SRC_NAME = "hgnc_family"
    SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)
    SCHEDULE = None
    UNCOMPRESS = False
    SRC_URLS = [
        'http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/csv/genefamily_db_tables/family.csv',
        'http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/csv/genefamily_db_tables/gene_has_family.csv'
    ]
    __metadata__ = {
        "src_meta": {
            'url': 'https://www.genenames.org/data/genegroup/#!/',
            'license_url': 'https://www.ebi.ac.uk/about/terms-of-use/'
        }
    }

    def post_dump(self, *args, **kwargs):
        if self.__class__.UNCOMPRESS:
            self.logger.info("Uncompress all archive files in '%s'" %
                             self.new_data_folder)
            uncompressall(self.new_data_folder)
