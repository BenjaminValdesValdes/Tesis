# 🗺️ Paso a Paso — Desarrollo del Informe de Trabajo de Título

**Proyecto:** Sistema de Control de Acceso Vehicular Automatizado mediante Reconocimiento de Patentes — UTEM Campus Ñuñoa

**Responsable del informe:** Ezequiel Molina
**Responsable del cronograma:** Benjamín Valdés (trabaja por su cuenta)

---

## 🔄 Protocolo de trabajo por capítulo

Cada capítulo sigue un ciclo de **5 etapas** que garantiza rigor académico, respaldo bibliográfico real y eficiencia:

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ETAPA 1 · BÚSQUEDA                                                    │
│  Gemini Deep Research + Connected Papers                                │
│  → Identificar fuentes relevantes (papers, libros, docs técnicos)       │
├─────────────────────────────────────────────────────────────────────────┤
│  ETAPA 2 · ANÁLISIS Y BORRADOR EN BRUTO                                │
│  NotebookLM                                                             │
│  → Subir las fuentes, verificar utilidad, identificar argumentos        │
│  → Redactar párrafos-borrador con las citas ya asociadas al documento   │
├─────────────────────────────────────────────────────────────────────────┤
│  ETAPA 3 · GESTIÓN BIBLIOGRÁFICA                                        │
│  Zotero + bibliografia.bib                                              │
│  → Importar cada fuente a Zotero (verificar metadatos reales)           │
│  → Exportar / sincronizar entradas al archivo .bib                      │
│  → Esto asegura que NINGUNA cita sea inventada por IA                   │
├─────────────────────────────────────────────────────────────────────────┤
│  ETAPA 4 · REDACCIÓN EN LaTeX                                           │
│  Asistente IA (yo) + anteproyecto como base                             │
│  → Tomo el anteproyecto + tus párrafos de NotebookLM + citas Zotero    │
│  → Genero el capítulo completo en .tex con \textcite y \parencite       │
├─────────────────────────────────────────────────────────────────────────┤
│  ETAPA 5 · REVISIÓN Y PULIDO                                           │
│  Tú revisas + me pides correcciones                                     │
│  → Verificar coherencia, profundidad, flujo narrativo                   │
│  → Compilar PDF y revisar formato visual                                │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 📚 Recomendaciones para cada etapa

### Etapa 1 — Búsqueda (Gemini Deep Research + Connected Papers)

1. **Empieza con los conceptos clave del capítulo** (ej: "YOLOv8 license plate detection", "Edge Computing IoT security", "ALPR systems").
2. **Gemini Deep Research:** Úsalo para obtener un panorama amplio y encontrar papers específicos. Pide que te entregue los DOI y títulos exactos.
3. **Connected Papers:** Ingresa un paper semilla relevante y explora el grafo de conexiones. Esto te revelará:
   - Papers fundacionales (los nodos grandes y antiguos)
   - Papers recientes del mismo tema (los nodos recientes conectados)
   - Revisiones/surveys que resumen el campo
4. **Guarda los PDFs** en una carpeta organizada por capítulo:
   ```
   fuentes/
   ├── cap1_marco_teorico/
   │   ├── yolov8_ultralytics_2023.pdf
   │   ├── edge_computing_survey_2022.pdf
   │   └── ...
   ├── cap2_metodologia/
   └── ...
   ```

> 💡 **Tip:** Prioriza papers con DOI y publicados en journals/conferencias reconocidas. Evita blogs o artículos sin peer-review como fuentes principales (pueden ser complementos, no pilares).

### Etapa 2 — Análisis y borrador (NotebookLM)

1. **Sube los PDFs del capítulo** a un notebook dedicado en NotebookLM.
2. **Haz preguntas dirigidas**, por ejemplo:
   - "¿Qué dice este paper sobre la precisión de YOLOv8 en detección de placas?"
   - "¿Cómo justifica este autor el uso de Edge Computing sobre Cloud?"
