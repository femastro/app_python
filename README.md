# app_python

# Tener Instalado :  
    youtube-dl
    
    # Para instalar youtube-dl
    :Debian , Ubuntu , Zorin
    sudo apt-get install youtube-dl

# Usar Python

Install Flask
Within the activated environment, use the following command to install Flask:

    pip ó pip3 install Flask

    pip ó pip3 install webbrowser

    pip ó pip3 install tqdm

# Si usas Base de Datos Msql :

    pip ó pip3 install Flask_mysqldb

# Crear Json 

    Crear en el root , la carpeta y dentro el archivo 
    
    EJ: config/db.json

    {
        "host":"127.0.0.1",
        "user":"root",
        "password":"",
        "dbase":"appPython"
    }
# Usar variable de entorno

    pip install python-dotenv

    # Probando Varaibles de Entorno
    from dotenv import load_dotenv
    load_dotenv()
    title = os.getenv('TITLE')
    print('Titulo = '+ title)

    Archivo en el root : .env
        TITLE="titulo" 
