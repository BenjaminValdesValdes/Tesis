# Contexto del Proyecto: Tesis UTEM

## Resumen del Proyecto
Sistema de Control de Acceso Vehicular Automatizado mediante Reconocimiento de Patentes para la Universidad Tecnológica Metropolitana, Sede Campus Ñuñoa.

## Objetivos Clave
- **Target:** Validar el acceso de **funcionarios** al estacionamiento del Campus Ñuñoa.
- **Tecnología Principal:** Detección de objetos mediante YOLOv8 (o iteraciones modernas si la literatura lo justifica).
- **Arquitectura:** Edge Computing local para garantizar baja latencia (<100ms) y privacidad.
- **Hardware Teórico:** Raspberry Pi 5 (con posibles aceleradores NPU) o NVIDIA Jetson Nano.
- **Prototipo Real (Entregable):** Un prototipo de software en PC (simulación) usando cámara web y un panel web de administración institucional. No habrá instalación física de barreras.
- **Restricciones de Detección:** El modelo reconoce formatos civiles chilenos y patentes verdes, **excluyendo** vehículos de emergencia (policías, bomberos), de gran tonelaje y **motocicletas** (dado que solo poseen patente trasera, haciéndolas indetectables por la cámara frontal del portón).

## Reglas de Comportamiento para Antigravity (IA)
1. **Evitar desvíos académicos (Scope Creep):** Si la literatura documenta técnicas avanzadas irrelevantes para un campus (e.g. lectura de patentes a 150 km/h en autopistas de cobro de peaje), omitirlas o mantenerlas al mínimo. Enfocar la redacción en entornos urbanos de baja velocidad y porterías.
2. **Justificación hacia el Proyecto:** Toda revisión del estado del arte (como la cuantización a INT8 o filtros climáticos) debe conectarse explícitamente con las limitaciones del hardware de borde propuesto para la UTEM.
3. **Prompts Contextualizados:** Todos los prompts generados para NotebookLM u otras IA deben incluir la instrucción explícita de centrarse en las necesidades de un sistema de acceso institucional de bajo costo.
