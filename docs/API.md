# API VNish utilizada

Base URL del ejemplo:

```text
http://192.168.1.108
```

## Lectura pública

| Método | Endpoint | Uso |
|---|---|---|
| GET | `/api/v1/summary` | Hashrate, temperaturas, placas, ventiladores, pools y throttle |
| GET | `/api/v1/status` | Estado, tiempo de estado, throttle y bloqueo |
| GET | `/api/v1/perf-summary` | Perfil, frecuencia y voltaje configurados |
| GET | `/api/v1/boards` | Información detallada de hashboards y chips |
| GET | `/api/v1/metrics` | Métricas históricas |
| GET | `/api/v1/autotune/presets` | Perfiles disponibles y estado de autotune |

## Autenticación

```http
POST /api/v1/unlock
Content-Type: application/json

{"pw":"CONTRASEÑA"}
```

La respuesta contiene un token. Home Assistant lo envía en las operaciones privilegiadas:

```http
Authorization: TOKEN
```

## Control de minería

| Método | Endpoint | Acción |
|---|---|---|
| POST | `/api/v1/mining/start` | Arranca la minería |
| POST | `/api/v1/mining/stop` | Detiene la minería |
| POST | `/api/v1/mining/restart` | Reinicia el backend |
| POST | `/api/v1/mining/throttle` | Aplica un porcentaje de rendimiento |
| POST | `/api/v1/system/reboot` | Reinicia el equipo |

Ejemplo de throttle:

```json
{"percent": 50}
```

## Ajustes

El endpoint autenticado `GET /api/v1/settings` devuelve la configuración completa. Para evitar sobrescribir campos de VNish, los scripts siguen este flujo:

1. Desbloquear y obtener token.
2. Leer los ajustes actuales.
3. Conservar la sección completa correspondiente.
4. Modificar únicamente los campos seleccionados.
5. Enviar el fragmento mediante `POST /api/v1/settings`.
6. Reiniciar el backend cuando sea necesario.

### Perfil

Se modifica:

```json
{"miner":{"overclock":{"preset":"1680"}}}
```

El package conserva el resto de `overclock` antes de enviarlo.

### Modo manual

Se establece `preset: disabled`, se actualizan `globals.freq` y `globals.volt`, y las frecuencias de cadena se ponen a cero para utilizar los valores globales.

### Ventiladores

Campos confirmados:

```json
{
  "mode": {"name": "auto", "param": 75},
  "fan_min_count": 2,
  "fan_min_duty": 17,
  "fan_max_duty": 62
}
```

El package conserva `mode.name` y modifica únicamente la temperatura objetivo y los límites seleccionados.
