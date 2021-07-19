Documentación necesaria para el frontend:

necesito que la página de introducción de datos lleve un formulario de datos con esta estructura mínima:
<form action="" method="post">
    <label for="user">Nombre: </label>
    <input type="text" id="user" name="user" /><br>
    <label for="text">Mensaje: </label>
    <input type="text" id="text" name="text" /><br>
    <input type="submit" id="send-signup" name="signup" value="Registrar" />
</form>

Los textos 'Nombre', y 'Mensaje' son completamente editables y se pueden substituir, al igual que el 'Registrar' de la etiqueta input de tipo submit.