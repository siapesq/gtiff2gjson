from logzero import logger
from colors_helper import rgb_to_hex
from geojson_helper import create_geojson
from gdal_helper import get_global_coordinates,get_gdal_dataset,get_gdal_rgb_bands

def check_pixel_raster_colors(width:int,height:int,red_band:list[list],green_band:list[list],LIMIAR_OF_COLOR:int,transform):
    try:
        logger.info(f"Checking Pixel Raster")
        points_same_color = [ [ {'coords':[],'color':"#ffffff"} for i in range(256) ] for j in range(256) ]
        for y in  range(0,height):
            for x in  range(0,width):
                r=-1
                g=-1
                if red_band is not None:
                    r=red_band[y][x]
                
                if green_band is not None:
                    g=green_band[y][x]

                if int(r*255)>=LIMIAR_OF_COLOR or int(g*255)>=LIMIAR_OF_COLOR:
                    color=rgb_to_hex(r=int(r*255),g=int(g*255),b=0)
                    lng,lat=get_global_coordinates(x=x,y=y,transform=transform)
                    points_same_color[int(r*255)][int(g*255)]['coords'].append([lng,lat])
                    points_same_color[int(r*255)][int(g*255)]['color']=color
        return points_same_color
    except Exception as err:
        raise Exception(err)

def process_raster(raster_name:str,geojson_name:str,limiar_of_color:int,max_distance_between_points):
    try:
        LIMIAR_OF_COLOR=limiar_of_color
        MAX_DISTANCE_BETWEEN_POINTS=max_distance_between_points
        logger.info(f"Init Processing Raster {raster_name}")
        logger.info(f"LIMIAR OF COLOR {LIMIAR_OF_COLOR}")
        logger.info(f"MAX_DISTANCE_BETWEEN_POINTS {MAX_DISTANCE_BETWEEN_POINTS}")
        dataset = get_gdal_dataset(raster_name)
        transform=dataset.GetGeoTransform()
        red_band,green_band=get_gdal_rgb_bands(dataset)
        height = dataset.RasterYSize
        width = dataset.RasterXSize
        logger.info(f"Raster Resolution {width}X{height}")
        points_same_color=check_pixel_raster_colors(
            width=width,
            height=height,
            red_band=red_band,
            green_band=green_band,
            LIMIAR_OF_COLOR=LIMIAR_OF_COLOR,
            transform=transform
        )

        create_geojson(
            geojson_name=geojson_name,
            points_same_color=points_same_color,
            LIMIAR_OF_COLOR=LIMIAR_OF_COLOR,
            MAX_DISTANCE_BETWEEN_POINTS=MAX_DISTANCE_BETWEEN_POINTS
        )
        logger.info(f"Finish Processing Raster {raster_name} Output at {geojson_name}")
    except Exception as err:
        raise Exception(err)