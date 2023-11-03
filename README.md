# geotiff_conversor
Python CLI para converter GeoTiffs de 2 Bandas para geojson

### Uso 
  * Usando o Binário
    
        usage: geotiff_conversor [-h] [--geojson [GEOJSON]] [--limiar_of_color [LIMIAR_OF_COLOR]]
                               [--max_distance_points [MAX_DISTANCE_POINTS]]
                               raste
        positional arguments:
          raster                GEOTIFF para ser convertido para GeoJSON
        
        options:
          -h, --help            show this help message and exit
          --geojson [GEOJSON]   Nome do arquivo de saida. Default vai ser o nome do antes do .tif
          --limiar_of_color [LIMIAR_OF_COLOR]
                                Limiar de cor é o limite do tom das Bandas RGB. Por Exemplo Se for 100,Só serão considerados pixels com a
                                banda R e G superiores a 100
          --max_distance_points [MAX_DISTANCE_POINTS]
                              É a distancia máxima em KiloMetros entre 2 pontos da mesma cor. É utilizado para a construção do GeoJSON

  * Usando o Script
    
      * Inicie o python Venv
        
            python3 -m venv venv
        
      * Instale todas as dependências(Talvez seja necessário instalar o gdal na sua máquina)

            pip install -r requirements.txt

      * Rode o script

            python3 geotiff_conversor raster.tif

  * Para Criar o Binário
    
       *  Compilar o trem com pyinstaller

              pyinstaller geotiff_conversor
          
       * Para Rodar

             ./dist/geotiff_conversor/geotiff_conversor    
        
### Dependências
  * gdal
  * geojson
  * numpy
  * wheel
  * logzero
  * turfpy
  * pyinstaller

