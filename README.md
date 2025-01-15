Para poder ejecutar correctamente los ejercicios, se debe tener un fichero .env con la siguiente estructura: 
```bash
AZURE_OPENAI_ENDPOINT=<endpoint>
AZURE_OPENAI_API_KEY=<api_key>
```

Crear un entorno virtual (venv) para ejecutar el notebook, para ello: 
Intalar virtualenv si no se tiene
```bash
pip install virtualenv
```
Crear un venv en la carpeta del proyecto
```bash
virtualenv .venv
```
Entrar en el venv:
```bash
.\.venv\Scripts\activate
```
Instalar los paquetes:
```bash
pip install -r requirements.txt
```
Una vez instalados los paquetes necesarios del requirements.txt, para ejecutar el server:
```bash
streamlit run email_app.py
```
