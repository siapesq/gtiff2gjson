# gtiff2gjson
Python CLI para converter GeoTiffs de 2 Bandas para geojson

### Uso 
  * Usando o Binário
    
            usage: gtiff2gjson.py [-h] [--geojson [GEOJSON]] [--min-channel-color [MIN_CHANNEL_COLOR]]
                      [--max-distance-between-points [MAX_DISTANCE_BETWEEN_POINTS]]
                      raster

            positional arguments:
            raster                GEOTIFF para ser convertido para GeoJSON

            options:
            -h, --help            show this help message and exit
            --geojson [GEOJSON]   Nome do arquivo de saida. Default vai ser o nome do antes do .tif
            --min-channel-color [MIN_CHANNEL_COLOR]
                                    É o valor minímo da banda dos canais R G para processar o pixel. Por exemplo se for igual a 90, so serão
                                    processados os pixels que possuirem as bandas do canal R ou G >=90. Default é 90,pode ser um inteiro entre
                                    1-254
            --max-distance-between-points [MAX_DISTANCE_BETWEEN_POINTS]
                                    Distância máxima em kilometros entre os pontos que tem a mesma cor. Essa distância é usada para a converter
                                    vários pontos de uma mesma cor e um poligono. Default é 200

  * Usando o Script
    
      * Inicie o python Venv
        
            python3 -m venv venv

      * Carregue o script do venv pro seu shell(exemplo com fish)
        
            source venv/bin/activate.fish
        
      * Instale todas as dependências(Talvez seja necessário instalar o gdal na sua máquina)

            pip install -r requirements.txt

      * Rode o script

            python3 gtiff2gjson raster.tif

  * Para Criar o Binário
    
       *  Compilar o trem com pyinstaller

              pyinstaller gtiff2gjson
          
       * Para Rodar

             ./dist/gtiff2gjson/gtiff2gjson    
        
### Dependências
  * gdal
  * geojson
  * wheel
  * logzero
  * turfpy
  * numpy
  * pyinstaller


