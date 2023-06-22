from src.TextSummarizer.pipeline.stage_01_dataingestion import DatatIngestionPipeline
from src.TextSummarizer.pipeline.stage_02_Datavalidiation import DatatValidationPipeline
from src.TextSummarizer.pipeline.stage03_datatransformation import DatatTransformationPipeline
from src.TextSummarizer.pipeline.st_04_model_trainer import ModelTrainerPipeline
from src.TextSummarizer.pipeline.st_05_modelEvaluation import ModelEvaluationTrainingPipeline

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

stage_name="Data model_trainer stage"

try:
    logger.info(f">>>> stage {stage_name} stage <<<<<")
    ModelTrainer=ModelTrainerPipeline()
    ModelTrainer.main()
    logger.info(f">>>>>>> stage {stage_name} completed <<<<<<\n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e