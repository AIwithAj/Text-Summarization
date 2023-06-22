from src.TextSummarizer.pipeline.stage_01_dataingestion import DatatIngestionPipeline

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