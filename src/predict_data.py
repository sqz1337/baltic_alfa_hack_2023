import os
from autogluon.tabular import TabularPredictor, TabularDataset
from sklearn.metrics import roc_auc_score

# Определите путь к данным для предсказаний относительно текущего расположения скрипта
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'input')

# Загрузка данных для предсказаний
test_data = TabularDataset(os.path.join(data_dir, 'test.parquet'))

# Определите путь для сохранения предсказаний
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'output')
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'predictions.csv')

# Определите путь к последней модели
model_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
model_list = os.listdir(model_dir)
model_list.sort(reverse=True)
latest_model = model_list[0]
model_path = os.path.join(model_dir, latest_model)

# Загрузка обученной модели
predictor = TabularPredictor.load(model_path)

# Предсказания
pred = predictor.predict_proba(test_data, as_multiclass=False)

# Сохранение предсказаний в CSV
test_data['score'] = pred
test_data[['id', 'score']].to_csv(output_file, index=False)
