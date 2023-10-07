import os
import tarfile

# Путь к папке с архивом
# model_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'input')
model_dir = '../models'

# Имя архива
archive_name = 'gluon_model.tar.gz'

# Полный путь к архиву
archive_path = os.path.join(model_dir, archive_name)

# Распаковка архива
with tarfile.open(archive_path, 'r:gz') as tar:
    tar.extractall(model_dir)

# Удаление архива
os.remove(archive_path)