3. **Para cada argumento que quieras usar**, redacta un párrafo-borrador como este:

   ```
   [BORRADOR PARA SECCIÓN: Detección de Objetos con YOLOv8]

   Según [Autor, Año], la arquitectura YOLOv8 logra un mAP de 53.9%
   en el benchmark COCO, superando a su predecesor YOLOv5 en un 12%.
   Esto la posiciona como una opción viable para aplicaciones de
   tiempo real en dispositivos con recursos limitados.

   FUENTE: archivo "yolov8_ultralytics_2023.pdf", página 4
   CLAVE BIB PROPUESTA: jocher2023yolov8
   ```

4. **Acumula estos párrafos** en un documento temporal (`.md` o `.txt`) por capítulo antes de pasármelos.

> ⚠️ **Regla de oro:** NotebookLM te da las ideas y los argumentos. Zotero te da la cita verificada. YO te doy el LaTeX final. Ninguno de los tres reemplaza al otro.

### Etapa 3 — Gestión bibliográfica (Zotero → .bib)

1. **Importa cada fuente a Zotero** (por DOI, ISBN o manualmente).
2. **Verifica los metadatos:** autor, año, título, journal/conferencia, DOI. Si algo está mal, corrígelo en Zotero directamente.
3. **Usa Better BibTeX** (plugin de Zotero) para:
   - Generar claves tipo `jocher2023yolov8` automáticamente
   - Exportar al archivo `documento/finales/bibliografia.bib` de forma continua
4. **Configura la exportación automática** de Better BibTeX apuntando a:
   ```
   documento/finales/bibliografia.bib
   ```
   Así cada vez que agregues una fuente, el `.bib` se actualiza solo.

> 🔒 **Esto es tu seguro contra alucinaciones de IA.** Si la cita existe en Zotero con metadatos verificados, es real. Punto.

### Etapa 4 — Redacción LaTeX (conmigo)

Cuando me pidas generar un capítulo, proporcióname:

1. **Los párrafos-borrador** de NotebookLM (con la sección destino indicada)
2. **Las claves .bib** de Zotero que corresponden a cada cita
3. **La sección del anteproyecto** que sirve de base (ya la tengo en `anteproyecto_content.txt`)
4. **Instrucciones específicas** si quieres algún enfoque particular

Yo me encargo de:
- Reescribir con tono de informe final (no copiar el anteproyecto)
- Estructurar en `\section`, `\subsection` con flujo narrativo
- Usar `\textcite{}` y `\parencite{}` correctamente
- Generar el `.tex` listo para compilar

### Etapa 5 — Revisión

1. **Compila el PDF** con LaTeX Workshop
2. **Lee el capítulo completo** en el PDF — busca:
   - ¿Fluye bien de sección a sección?
   - ¿Las citas están donde corresponden?
   - ¿Falta profundidad en algún punto?
3. **Pídeme ajustes específicos** ("amplía la sección de OCR", "agrega una comparación con YOLOv5", etc.)

---

## 📋 Orden de capítulos — De arriba a abajo

El orden está diseñado para que **cada capítulo se alimente del anterior**. Esto significa que la información va quedando coherente y respaldada a medida que avanzas.

---

### 🟢 PASO 1 · Capítulo 1 — Marco Teórico

**¿Por qué primero?** Es la base conceptual de todo el informe. Define los conceptos que usarás en los capítulos posteriores. Si el marco teórico está sólido, el resto fluye naturalmente.

**Secciones a desarrollar:**

| # | Sección | Base del anteproyecto | Investigación adicional necesaria |
|---|---------|----------------------|-----------------------------------|
| 1.1 | Visión computacional y detección de objetos | Pág. 6 "Detección de Objetos mediante YOLOv8" | Historia de YOLO (v1→v8), benchmarks, comparativas |
| 1.2 | Arquitectura YOLOv8 en detalle | Pág. 6 (mención breve) | Paper original Ultralytics, backbone CSPDarknet, head architecture |
| 1.3 | OCR y reconocimiento de caracteres | Pág. 6 (mención al motor OCR) | Tesseract, EasyOCR, PaddleOCR — comparar alternativas |
| 1.4 | Reconocimiento automático de patentes (ALPR) | No está en anteproyecto | Estado del arte: OpenALPR, sistemas comerciales, papers de ALPR |
| 1.5 | Edge Computing vs Cloud Computing | Pág. 7 "Arquitectura Edge Computing" | Papers sobre latencia, privacidad, IoT edge |
| 1.6 | Formatos de patentes vehiculares en Chile | Pág. 6 "Gobierno de Chile, 2025" | Normativa vigente, formatos históricos y nuevos |
| 1.7 | Marco normativo: Ley 19.628 y protección de datos | Pág. 9-10 "Marco Normativo y Ético" | Ley 19.628, nueva Ley de Datos Personales, GDPR como referencia |

