from src.Stages.logging import logger
from src.Stages.pipeline.Data_Ingestion_P import DataIngestionTrainingPipeline
from src.Stages.pipeline.Model_Train_P import ModelTrainingPipeline
from src.Stages.pipeline.Model_Evaluation_MLFlow_P import EvaluationPipeline

# STAGE_NAME = "Data Ingestion stage"
# try:
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
#    data_ingestion = DataIngestionTrainingPipeline()
#    data_ingestion.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e

# STAGE_NAME = "Training"
# try: 
#    logger.info(f"*******************")
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#    model_trainer = ModelTrainingPipeline()
#    model_trainer.main()
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e

STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e