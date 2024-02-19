import pathlib

import psutil

# ディスク使用量をチェックしたいディレクトリを指定
check_target_directory: pathlib = pathlib.Path(__file__).parent
print(f"{check_target_directory=}")

# ディスク使用量を取得
disk_usage = psutil.disk_usage(str(check_target_directory))
print(f"{disk_usage=}")
print(f"{disk_usage.percent=}")
