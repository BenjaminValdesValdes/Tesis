# 🗺️ Paso a Paso — Desarrollo del Informe de Trabajo de Título

**Proyecto:** Sistema de Control de Acceso Vehicular Automatizado mediante Reconocimiento de Patentes — UTEM Campus Ñuñoa

**Autores:** Ezequiel Molina · Benjamín Valdés

---

## Estrategia general

El informe se desarrolla **capítulo por capítulo** en la carpeta `borrador/`. Cada capítulo pasa por un flujo de 3 pasos antes de tocar el LaTeX:

```
Borrador v1 (Autor A) → Revisión cruzada (Autor B) → Borrador final → LaTeX
```

**Regla de oro:** No se edita ningún `.tex` hasta que el borrador final del capítulo esté aprobado por ambos.

---

## 👥 Estrategia de trabajo en dupla

### Modelo: Capítulos en paralelo con revisión cruzada

Cada uno toma **capítulos distintos simultáneamente**. Cuando ambos terminan su borrador v1, intercambian para revisión. Esto duplica la velocidad sin sacrificar calidad. 

| Ronda | Ezequiel (escribe) | Benjamín (escribe) |
|-------|--------------------|--------------------|
| 1 | Introducción | Cap. 1 — Marco Teórico |
| 2 | Cap. 2 — Metodología | Cap. 3 — Desarrollo |
| 3 | Cap. 4 — Resultados | Conclusiones |
| 4 | Resumen + Abstract | Glosario + Bibliografía + Anexos |

> **Nota:** La asignación de arriba es una sugerencia. Ajusten según afinidad con el tema. Lo importante es que siempre haya dos capítulos avanzando en paralelo.

### Flujo por capítulo

```
1. Autor A escribe   →  borrador/Cap_X_v1_EzequielOBenjamin.md
2. Autor B revisa    →  Agrega comentarios, corrige, complementa
3. Se consolida      →  borrador/Cap_X_final.md
4. Se pasa a LaTeX   →  documento/capitulos/capituloX.tex
```

### Convención de nombres para borradores

```
borrador/
├── 00_Introduccion_v1_Ezequiel.md
├── 00_Introduccion_v1_Benjamin_revision.md
├── 00_Introduccion_final.md
├── 01_MarcoTeorico_v1_Benjamin.md
├── 01_MarcoTeorico_v1_Ezequiel_revision.md
├── 01_MarcoTeorico_final.md
├── ...
```

---

## 📋 Orden de trabajo (de arriba a abajo)

El orden está pensado para que cada capítulo siguiente tenga como insumo lo que ya se escribió antes. **No es necesario esperar a terminar uno para empezar el siguiente** — por eso se trabaja en paralelo — pero sí se respeta esta prioridad.

---

### Fase 0 · Preparación (antes de escribir)

- [ ] **Leer el anteproyecto completo** — Ambos deben conocerlo al detalle.
  - Archivo: `borrador/Anteproyecto Sistema Acceso Vehicular UTEM (1).pdf`
- [ ] **Consensuar la estructura de capítulos** — Revisar los esqueletos `.tex` que ya existen y ajustar las secciones al contenido real del proyecto.
- [ ] **Definir quién toma qué** en la Ronda 1.

**Producto:** Nada escrito. Solo alineación entre ambos.

---

### Fase 1 · Columna vertebral (Ronda 1)

Estos dos capítulos se escriben **primero y en paralelo** porque definen el alcance de todo lo demás.

#### 📄 Introducción (`00_Introduccion`)

| Sección | Insumo desde el anteproyecto |
|---------|------------------------------|
| Contexto y motivación | "Contextualización y Definición del Problema Institucional" (pág. 3-4) |
| Justificación | Misma sección + Resumen Ejecutivo |
| Problema de investigación | Párrafo final de Contextualización (pág. 4) |
| Objetivo general | "Objetivos del Proyecto" (pág. 4) |
| Objetivos específicos | "Objetivos Específicos" (pág. 4-5) |
| Estructura del documento | Redactar de cero (describe los capítulos) |

> ⚠️ **La Introducción NO es copiar el anteproyecto.** Hay que reescribir con tono de informe final, en pasado o presente según lo que corresponda, y agregar profundidad.

#### 📄 Cap. 1 — Marco Teórico (`01_MarcoTeorico`)

