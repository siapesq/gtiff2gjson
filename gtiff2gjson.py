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
        help="""
            É o valor minímo da banda dos canais R G para processar o pixel.
            Por exemplo se for igual a 90, so serão processados os pixels que possuirem as bandas do canal R ou G >=90.
            Default é 90,pode ser um inteiro entre 1-254
        """,
        type=int
    )
    parser.add_argument(
        "--max-distance-between-points",
        nargs='?',
        default=200,
        help="""
            Distância máxima em kilometros entre os pontos que tem a mesma cor.
            Essa distância é usada para a converter vários pontos de uma mesma cor e um poligono.
            Default é 200
        """,
        type=int
    )
    args=parser.parse_args()
    
    if not args.geojson:
        nome_geo_tiff=os.path.splitext(args.raster)[0]
        args.geojson=f"{nome_geo_tiff}.geojson"
    
    if args.min_channel_color>254 or args.min_channel_color<=0:
        raise Exception("--min-channel-color has invalid value")

    process_raster(
        raster_name=args.raster,
        geojson_name=args.geojson,
        min_channel_color=args.min_channel_color,
        max_distance_between_points=args.max_distance_between_points
    )
    
except Exception as err:
    logger.error(err)