**Búsquedas recomendadas para Connected Papers:**
- Paper semilla: *"YOLOv8"* de Ultralytics → grafo de detección de objetos
- Paper semilla: *"Automatic License Plate Recognition survey"* → grafo de ALPR
- Paper semilla: *"Edge Computing for IoT"* → grafo de edge computing

**Producto:** `documento/capitulos/capitulo1.tex` completo con todas las citas

---

### 🟡 PASO 2 · Introducción

**¿Por qué después del Marco Teórico?** Parece contraintuitivo, pero la Introducción se escribe mejor cuando ya tienes claro el marco conceptual. Así puedes presentar el problema con más profundidad y hacer referencia precisa a los conceptos que se desarrollarán en el Cap. 1.

**Secciones a desarrollar:**

| # | Sección | Base del anteproyecto |
|---|---------|----------------------|
| — | Contexto y motivación | Pág. 3-4 "Contextualización y Definición del Problema" |
| — | Justificación del proyecto | Resumen Ejecutivo + Contextualización |
| — | Problema de investigación | Párrafo final de Contextualización (pág. 4) |
| — | Objetivo general | Pág. 4 "Objetivos del Proyecto" |
| — | Objetivos específicos | Pág. 4-5 "Objetivos Específicos" |
| — | Estructura del documento | Redactar de cero (describe cada capítulo) |

> ⚠️ **Importante:** La Introducción NO es copiar el anteproyecto. Se reescribe con tono de informe final, en pasado para lo que ya se hizo, y se agrega profundidad argumentativa.

**Búsquedas recomendadas:** Mínimas — la Introducción se nutre principalmente del anteproyecto y de lo que ya investigaste para el Marco Teórico.

**Producto:** `documento/capitulos/introduccion.tex` completo

---

### 🟡 PASO 3 · Capítulo 2 — Metodología

**¿Por qué aquí?** Una vez que el lector sabe qué se va a hacer (Intro) y entiende los conceptos (Cap. 1), necesita saber **cómo** se hizo.

**Este capítulo tiene DOS ejes** (indicación del profesor):

#### A) Metodología de Desarrollo

| # | Sección | Base del anteproyecto |
|---|---------|----------------------|
| 2.1 | Prototipado Rápido como metodología | Pág. 8 "Metodología: Prototipado Rápido" |
| 2.2 | Ciclos iterativos (4 fases) | Pág. 8 (los 4 pasos) |
| 2.3 | Herramientas y tecnologías utilizadas | Describir las reales: Python, YOLOv8, Flask/FastAPI, etc. |
| 2.4 | Diseño teórico de hardware | Pág. 8-9 "Diseño Teórico de la Infraestructura de Hardware" |

#### B) Metodología de Gestión del Proyecto

| # | Sección | Contenido |
|---|---------|-----------|
| 2.5 | Marco de gestión (Scrum/Kanban/la que usen) | Cómo se organizaron como equipo |
| 2.6 | Roles y distribución del trabajo | Quién hizo qué |
| 2.7 | Herramientas de seguimiento | GitHub Projects, Trello, etc. — con evidencia |

#### C) Alcance

| # | Sección | Base del anteproyecto |
|---|---------|----------------------|
| 2.8 | Alcance de la solución | Pág. 5-6 "Alcance y Limitaciones" |
| 2.9 | Limitaciones identificadas | Pág. 6 "Limitaciones Identificadas" |

**Búsquedas recomendadas:**
- *"Rapid Prototyping methodology software engineering"*
- *"Scrum methodology"* o la que realmente hayan usado
- Buscar referencias bibliográficas que respalden la elección de Prototipado Rápido

**Producto:** `documento/capitulos/capitulo2.tex` completo

---

### 🟠 PASO 4 · Capítulo 3 — Desarrollo de la Solución

