# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



from datetime import date, datetime
from dataclasses import dataclass, field
from scrapy.item import Item, Field
from itemloaders.processors import TakeFirst  # provided by scrapy


class BookableDate(scrapy.Item):
    event_id = Field()
    event_occurrence = Field()

    name = Field()
    location = Field()
    facility = Field()
    
    details = Field()

    start_time = Field()
    end_time = Field()
    duration_minutes = Field()
    time_range_description = Field()

    address = Field()
    facility = Field()

    instructor = Field(default=None)

    url = Field()

    category = Field()
    
