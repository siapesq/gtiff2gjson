from logzero import logger
from utils.colors import rgb_to_hex
from utils.gdal import get_global_coordinates,get_gdal_dataset,get_gdal_rgb_bands
from utils.geojson import build_geojson

def get_points_grouped_by_color(
    width:int,
    height:int,
    red_band:list[list],
    green_band:list[list],
    min_channel_color:int,
    transform:tuple[5]
):
    try:
        logger.info(f"Grouping coordinates by color")
        points = [ [ {'coords':[],'color':"#ffffff"} for i in range(256) ] for j in range(256) ]
        for y in  range(0,height):
            for x in  range(0,width):
                r = -1 
                g = -1
                if red_band is not None:
                    r=red_band[y][x]
                
                if green_band is not None:
                    g=green_band[y][x]

                if int(r*255)>=min_channel_color or int(g*255)>=min_channel_color:
                    color=rgb_to_hex(r=int(r*255),g=int(g*255),b=0)
                    lng,lat=get_global_coordinates(x=x,y=y,transform=transform)
                    points[int(r*255)][int(g*255)]['coords'].append([lng,lat])
                    points[int(r*255)][int(g*255)]['color']=color
        return points
    except Exception as err:
        raise Exception(err)
    
def process_raster(
    raster_name:str,
    geojson_name:str,
    min_channel_color:int,
    max_distance_between_points:int
):
    try:
        logger.info(f"Init Processing Raster {raster_name}")
        logger.info(f"MIN_CHANNEL_COLOR {min_channel_color}")
        logger.info(f"MAX_DISTANCE_BETWEEN_POINTS {max_distance_between_points}")
        dataset = get_gdal_dataset(raster_name)
        transform=dataset.GetGeoTransform()
        red_band,green_band=get_gdal_rgb_bands(dataset)
        height = dataset.RasterYSize
        width = dataset.RasterXSize
        logger.info(f"Raster Resolution {width}X{height}")
        points=get_points_grouped_by_color(
            width=width,
            height=height,
            red_band=red_band,
            green_band=green_band,
            min_channel_color=min_channel_color,
            transform=transform
        )
        build_geojson(
            geojson_name=geojson_name,
            points=points,
            min_channel_color=min_channel_color,
            max_distance_between_points=max_distance_between_points
        )
        logger.info(f"Finish Processing Raster {raster_name} Output at {geojson_name}")
    except Exception as err:
        raise Exception(err)