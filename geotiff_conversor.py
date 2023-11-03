import argparse
from raster import process_raster
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
        "--limiar_of_color",
        nargs='?',
        default=100,
        help="Limiar de cor é o limite do tom das Bandas RGB.\nPor Exemplo Se for 100,Só serão considerados pixels com a banda R e G superiores a 100",
        type=int
    )
    parser.add_argument(
        "--max_distance_points",
        nargs='?',
        default=500,
        help="É a distancia máxima em KiloMetros entre 2 pontos da mesma cor.\nÉ utilizado para a construção do GeoJSON",
        type=int
    )
    args=parser.parse_args()
    
    if not args.geojson:
        nome_geo_tiff=os.path.splitext(args.raster)[0]
        args.geojson=f"{nome_geo_tiff}.geojson"
    
    process_raster(args.raster,args.geojson,args.limiar_of_color,args.max_distance_points)

except Exception as err:
    logger.error(err)
