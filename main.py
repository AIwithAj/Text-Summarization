from src.TextSummarizer.pipeline.stage_01_dataingestion import DatatIngestionPipeline
from src.TextSummarizer.pipeline.stage_02_Datavalidiation import DatatValidationPipeline
from src.TextSummarizer.pipeline.stage03_datatransformation import DatatTransformationPipeline

from src.TextSummarizer.logging import logger

stage_name="Data Ingestion stage"

try:
    logger.info(f">>>> stage {stage_name} stage <<<<<")
    data_ingestion=DatatIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {stage_name} completed <<<<<<\n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e



stage_name="Data Validation stage"

try:
    logger.info(f">>>> stage {stage_name} stage <<<<<")
    data_validation=DatatValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {stage_name} completed <<<<<<\n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e


stage_name="Data Transformation stage"

try:
    logger.info(f">>>> stage {stage_name} stage <<<<<")
    data_transformation=DatatTransformationPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> stage {stage_name} completed <<<<<<\n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e