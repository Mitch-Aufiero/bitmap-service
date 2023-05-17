import shutil
import time
import errno


class FileMover:
    @staticmethod
    def move_file(file_path, destination_path, max_attempts = 5):
            attempt = 1
            while attempt <= max_attempts:
                attempt = attempt + 1
                try:
                    shutil.move(file_path, destination_path)
                except OSError as e:
                    if e.errno == errno.EACCES:
                        time.sleep(1) 
                    else:
                        raise e