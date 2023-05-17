
class FileExtensionReplacer:
    @staticmethod
    def replace_file_extension(filename, new_extension):
        base_name = filename.rsplit('.', 1)[0]  # Split at the last dot
        new_filename = f"{base_name}{new_extension}"
        return new_filename