| Sección sugerida | Insumo desde el anteproyecto |
|------------------|------------------------------|
| Visión computacional y detección de objetos | "Detección de Objetos mediante YOLOv8" (pág. 6) |
| Arquitectura YOLOv8 | Expandir con bibliografía adicional |
| OCR y reconocimiento de caracteres | Mencionado brevemente (pág. 6) — expandir |
| Edge Computing vs Cloud Computing | "Arquitectura Edge Computing" (pág. 7) |
| Formatos de patentes en Chile | "Gobierno de Chile, 2025" (pág. 6) |
| Marco normativo y legal (Ley 19.628) | "Marco Normativo y Ético" (pág. 9-10) |
| Estado del arte: sistemas ALPR existentes | Investigar soluciones comerciales/académicas similares |

> 📚 Este capítulo requiere **investigación bibliográfica adicional**. El anteproyecto da la estructura, pero hay que profundizar cada tema con fuentes académicas.

---

### Fase 2 · Cómo y qué (Ronda 2)

Una vez definidos los objetivos (Intro) y el marco conceptual (Cap. 1), se puede escribir cómo se hizo y qué se construyó.

#### 📄 Cap. 2 — Metodología (`02_Metodologia`)

Este capítulo debe cubrir **dos ejes metodológicos** distintos, tal como indicó el profesor:

**A) Metodología de desarrollo** — Cómo se construyó la solución técnica.
**B) Metodología de gestión del proyecto** — Cómo se organizó y gestionó el trabajo entre ambos.

| Sección sugerida | Tipo | Insumo / Contenido |
|------------------|------|---------------------|
| Metodología de desarrollo: Prototipado Rápido | Desarrollo | "Metodología: Prototipado Rápido" (pág. 8) |
| Fases del ciclo de desarrollo (4 ciclos iterativos) | Desarrollo | Los 4 pasos descritos en pág. 8 |
| Metodología de gestión: Scrum / Kanban / la que usen | Gestión | Describir cómo se organizaron como equipo: sprints, reuniones, tablero de tareas, herramientas de seguimiento (GitHub Projects, Trello, etc.) |
| Roles y distribución del trabajo | Gestión | Quién hizo qué, cómo se dividieron las responsabilidades |
| Herramientas y tecnologías | Desarrollo | Python, YOLOv8, Flask/FastAPI, etc. — detallar las reales usadas |
| Diseño teórico de hardware | Desarrollo | "Diseño Teórico de la Infraestructura de Hardware" (pág. 8-9) |
| Alcance y limitaciones | Ambos | "Alcance y Limitaciones" (pág. 5-6) |

> 💡 **Tip del profesor:** La metodología de gestión demuestra que el proyecto se ejecutó de forma profesional y organizada. Incluyan evidencia concreta: capturas de tableros Kanban, actas de reuniones con el profesor, cronograma Gantt si lo tienen, etc.

#### 📄 Cap. 3 — Desarrollo de la Solución (`03_Desarrollo`)

| Sección sugerida | Insumo desde el anteproyecto |
|------------------|------------------------------|
| Arquitectura del sistema | Diseño real implementado (diagramas) |
| Modelo de IA: entrenamiento y dataset | "Desarrollo de Modelos de IA" (pág. 5) |
| Interfaz de simulación (app escritorio) | "Interfaz de Simulación Funcional" (pág. 5) |
| Panel administrativo web | "Panel Administrativo de Gestión" (pág. 5) |
| Lógica de control de acceso | "Lógica de Control de Acceso" (pág. 5) |
| Modelo de datos y BD | Diseño real de la base de datos |
| Diseño de infraestructura física | "Diseño Teórico de Infraestructura" (pág. 5) |

> 🔧 Este capítulo es el **más técnico y largo**. Consideren dividirlo en subsecciones claras y apoyarlo con diagramas, capturas de pantalla y fragmentos de código.

---

### Fase 3 · Evaluación (Ronda 3)

Solo se puede escribir esto cuando el desarrollo (Cap. 3) esté documentado.

#### 📄 Cap. 4 — Resultados y Discusión (`04_Resultados`)

