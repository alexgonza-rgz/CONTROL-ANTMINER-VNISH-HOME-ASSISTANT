# Home Assistant VNish Control

Control y monitorización local de un Antminer con firmware VNish desde Home Assistant.

El proyecto nació y se verificó con un **Antminer S19 Pro**, **VNish 1.3.5** y la IP `192.168.1.108`. Utiliza directamente la API HTTP local de VNish; no expone el minero a Internet y no necesita componentes personalizados de Lovelace.

## Funciones

- Estado de conexión y minería.
- Hashrate total y por cada una de las tres hashboards.
- Temperaturas de chips y PCB.
- RPM de los cuatro ventiladores y duty PWM actual.
- Frecuencia y voltaje configurados y medidos.
- Consumo y eficiencia cuando la fuente ofrece telemetría.
- Throttle de rendimiento entre el 10 y el 100 %.
- Inicio, parada y reinicio del backend de minería.
- Reinicio completo del Antminer.
- Selección de los 25 perfiles VNish, de 1680 W / 57 TH a 5520 W / 184 TH.
- Modo manual de frecuencia y voltaje, desactivando automáticamente el preset.
- Configuración automática de ventiladores: temperatura objetivo, PWM mínimo/máximo y número mínimo de ventiladores.
- Protección automática por sobretemperatura, watchdog sin hashrate y aviso de desconexión.
- Tarjeta Lovelace compacta creada únicamente con tarjetas nativas.

## Requisitos

- Home Assistant con soporte para `packages`.
- Antminer accesible desde la red de Home Assistant.
- VNish 1.3.5 o una versión con API compatible.
- Contraseña del panel VNish.

## Instalación

1. Copia [`home-assistant/packages/vnish_antminer_package.yaml`](home-assistant/packages/vnish_antminer_package.yaml) a:

   ```text
   /config/packages/vnish_antminer_package.yaml
   ```

2. Habilita los packages en `/config/configuration.yaml`:

   ```yaml
   homeassistant:
     packages: !include_dir_named packages
   ```

3. Añade la contraseña de VNish a `/config/secrets.yaml`:

   ```yaml
   vnish_password: "CAMBIA_ESTA_CONTRASEÑA"
   ```

4. Si el Antminer no usa `192.168.1.108`, sustituye esa IP en todo el package.

5. Comprueba la configuración y reinicia Home Assistant.

6. En el panel de Home Assistant, añade una tarjeta **Manual** y pega el contenido de [`home-assistant/dashboards/vnish_antminer_card.yaml`](home-assistant/dashboards/vnish_antminer_card.yaml).

## Uso seguro

Los perfiles superiores a la capacidad nominal de la fuente pueden provocar sobrecarga, sobretemperatura o daños. Los perfiles sin ajustar pueden iniciar el autotune de VNish. No utilices límites PWM bajos sin supervisar las temperaturas.

El modo manual envía `preset: disabled`, pone la frecuencia individual de cada cadena a cero y aplica la frecuencia y el voltaje globales seleccionados. Utiliza valores que ya hayas validado en VNish.

## API

La integración usa `/api/v1/summary`, `/api/v1/perf-summary`, `/api/v1/settings`, `/api/v1/unlock` y los comandos de minería. Las operaciones privilegiadas obtienen primero un token y lo envían mediante `Authorization`.

Consulta [docs/API.md](docs/API.md) para ver los endpoints y el flujo de autenticación.

## Compatibilidad

La estructura JSON puede cambiar entre versiones de VNish o modelos de Antminer. Antes de usarlo con otro equipo, comprueba los endpoints y adapta el número de hashboards o ventiladores.

## Problemas conocidos

- Algunas fuentes no proporcionan consumo y eficiencia; en ese caso los sensores mostrarán `0`.
- Las entidades antiguas eliminadas del package pueden quedar huérfanas en el registro de Home Assistant y deben borrarse manualmente.
- No se incluye el cambio de modo de ventilación porque solo se ha verificado el modo `auto`. Se conservan siempre el modo y los campos desconocidos existentes.

## Licencia

MIT. Consulta [LICENSE](LICENSE).
