import scrapy


class MedexItem(scrapy.Item):
    name = scrapy.Field()
    dosage_form = scrapy.Field()
    generic_name = scrapy.Field()
    strength = scrapy.Field()
    manufacturer = scrapy.Field()
    unit_price = scrapy.Field()
    strip_price = scrapy.Field()
    indications = scrapy.Field()
    composition = scrapy.Field()
    pharmacology = scrapy.Field()
    dosage_administration = scrapy.Field()
    interaction = scrapy.Field()
    contraindications = scrapy.Field()
    side_effects = scrapy.Field()
    pregnancy_lactation = scrapy.Field()
    precautions_warnings = scrapy.Field()
    overdose_effects = scrapy.Field()
    therapeutic_class = scrapy.Field()
    storage_conditions = scrapy.Field()
