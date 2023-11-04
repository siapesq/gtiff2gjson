# gtiff2gjson
Python CLI para converter GeoTiffs de 2 Bandas para geojson

### Uso 
  * Usando o Binário
    
        usage: gtiff2gjson [-h] [--geojson [GEOJSON]] [--limiar_of_color [LIMIAR_OF_COLOR]]
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
  * numpy
  * wheel
  * logzero
  * turfpy
  * pyinstaller


