from src.Stages.config.configuration import ConfigurationManager
from src.Stages.components.Model_Evaluation_MLFlow import Evaluation
from src.Stages.logging import logger
from pathlib import Path

#Loading config.yaml and prams.yaml files
CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")

STAGE_NAME = "Evaluation stage"
class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager(CONFIG_FILE_PATH, PARAMS_FILE_PATH)
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
            