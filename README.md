# Guía de Uso del Proyecto de Tesis en LaTeX (Norma UTEM)

¡Bienvenido al proyecto de LaTeX para tu Trabajo de Titulación (Tesis)! Este proyecto está estructurado modularmente siguiendo estrictamente la **Pauta para la Presentación de Trabajos de Titulación** de la Universidad Tecnológica Metropolitana (UTEM).

Dado que es tu primera vez trabajando con LaTeX, esta guía te dará el paso a paso para configurar tu entorno, compilar tu documento y escribir tu contenido de la manera más fácil y profesional posible.

---

## 1. Estructura del Proyecto

Para que tu trabajo sea ordenado, el proyecto está dividido en carpetas y archivos independientes. Solo debes editar el archivo correspondiente a la sección en la que estés trabajando:

*   **`main.tex`**: Es el archivo maestro. **Solo compilas este archivo**. Se encarga de unir todas las partes y de estructurar la paginación de la tesis.
*   **`configuracion/`**:
    *   `paquetes.tex`: Carga las herramientas y fuentes necesarias (no necesitas modificarlo).
    *   `formato.tex`: Define márgenes (4cm sup/izq, 2.5cm inf/der), tipografía Arial 12pt, interlineado 1.5, y estilos de títulos (no necesitas modificarlo).
    *   `comandos.tex`: **¡Modifica este archivo primero!** Aquí pones el título de tu tesis, tu nombre, profesor guía, carrera, facultad, año, etc.
*   **`preliminares/`**: Contiene las páginas anteriores al contenido formal (portada, derecho de autor, calificaciones, dedicatoria, agradecimientos, resumen y abstract).
*   **`capitulos/`**: Aquí escribes el desarrollo de tu tesis:
    *   `introduccion.tex`: Introducción formal.
    *   `capitulo1.tex` a `capitulo4.tex`: Plantillas para Marco Teórico, Metodología, Desarrollo y Resultados.
    *   `conclusiones.tex`: Conclusiones y trabajos futuros.
*   **`finales/`**:
    *   `bibliografia.bib`: Base de datos de tus referencias (libros, páginas web, artículos).
    *   `glosario.tex`: Definiciones de términos técnicos (optativo).
    *   `anexos.tex`: Manuales, códigos extensos o datos complementarios (optativo).
*   **`figuras/`**: Guarda aquí todas las imágenes (PNG, JPG, PDF) que vayas a insertar en tu tesis.

---

## 2. Configuración del Entorno de Trabajo (Windows)

Para poder compilar y generar tu PDF, necesitas instalar dos herramientas: un **distribuidor de LaTeX** (el motor) y un **editor** (la interfaz de escritura).

