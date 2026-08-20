# Contribuir

1. Crea una rama desde `main`.
2. No incluyas direcciones públicas, contraseñas, tokens, datos de pools ni archivos HAR sin revisar.
3. Conserva la compatibilidad con tarjetas nativas de Home Assistant.
4. Valida los archivos antes de enviar cambios:

   ```bash
   python -m pip install PyYAML
   python scripts/validate_yaml.py
   ```

5. Explica el modelo de Antminer y la versión de VNish usados durante las pruebas.

Los cambios de endpoints o cuerpos JSON deben estar respaldados por una captura de la API o documentación verificable.