| Sección sugerida | Insumo |
|------------------|--------|
| Plan de pruebas | Definir métricas: precisión, recall, F1, tiempo de respuesta |
| Resultados del modelo de IA | Métricas reales de entrenamiento/validación |
| Resultados de la simulación | Pruebas con cámara web, distintas condiciones |
| Evaluación económica | "Evaluación Económica" (pág. 10-13) — actualizar con datos reales |
| Discusión | Comparar con estado del arte, analizar limitaciones |

#### 📄 Conclusiones (`05_Conclusiones`)

| Sección | Contenido |
|---------|-----------|
| Cumplimiento de objetivos | Evaluar cada objetivo específico: ✅ cumplido / ⚠️ parcial |
| Aportes y contribuciones | Qué le aporta esto a la UTEM y al campo |
| Limitaciones | Ser honestos sobre qué no se logró |
| Trabajos futuros | Migración a Raspberry Pi, integración con sistemas UTEM, etc. |

---

### Fase 4 · Cierre (Ronda 4)

Estas secciones se escriben **al final** porque dependen de tener todo lo demás listo.

#### 📄 Resumen y Abstract (`06_Resumen`)

- **Resumen:** Síntesis de 1 página máximo (objetivo → método → resultados)
- **Abstract:** Traducción fiel al inglés del resumen
- **Palabras claves / Keywords:** 5-7 términos temáticos

> ✍️ Se escriben **después** de tener todos los capítulos listos, porque resumen el trabajo completo.

#### 📄 Glosario, Bibliografía y Anexos (`07_Finales`)

- **Glosario:** Ir recopilando términos técnicos a medida que se escriben los capítulos (YOLOv8, ALPR, Edge Computing, GPIO, CAPEX, OPEX, etc.)
- **Bibliografía:** Se va armando progresivamente en `finales/bibliografia.bib` cada vez que se cita una fuente nueva.
- **Anexos:** Manual de instalación, código fuente relevante, encuestas si las hay.

---

## 📆 Resumen del flujo completo

```
Semana 1 ──── Fase 0: Alineación + Fase 1: Introducción ∥ Marco Teórico
Semana 2 ──── Revisión cruzada Fase 1 + Fase 2: Metodología ∥ Desarrollo
Semana 3 ──── Revisión cruzada Fase 2 + Continuar Desarrollo (es largo)
Semana 4 ──── Fase 3: Resultados ∥ Conclusiones
Semana 5 ──── Revisión cruzada Fase 3 + Fase 4: Resumen, Glosario, Anexos
Semana 6 ──── Revisión final completa + Traspaso a LaTeX de todo
```

> ⏰ Los tiempos son orientativos. Lo importante es respetar el **orden de dependencias** y el flujo de revisión cruzada.

---

## ✅ Checklist de progreso

### Borradores
- [ ] `00_Introduccion_final.md`
- [ ] `01_MarcoTeorico_final.md`
- [ ] `02_Metodologia_final.md`
- [ ] `03_Desarrollo_final.md`
- [ ] `04_Resultados_final.md`
- [ ] `05_Conclusiones_final.md`
- [ ] `06_Resumen_final.md` (Resumen + Abstract)
- [ ] `07_Finales_final.md` (Glosario + Anexos)

### Traspaso a LaTeX
- [ ] `introduccion.tex`
- [ ] `capitulo1.tex` — Marco Teórico
- [ ] `capitulo2.tex` — Metodología
- [ ] `capitulo3.tex` — Desarrollo
- [ ] `capitulo4.tex` — Resultados
- [ ] `conclusiones.tex`
- [ ] `resumen.tex` + `abstract.tex`
- [ ] `glosario.tex` + `anexos.tex`
- [ ] `bibliografia.bib` (completo)

---

## 💡 Tips para trabajar con el asistente IA

1. **Un capítulo a la vez:** Pídeme que genere el borrador de un capítulo específico indicándome las secciones y el contenido que quieres.
2. **Dame contexto:** Cuando me pidas un capítulo, referencia el anteproyecto y cualquier borrador previo que sea relevante.
3. **Revisión iterativa:** Después de generar un borrador v1, puedes pedirme que revise y mejore secciones específicas.
4. **No tocar LaTeX aún:** Los `.tex` se editan solo cuando el borrador final está aprobado.
5. **Bibliografía progresiva:** Cada vez que mencionen una fuente nueva en un borrador, anótenla para ir armando el `.bib`.