### Paso 1: Instalar el motor LaTeX
Recomendamos **MiKTeX** porque descarga automáticamente cualquier paquete adicional que tu documento requiera:
1. Descarga el instalador de [MiKTeX para Windows](https://miktex.org/download).
2. Ejecuta el instalador y sigue los pasos predeterminados.
3. Durante la instalación, cuando te pregunte *«Ask me first before installing missing packages»*, selecciona **«Always install missing packages on-the-fly»** (esto te ahorrará muchas alertas e interrupciones).

### Paso 2: Instalar el Editor LaTeX (Elige una opción)

#### Opción A: TeXstudio (Altamente recomendado para principiantes)
Es el editor clásico para LaTeX, muy estable y con visualizador de PDF incorporado.
1. Descarga e instala [TeXstudio](https://www.texstudio.org/).
2. Ábrelo, ve a **Opciones > Configurar TeXstudio**:
   * En **Compilación (Build)**, asegúrate de que el compilador predeterminado (*Default Compiler*) sea **PdfLaTeX** y el de bibliografía (*Default Bibliography*) sea **Biber**.
3. Abre el archivo `main.tex` en TeXstudio.
4. Para compilar y ver tu documento, presiona la tecla **F5** (o haz clic en el botón verde de doble flecha en la barra de herramientas). ¡Listo!

#### Opción B: Visual Studio Code
Si ya usas VS Code para programar:
1. Abre VS Code e instala la extensión **LaTeX Workshop**.
2. Instala la extensión de lenguaje **Spanish** si deseas corrector ortográfico.
3. Abre la carpeta del proyecto en VS Code. Al abrir `main.tex`, la extensión se configurará y compilará automáticamente al guardar.

#### Opción C: Overleaf (Opción Online, sin instalar nada)
Si prefieres trabajar en la nube o colaborar con otros:
1. Sube este proyecto en formato `.zip` a [Overleaf](https://www.overleaf.com/).
2. En la configuración de Overleaf (arriba a la izquierda), asegúrate de que el compilador sea **pdfLaTeX** y el motor de bibliografía esté en **Biber**.
3. Presiona el botón verde *Recompile*.

---

## 3. ¿Cómo escribir en tu Tesis? Guía Básica

LaTeX utiliza comandos sencillos para dar formato. Aquí tienes los ejemplos más comunes que necesitarás:

### A. Estructura de títulos y secciones
Dentro de los archivos de los capítulos (ej. `capitulo1.tex`), utiliza:
```latex
\section{Título de la Sección} % Crea secciones como 1.1, 1.2
\subsection{Título de la Subsección} % Crea subsecciones como 1.1.1, 1.1.2
\subsubsection{Título de la Subsubsección} % Crea subsubsecciones como 1.1.1.1
```

### B. Insertar imágenes
1. Guarda la imagen en la carpeta `figuras/` (por ejemplo, `mi_diagrama.png`).
2. Insértala en tu texto usando este código:
```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{figuras/mi_diagrama.png}
    \caption{Descripción clara de la ilustración.}
    \label{fig:mi_diagrama}
\end{figure}
```
*   `[H]` fuerza a que la imagen se quede exactamente donde la pusiste en el texto.
*   `width=0.8\textwidth` hace que la imagen ocupe el 80% del ancho del texto (puedes ajustar este valor).
*   `\label{fig:mi_diagrama}` es una etiqueta para que puedas citarla en el texto escribiendo: `"... como se detalla en la Figura \ref{fig:mi_diagrama}."`

### C. Crear tablas
Puedes diseñar tus tablas con herramientas visuales online como [Tables Generator](https://www.tablesgenerator.com/latex_tables) y luego pegar el código resultante. Asegúrate de estructurarlas así:
```latex
\begin{table}[H]
    \centering
    \caption{Título descriptivo de la tabla.}
    \begin{tabular}{|l|c|r|}
        \hline
        \textbf{Izquierda} & \textbf{Centro} & \textbf{Derecha} \\ \hline
        Fila 1 Col 1 & Fila 1 Col 2 & Fila 1 Col 3 \\ \hline
        Fila 2 Col 1 & Fila 2 Col 2 & Fila 2 Col 3 \\ \hline
    \end{tabular}
    \label{tab:mi_tabla}
\end{table}
```

### D. Citar bibliografía (Norma APA)
1. Abre el archivo `finales/bibliografia.bib`.
2. Añade tus fuentes en el formato BibTeX (puedes copiar el formato BibTeX directamente desde Google Académico haciendo clic en *Citar > BibTeX*). Ejemplo:
```bibtex
@book{sommerville2011,
  author    = {Sommerville, Ian},
  title     = {Ingeniería de software},
  year      = {2011},
  publisher = {Addison-Wesley}
}
```
3. Para citar esta fuente en tu texto (ej. en `capitulo1.tex`), usa:
   *   Si el autor es parte de la redacción:
       `Según \textcite{sommerville2011}, la ingeniería de software es...`
       *(Resultado: Según Sommerville (2011), la ingeniería de software es...)*
   *   Si la cita va al final del párrafo:
       `El diseño de sistemas debe ser estructurado \parencite{sommerville2011}.`
       *(Resultado: El diseño de sistemas debe ser estructurado (Sommerville, 2011).)*

---

## 4. El Flujo de Compilación (Por si compilas de forma manual)

Para que LaTeX resuelva correctamente los números de página, el índice, la bibliografía y las citas, se debe ejecutar una secuencia de compilación. En los editores esto ocurre de forma automática (o con presionar F5 en TeXstudio), pero el flujo técnico es:

1.  **PdfLaTeX**: Compila el documento principal y genera la estructura básica.
2.  **Biber**: Procesa el archivo de bibliografía `bibliografia.bib` y las citas.
3.  **PdfLaTeX**: Asocia la bibliografía al texto.
4.  **PdfLaTeX**: Resuelve las referencias cruzadas finales (índices y citas).

¡Felicidades! Tienes todo configurado para comenzar tu tesis de forma completamente profesional.

Comando para compilar en una sola linea:
```bash
latexmk -pdf main.tex
```