**¿Por qué aquí?** El capítulo más técnico y largo. Requiere tener la Metodología clara porque describe **qué se construyó** siguiendo la metodología del Cap. 2.

| # | Sección | Base del anteproyecto |
|---|---------|----------------------|
| 3.1 | Arquitectura general del sistema | Diseño real implementado (diagrama) |
| 3.2 | Modelo de IA: dataset y entrenamiento | Pág. 5 "Desarrollo de Modelos de IA" |
| 3.3 | Pipeline de detección y OCR | Flujo: captura → YOLO → OCR → validación |
| 3.4 | Aplicación de escritorio (simulación) | Pág. 5 "Interfaz de Simulación Funcional" |
| 3.5 | Panel administrativo web | Pág. 5 "Panel Administrativo de Gestión" |
| 3.6 | Lógica de control de acceso | Pág. 5 "Lógica de Control de Acceso" |
| 3.7 | Modelo de datos y base de datos | Diseño real de BD (diagrama ER) |
| 3.8 | Diseño de infraestructura física | Pág. 5 "Diseño Teórico de Infraestructura" |

> 🔧 **Este capítulo requiere diagramas, capturas de pantalla y posiblemente fragmentos de código.** Prepáralos antes de pedirme la redacción LaTeX.

**Producto:** `documento/capitulos/capitulo3.tex` completo

---

### 🟠 PASO 5 · Capítulo 4 — Resultados y Discusión

**¿Por qué aquí?** Solo se puede evaluar cuando el desarrollo (Cap. 3) está documentado.

| # | Sección | Contenido |
|---|---------|-----------|
| 4.1 | Plan de pruebas | Definir métricas: precisión, recall, F1, tiempo de respuesta |
| 4.2 | Resultados del modelo de IA | Métricas reales de entrenamiento/validación, matrices de confusión |
| 4.3 | Resultados de la simulación | Pruebas con cámara web, distintas condiciones |
| 4.4 | Evaluación económica | Pág. 10-13 "Evaluación Económica" — actualizar con datos reales |
| 4.5 | Discusión | Comparar con estado del arte, analizar limitaciones |

**Producto:** `documento/capitulos/capitulo4.tex` completo

---

### 🔴 PASO 6 · Conclusiones

**¿Por qué al final?** Resumen del cumplimiento de objetivos. No se puede escribir sin tener todo lo anterior.

| # | Sección | Contenido |
|---|---------|-----------|
| — | Cumplimiento de objetivos | Evaluar cada objetivo específico: ✅ cumplido / ⚠️ parcial |
| — | Aportes y contribuciones | Qué aporta esto a la UTEM y al campo |
| — | Limitaciones | Ser honesto sobre qué no se logró |
| — | Trabajos futuros | Raspberry Pi real, integración con sistemas UTEM, etc. |

**Producto:** `documento/capitulos/conclusiones.tex` completo

---

### 🔴 PASO 7 · Resumen, Abstract y secciones finales

**¿Por qué último?** El Resumen sintetiza TODO el trabajo. Se escribe cuando ya existe todo.

| Sección | Archivo destino |
|---------|-----------------|
| Resumen (1 página máx.) | `preliminares/resumen.tex` |
| Abstract (traducción al inglés) | `preliminares/abstract.tex` |
| Glosario | `finales/glosario.tex` |
| Anexos | `finales/anexos.tex` |
| Bibliografía (verificar completitud) | `finales/bibliografia.bib` |

> 📝 **El glosario se va armando progresivamente** a medida que escribes cada capítulo. Cada vez que uses un término técnico nuevo (YOLOv8, ALPR, Edge Computing, GPIO, mAP, etc.), anótalo para que al final solo sea cuestión de compilarlo.

---

## ✅ Checklist de progreso

### Investigación (Etapas 1-3)
- [ ] Fuentes Cap. 1 — Marco Teórico (búsqueda + NotebookLM + Zotero)
- [ ] Fuentes Introducción (mínimas, principalmente anteproyecto)
- [ ] Fuentes Cap. 2 — Metodología (búsqueda + NotebookLM + Zotero)
- [ ] Fuentes Cap. 3 — Desarrollo (preparar diagramas + capturas)
- [ ] Fuentes Cap. 4 — Resultados (métricas reales del modelo)

