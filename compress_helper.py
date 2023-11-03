from logzero import logger
import gzip
import shutil
def compress_file(file_name):
    try:
        logger.info(f"Compressing file {file_name}")
        with open(file_name, 'rb') as f_in:
            with gzip.open(f'{file_name}.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
    except Exception as err:
        raise Exception(err)


    
