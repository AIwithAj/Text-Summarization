from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.components.data_validation import DataValidation
from src.TextSummarizer.logging import logger

class DatatValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_vaidation=DataValidation(config=data_validation_config)
        data_vaidation.validate_all_files_exists()