### Redacción LaTeX (Etapas 4-5)
- [ ] `capitulo1.tex` — Marco Teórico ← **EMPEZAR AQUÍ**
- [ ] `introduccion.tex` — Introducción
- [ ] `capitulo2.tex` — Metodología
- [ ] `capitulo3.tex` — Desarrollo
- [ ] `capitulo4.tex` — Resultados
- [ ] `conclusiones.tex` — Conclusiones
- [ ] `resumen.tex` + `abstract.tex`
- [ ] `glosario.tex` + `anexos.tex`
- [ ] `bibliografia.bib` — verificación final de completitud

---

## 🛠️ Setup inicial recomendado (hacer una sola vez)

### Zotero + Better BibTeX
1. Instala **Better BibTeX** en Zotero: https://retorque.re/zotero-better-bibtex/
2. Crea una colección llamada `Tesis UTEM - ALPR`
3. Configura la exportación automática:
   - Click derecho en la colección → "Export Collection..."
   - Formato: "Better BibLaTeX" o "Better BibTeX"
   - Marca ✅ "Keep updated" (exportación automática)
   - Guarda en: `documento/finales/bibliografia.bib`
4. Configura el formato de claves en Better BibTeX:
   - Preferencias → Better BibTeX → Citation Keys
   - Patrón sugerido: `[auth:lower][year][shorttitle:lower:clean]`

### Carpeta de fuentes
```
Crea esta estructura en tu repositorio:
fuentes/
├── cap1_marco_teorico/
├── cap2_metodologia/
├── cap3_desarrollo/
├── cap4_resultados/
└── general/
```

### NotebookLM
- Crea un notebook por capítulo para mantener orden
- Nombre sugerido: "Tesis Cap1 - Marco Teórico", "Tesis Cap2 - Metodología", etc.

---

## 💡 Tips de eficiencia

1. **Un capítulo a la vez, completo.** No saltes entre capítulos. Termina el ciclo completo (búsqueda → NotebookLM → Zotero → LaTeX → revisión) antes de pasar al siguiente.

2. **Cuando me pidas el LaTeX, dame todo junto.** No me pidas sección por sección — es más eficiente que me des todos los párrafos-borrador del capítulo y yo genere el `.tex` completo de una vez.

3. **Usa Gemini Deep Research para preguntas amplias** ("¿cuál es el estado del arte de ALPR?") y **Connected Papers para profundizar** a partir de un paper específico que ya encontraste.

4. **En NotebookLM, sé específico.** En vez de "resúmeme este paper", pregunta "¿qué métricas de precisión reporta este paper para detección de placas?". Así tus párrafos-borrador serán más útiles.

5. **Agrega las fuentes del anteproyecto a Zotero primero.** Ya tienes estas citas en la bibliografía del anteproyecto — importalas a Zotero de inmediato:
   - Jocher et al. (2023) — Ultralytics YOLOv8
   - IBM (2024) — Edge Computing
   - Ley 19.628 — Protección de datos
   - Gobierno de Chile (2025) — Nuevas patentes

6. **No te preocupes por el cronograma.** Benjamín se encarga de eso. Tú enfócate 100% en el contenido del informe.

7. **Compila frecuentemente.** Después de cada capítulo, compila el PDF completo para asegurar que todo se ve bien y las citas se resuelven correctamente.

8. **El glosario es acumulativo.** Cada vez que escribas un término técnico nuevo en cualquier capítulo, agrégalo inmediatamente al glosario. No lo dejes para el final.

---

## 📆 Resumen del flujo

```
PASO 1 → Cap. 1 Marco Teórico     (el más intensivo en investigación)
PASO 2 → Introducción              (se nutre del Marco Teórico)
PASO 3 → Cap. 2 Metodología        (cómo se hizo)
PASO 4 → Cap. 3 Desarrollo         (qué se construyó — el más largo)
PASO 5 → Cap. 4 Resultados         (evaluación de lo construido)
PASO 6 → Conclusiones              (síntesis final)
PASO 7 → Resumen + Abstract + Finales (cierre del documento)
```

> 🎯 **Cada paso sigue el mismo ciclo:** Búsqueda → NotebookLM → Zotero → LaTeX (conmigo) → Revisión
