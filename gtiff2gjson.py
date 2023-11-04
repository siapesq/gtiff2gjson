import argparse
from utils.raster import process_raster
from logzero import logger
import os
try:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "raster",
        help="GEOTIFF para ser convertido para GeoJSON",
        type=str
    )
    parser.add_argument(
        "--geojson",
        nargs='?',
        default=False,
        help="Nome do arquivo de saida.\nDefault vai ser o nome do antes do .tif",
        type=str
    )
    parser.add_argument(
        "--min-channel-color",
        nargs='?',
        default=90,
        help="",
        type=int
    )
    parser.add_argument(
        "--max-distance-between-points",
        nargs='?',
        default=200,
        help="",
        type=int
    )
    args=parser.parse_args()
    
    if not args.geojson:
        nome_geo_tiff=os.path.splitext(args.raster)[0]
        args.geojson=f"{nome_geo_tiff}.geojson"
    
    process_raster(
        raster_name=args.raster,
        geojson_name=args.geojson,
        min_channel_color=args.min_channel_color,
        max_distance_between_points=args.max_distance_between_points
    )
    
except Exception as err:
    logger.error(err)
