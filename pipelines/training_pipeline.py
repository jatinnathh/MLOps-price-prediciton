import sys
import os

current_file_path = os.path.abspath(__file__)
project_root = os.path.abspath(os.path.join(current_file_path, '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


from steps.data_ingestion_step import data_ingestion_step
from steps.data_splitter_step import data_splitter_step
from steps.feature_engineering_step import feature_engineering_step
from steps.handle_missing_values_step import handle_missing_values_step
from steps.model_building_step import model_building_step
from steps.model_evaluator_step import model_evaluator_step
from steps.outlier_detection_step import outlier_detection_step
from zenml import Model, pipeline, step

@pipeline(
    model=Model(
        name="prices_predictor"
    ),
)

#end to end pipeline 
def ml_pipeline():
    raw_data=data_ingestion_step(
        file_path=r'C:\Users\jatin\Desktop\CAL AI&ML\Self\house pred end to end\data\archive.zip'
    )


    filled_data=handle_missing_values_step(raw_data)

    engineered_data=feature_engineering_step(
        filled_data,strategy='log',features=['Gr Liv Area','SalePrice']
    )

    clean_data=outlier_detection_step(engineered_data,column_name='SalePrice')

    X_train,X_test,y_train,y_test=data_splitter_step(clean_data,target_column='SalePrice')

    model=model_building_step(X_train=X_train,y_train=y_train)

    evaluation_metrics,mse=model_evaluator_step(
        trained_model=model,X_test=X_test,y_test=y_test
    )

    return model
if __name__ == "__main__":
    run = ml_pipeline()