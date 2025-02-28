import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


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

    
class MedexSpider(CrawlSpider):
    name = "medex"
    allowed_domains = ["medex.com.bd"]
    start_urls = ["https://medex.com.bd/brands"]

    rules = (
        # Follow pagination links
        Rule(LinkExtractor(restrict_css='li.page-item a[rel="next"]'), follow=True),
        # Extract and process medicine detail pages
        Rule(
            LinkExtractor(restrict_css=".hoverable-block"),
            callback="parse_medicine",
        ),
    )

    def parse_medicine(self, response):
        """
        Parse the medicine detail page and extract all available information.
        """
        item = MedexItem()

        # Extract basic information with improved error handling
        item["name"] = self.extract_text(response, '//h1[@class="page-heading-1-l brand"]/text()')
        item["dosage_form"] = self.extract_text(response, '//h1[@class="page-heading-1-l brand"]/small/text()')
        item["generic_name"] = self.extract_text(response, '//div[contains(., "Generic Name")]/a/text()')
        item["strength"] = self.extract_text(response, ".data-row-strength .grey-ligten::text")
        item["manufacturer"] = self.extract_text(response, '//div[@title="Manufactured by"]/a/text()')

        # Extract pricing information
        unit_price = self.extract_text(
            response, '//span[contains(., "Unit Price:")]/following-sibling::span[1]/text()'
        )
        pack_size = self.extract_text(
            response, '//span[contains(., "Unit Price:")]/following-sibling::span[@class="pack-size-info"]/text()'
        )
        item["unit_price"] = f"{unit_price} {pack_size}" if pack_size else unit_price
        item["strip_price"] = self.extract_text(
            response, '//span[contains(., "Strip Price:")]/following-sibling::span/text()'
        )

        # Extract detailed information using the section helper method
        sections = {
            "indications": "indications",
            "composition": "composition",
            "pharmacology": "mode_of_action",
            "dosage_administration": "dosage",
            "interaction": "interaction",
            "contraindications": "contraindications",
            "side_effects": "side_effects",
            "pregnancy_lactation": "pregnancy_cat",
            "precautions_warnings": "precautions",
            "overdose_effects": "overdose_effects",
            "therapeutic_class": "drug_classes",
            "storage_conditions": "storage_conditions",
        }

        for item_key, section_id in sections.items():
            item[item_key] = self.get_section(response, section_id)

        self.logger.info(f"Scraped medicine: {item['name']}")
        yield item

    def extract_text(self, response, xpath_or_css):
        """
        Helper method to extract and clean text using either xpath or css selector.
        Returns empty string if nothing is found.
        """
        result = ""
        if xpath_or_css.startswith("//") or xpath_or_css.startswith("(//"):
            # It's an xpath
            result = response.xpath(xpath_or_css).get("")
        else:
            # It's a CSS selector
            result = response.css(xpath_or_css).get("")
            
        return result.strip() if result else ""

    def get_section(self, response, section_id):
        """
        Helper function to extract section content from the medicine detail page.
        Handles missing sections gracefully.
        """
        # First check if the section exists
        if not response.xpath(f'//div[@id="{section_id}"]').get():
            return ""
            
        # Extract all text from the section
        text_parts = response.xpath(
            f'//div[@id="{section_id}"]/following-sibling::div[@class="ac-body"][1]//text()'
        ).getall()
        
        # Clean and join the text
        return " ".join([part.strip() for part in text_parts if part.strip()])