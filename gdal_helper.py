from logzero import logger
from osgeo import gdal
gdal.UseExceptions()
def get_global_coordinates(x, y,transform)->tuple:
    """Returns global coordinates from pixel x, y coords"""
    try:
        x_origin=transform[0] 
        y_origin=transform[3] 
        pixel_width=transform[1]
        pixel_height=transform[5]
        rotation_1=transform[2] 
        rotation_2=transform[4]
        xp = pixel_width * x + rotation_1 * y + x_origin
        yp = rotation_2 * x + pixel_height * y + y_origin
        return (xp, yp)
    except Exception as err:
        raise Exception(err)

def get_gdal_dataset(file_name:str)->gdal.Dataset:
    try:
        logger.info(f"Initializing GDAL Dataset")
        dataset = gdal.Open(file_name)
        if not dataset:
            raise Exception(f"Raster {file_name} could not be open")
        return dataset
    except Exception as err:
        raise Exception(err)
    
def get_gdal_rgb_bands(dataset:gdal.Dataset)->tuple:
    try:
        logger.info(f"Getting Raster BANDS(R,G)")
        logger.info(f"BAND_NUMBER={dataset.RasterCount}")
        red_band=None
        green_band=None
        if dataset.RasterCount>=1:
            red_band=dataset.GetRasterBand(1).ReadAsArray()
        if dataset.RasterCount>=2:
            green_band=dataset.GetRasterBand(2).ReadAsArray()
        return (red_band,green_band)
    except Exception as err:
        raise Exception(err)