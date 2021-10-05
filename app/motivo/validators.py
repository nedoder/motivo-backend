from django.core.exceptions import ValidationError
from practice.settings import UPLOAD_FILE_MAX_SIZE_MB

def validate_file_size(value):
    """
    Make sure the file has proper size
        2.5MB - 2621440
        3MB - 3145728
        5MB - 5242880
        10MB - 10485760
        20MB - 20971520
        50MB - 5242880
        100MB - 104857600
        250MB - 214958080
        500MB - 429916160
    """
    filesize= value.size
    limitation_bytes = 1024 * 1024 * UPLOAD_FILE_MAX_SIZE_MB
    
    if filesize > limitation_bytes:
        raise ValidationError(f"The maximum file size that can be uploaded is {UPLOAD_FILE_MAX_SIZE_MB}MB")
    else:
        return value
