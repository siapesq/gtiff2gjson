from logzero import logger
from geojson import Point,FeatureCollection,dump,Feature,Polygon,MultiPoint,MultiPolygon
from turfpy import measurement
from turfpy.transformation import convex
#ignore shapely warnings
import warnings
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning) 

def create_point_feature(cordinates:tuple[2],properties:dict)->Feature:
    try:
        ponto=Point(coordinates=cordinates)
        feature=Feature(geometry=ponto,properties=properties)
        return feature
    except Exception as err:
        raise Exception(err)
    
def create_polygon(cordinates:list[list[2]],properties:dict)->Feature:
    try:
        polygon=Polygon(coordinates=cordinates)
        feature=Feature(geometry=polygon,properties=properties)
        return feature
    except Exception as err:
        raise Exception(err)

def create_multipoint(cordinates:list[list],properties:dict)->Feature:
    try:
        pontos=MultiPoint(coordinates=cordinates)
        feature=Feature(geometry=pontos,properties=properties)
        return feature
    except Exception as err:
        raise Exception(err)

def create_polygon_properties(color:str)->dict:
    try:
        return{
            "fill":color,
            "stroke-width": 0,
            "stroke-opacity": 0,
            "fill-opacity": 1
        }
    except Exception as err:
        raise Exception(err)
    
def create_multipolygon(cordinates:list[list],properties:dict)->Feature:
    try:
        multipolygon=MultiPolygon(coordinates=cordinates)
        feature=Feature(
            geometry=multipolygon,
            properties=properties
        )
        return feature
    except Exception as err:
        raise Exception(err)

def make_convex_from_polygon(cordinates):
    try:
        points=[]
        for point in cordinates:
            feature=Feature(geometry=Point(coordinates=point))
            points.append(feature)
        feature=convex(features=FeatureCollection(points))
        return feature
    except Exception as err:
        raise Exception(err)

def write_geojson(geojson_name:str,features:list[Feature]):
    try:
        logger.info(f"Dumping GeoJSON to Output File {geojson_name}")
        geojson=FeatureCollection(features=features)
        with open(geojson_name, 'w') as outfile:
            dump(geojson,outfile)
    except Exception as err:
        raise Exception(err)
    
def create_multipolygon_from_points_with_same_color(
    max_distance_between_points:int,
    points_coords:list,
    color:str
)->Feature | None:
    try:
        polygons=[]
        for index in range(0,len(points_coords)):

            current_point=Point(points_coords[index])
            polygon_coords=[points_coords[index]]
            
            is_last_point=index==len(points_coords)-1
            if is_last_point:
                break

            for next_index in range(index+1,len(points_coords)):
                next_point=Point(points_coords[next_index])
                distance=measurement.distance(point1=current_point,point2=next_point,units='km')

                if distance<=max_distance_between_points:
                    #new_vertice
                    polygon_coords.append(points_coords[next_index])
                else:
                    #close polygon
                    polygon_coords.append(points_coords[index])
                    break

            has_linear_ring=len(polygon_coords)>=4
            if has_linear_ring:
                feature=make_convex_from_polygon(cordinates=polygon_coords)
                convex_coordinates=feature['geometry']['coordinates']

                if type(convex_coordinates[0][0])==list:
                    polygons.append(convex_coordinates)

        if len(polygons)>0:
            properties=create_polygon_properties(color=color)
            feature=create_multipolygon(cordinates=polygons,properties=properties)
            return feature

    except Exception as err:
        raise Exception(err)


def build_geojson(
    geojson_name:str,
    points:list[list[dict[str]]],
    min_channel_color:int,
    max_distance_between_points:int
):
    try:
        logger.info(f"Init GeoJSON Building")
        features=[]
        for r in range(min_channel_color,256):
            for g in range(min_channel_color,256):

                points_coords=points[r][g]['coords']
                color=points[r][g]['color']
                
                if len(points_coords)==0:
                    continue

                feature=create_multipolygon_from_points_with_same_color(
                    max_distance_between_points=max_distance_between_points,
                    points_coords=points_coords,
                    color=color
                )

                if feature is None:
                    continue

                features.append(feature)

        write_geojson(geojson_name=geojson_name,features=features)

        logger.info(f"Number of features in GeoJSON {len(features)}")

    except Exception as err:

        raise Exception(err)
    
