"""Module interface.py"""
import logging
import os

import config
import src.algorithms.detections
import src.algorithms.mappings
import src.algorithms.page
import src.functions.objects


class Interface:
    """
    Executes the functions that process the input text, and the tokens classifications results.
    """

    def __init__(self):
        """
        Constructor
        """

        # Objects
        objects = src.functions.objects.Objects()
        self.__architecture = objects.read(
            uri=os.path.join(config.Config().data_, 'architecture.json'))['name']

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, text: str, tokens: list):
        """

        :param text:
        :param tokens:
        :return:
        """

        page = src.algorithms.page.Page(text=text).exc()
        detections = src.algorithms.detections.Detections(tokens=tokens).exc()
        mappings = src.algorithms.mappings.Mappings(page=page, detections=detections).exc()
        
        self.__logger.info('Page:\n%s', page)
        self.__logger.info('Detections:\n%s', detections)
        self.__logger.info('Mappings:\n%s', mappings)
