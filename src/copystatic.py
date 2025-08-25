import os
import shutil


def copy_files_recursive(source, target):
    if not os.path.exists(target):
        os.mkdir(target)

    for content in os.listdir(source):
        source_path = os.path.join(source, content)
        target_path = os.path.join(target, content)
        print(f" * {source_path} -> {target_path}")
        if not os.path.isfile(source_path):
            copy_files_recursive(source_path, target_path)
        else:
            shutil.copy(source_path, target_path)
