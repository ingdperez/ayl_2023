### Puesta en funcionamiento
1. Abre una terminal de comandos
2. Navega hasta la raíz del proyecto donde quieres listar las dependencias
3. Ejecuta:

    `pip freeze > requirements.txt`
4. Abre el archivo requirements.txt creado, este listará todas las dependecias de paquetes así como la versión del mismo que tu proyecto requiere para funcionar:
5. Para instalar esta lista de dependencias en cualquier otra instalación de Python puedes ejecutar: 

    `pip install -r requirements.txt`