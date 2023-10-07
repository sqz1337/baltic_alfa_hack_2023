import os
import datetime
import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor

# Определите путь к данным для обучения относительно текущего расположения скрипта
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'input')

# Загрузите обе части данных
train_part1 = TabularDataset(os.path.join(data_dir, 'train_part1.parquet')).drop(columns=['target_1', 'target_2'])
train_part2 = TabularDataset(os.path.join(data_dir, 'train_part2.parquet')).drop(columns=['target_1', 'target_2'])

# Объедините данные в один DataFrame
train_data = pd.concat([train_part1, train_part2], ignore_index=True)

# Определите путь для сохранения модели
model_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
model_prefix = datetime.datetime.now().strftime("%d%m%y_%H%M%S")
model_path = os.path.join(model_dir, f'{model_prefix}_model')

# Обучение модели
predictor = TabularPredictor(label='total_target', eval_metric='roc_auc', path=model_path).fit(train_data=train_data)
