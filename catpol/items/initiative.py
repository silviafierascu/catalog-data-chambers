# -*- coding: utf-8 -*-

import json
import scrapy
import hashlib

class InitiativeItem(scrapy.Item):
    title = scrapy.Field()
    status = scrapy.Field()
    author = scrapy.Field()
