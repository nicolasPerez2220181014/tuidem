version: "3.9"

services:
  mongodb:
    # Usa la imagen o el Dockerfile de MongoDB como prefieras
    build: 
      context: .
      dockerfile: dockerfile.mongodb
    restart: always
    container_name: mongo_database_value
    environment:
      MONGO_INITDB_DATABASE: tuidem
      MONGO_INITDB_ROOT_USERNAME: DeVelopers
      MONGO_INITDB_ROOT_PASSWORD: DeV.2024_Tuidem
    volumes:
      - mongo_data:/data/db            # Volumen de Docker para persistencia de datos
      - ./data/logs:/data/logs          # Logs en el sistema de archivos host
      - ./conf/ckMongo:/etc/mongodb/ckMongo
      # Monta el archivo de configuración de MongoDB si es necesario
      - ./conf/mongod.conf:/etc/mongod.conf
    ports:
      - 28364:28364
    # Usa el archivo de configuración solo si es necesario
    command: mongod --config /etc/mongod.conf

  tuidemdocker:
    container_name: tuidem_mongo_app
    build:
      context: .
      dockerfile: dockerfile
    depends_on:
      - mongodb
    ports:
      - '8081:7393'
    working_dir: /tuidem
    command: tail -f /dev/null
    volumes:
      - ./site:/tuidem

# Define los volúmenes de Docker para la base de datos
volumes:
  mongo_data: