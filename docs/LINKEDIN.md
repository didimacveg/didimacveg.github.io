# Textos para LinkedIn

Listos para copiar y pegar. Recomendación: perfil en **inglés** (lo leerán admisiones de
Holanda e ingenieros de fuera de España); debajo de cada bloque tienes la versión en español
por si prefieres esa o quieres crear el perfil secundario en español que LinkedIn permite.

Antes de pegar nada, lee cada frase y comprueba que es verdad tal cual. Si una frase de «qué
es mío» no describe lo que hiciste tú, cámbiala: en una entrevista te van a preguntar por ella.

---

## 1. Titular

**Inglés (recomendado; el límite del titular es de 220 caracteres):**

```
Physics and engineering student, Madrid | Building RAAN, an open orbital-data lab | Applying for 2027: Aerospace Engineering, Applied Physics
```

**Español:**

```
Estudiante de Bachillerato de Ciencias, Madrid | Construyo RAAN, un laboratorio abierto de datos orbitales | Solicitudes 2027: Ing. Aeroespacial, Física Aplicada
```

---

## 2. Acerca de

**Inglés:**

```
I'm 17 and in my final year of the Sciences Bachillerato in Madrid. In September 2027 I want to start in the Netherlands: Aerospace Engineering at TU Delft, Applied Physics at TU/e or Advanced Technology at Twente.

I build software on physics and mathematics, and I check it against measurement instead of against my own expectations.

What I have built so far:

• RAAN, an open lab on public orbital data: a digital twin of 20,152 catalogued objects, a collision-risk study on ESA's dataset and a manoeuvre detector. The naive baseline is reproduced first, and the result where my model did not beat it is published as it is.
• gravity-lab, an N-body simulator in C++ that reproduces Mercury's relativistic precession within 0.4 % of the accepted value.
• KAIROS, a local-first AI assistant with 17 agents and every design decision written down.
• In progress: QEC Lab, on neural decoders for quantum error correction.

How I work: I use AI coding assistants heavily and I say so. Much of the code in these projects was written by an AI. What is mine is the question, the rules each project must obey (public data only, baselines first, negative results published), the decisions and the responsibility for every claim.

Interests: space engineering, physics, machine learning and, in the long run, quantitative trading.

Also: Cambridge C1 Advanced, basic Chinese (YCT 2), black belt in judo, and I tutor school students.

Everything is at didimacveg.github.io. If you work in orbital dynamics, quantum error correction or quantitative research, I would be glad to hear what you would have done differently.
```

**Español:**

```
Tengo 17 años y estudio 2.º de Bachillerato de Ciencias en Madrid. En septiembre de 2027 quiero empezar en Holanda: Aerospace Engineering en TU Delft, Applied Physics en TU/e o Advanced Technology en Twente.

Construyo software con física y matemáticas, y lo compruebo contra medidas en lugar de contra lo que yo espero que salga.

Lo que he construido hasta ahora:

• RAAN, un laboratorio abierto con datos orbitales públicos: un gemelo digital de 20.152 objetos catalogados, un estudio de riesgo de colisión con el dataset de la ESA y un detector de maniobras. Primero se reproduce la línea base, y el resultado en el que mi modelo no la superó está publicado tal cual.
• gravity-lab, un simulador de N cuerpos en C++ que reproduce la precesión relativista de Mercurio con un 0,4 % de error respecto al valor aceptado.
• KAIROS, un asistente de IA que funciona en local, con 17 agentes y cada decisión de diseño por escrito.
• En curso: QEC Lab, sobre decodificadores neuronales para corrección de errores cuánticos.

Cómo trabajo: uso mucho los asistentes de programación de IA y lo digo. Gran parte del código de estos proyectos lo ha escrito una IA. Lo mío es la pregunta, las reglas que cada proyecto debe cumplir (solo datos públicos, líneas base primero, resultados negativos publicados), las decisiones y la responsabilidad de cada afirmación.

Intereses: ingeniería espacial, física, machine learning y, a largo plazo, trading cuantitativo.

Además: Cambridge C1 Advanced, chino básico (YCT 2), cinturón negro de judo y doy clases particulares.

Todo está en didimacveg.github.io. Si trabajas en dinámica orbital, corrección de errores cuánticos o investigación cuantitativa, me encantaría saber qué habrías hecho de otra manera.
```

---

## 3. Sección «Proyectos»

Para cada uno: **Nombre**, **Fechas**, **URL** y **Descripción**. Las URL de RAAN solo
funcionan cuando hayas hecho público el repositorio `kessler` (ver `PASOS_PARA_DIEGO.md`).

### 3.1 RAAN · Open Orbital Intelligence Lab

- Fechas: nov. 2026 – actualidad
- URL: `https://didimacveg.github.io/kessler/`

```
An open, reproducible lab on public orbital data. Research project, not for operational use.

• Orbital digital twin: 20,152 catalogued objects on a WebGL globe, propagated with SGP4. Propagator checked against Vallado's 666 reference vectors (max difference 3.5e-5 km).
• Collision research lab on ESA's Collision Avoidance Challenge dataset: naive forecast reproduced exactly (L = 0.694). My best model scores 0.627 on the test set but fails cross-validation, so I report it as a negative result, not as an improvement.
• Manoeuvre detection on 15 satellites, leave-one-satellite-out: F1 0.81 for the classifier, 0.74 for the physics baseline, 0.09 for chance.
• 6-page technical report.

How it was made: an AI coding assistant (Claude Code) wrote most of the code and a second, independent session reviewed it and re-ran every experiment. I set the question and the rules (public data only, baselines first, negative results published) and I answer for every claim.
```

Español:

```
Laboratorio abierto y reproducible con datos orbitales públicos. Proyecto de investigación, no apto para uso operativo.

• Gemelo digital orbital: 20.152 objetos catalogados en un globo WebGL, propagados con SGP4. Propagador comprobado con los 666 vectores de referencia de Vallado (diferencia máxima 3,5e-5 km).
• Laboratorio de colisiones con el dataset del Collision Avoidance Challenge de la ESA: predicción ingenua reproducida exactamente (L = 0,694). Mi mejor modelo obtiene 0,627 en test pero no supera la validación cruzada, así que lo publico como resultado negativo, no como mejora.
• Detección de maniobras en 15 satélites, dejando un satélite fuera en cada prueba: F1 0,81 el clasificador, 0,74 la línea base física, 0,09 el azar.
• Informe técnico de 6 páginas.

Cómo se hizo: un asistente de IA (Claude Code) escribió la mayor parte del código y una segunda sesión independiente lo revisó y repitió todos los experimentos. Yo fijé la pregunta y las reglas (solo datos públicos, líneas base primero, resultados negativos publicados) y respondo de cada afirmación.
```

### 3.2 QEC Lab

- Fechas: nov. 2026 – actualidad
- URL: ninguna todavía. **No lo añadas a LinkedIn hasta que haya algo que enseñar.** Cuando lo haya:

```
In progress. An open lab for quantum error correction: neural decoders compared with minimum-weight perfect matching (MWPM) on the surface code, under one protocol and with the baseline reproduced first. No results yet; they will be published whichever way they go. Built with an AI coding assistant; the question and the rules are mine.
```

Español:

```
En curso. Laboratorio abierto de corrección de errores cuánticos: decodificadores neuronales comparados con MWPM (emparejamiento perfecto de peso mínimo) en el código de superficie, con un único protocolo y reproduciendo primero la línea base. Aún sin resultados; se publicarán salgan como salgan. Construido con un asistente de IA; la pregunta y las reglas son mías.
```

### 3.3 gravity-lab

- Fechas: 2026
- URL: `https://didimacveg.github.io/gravity-lab/`

```
An N-body simulator of the Solar System in C++17, validated against astronomical measurement.

• Reproduces Mercury's relativistic perihelion precession: 42.81 arcsec per century against the accepted 42.98 (0.4 % error). The control without perturbations returns exactly zero.
• Four integrators compared. Yoshida 4 (symplectic, fourth order) keeps the energy error at 1.4e-11 over 100 years; explicit Euler drifts to 8 %.
• Black-hole module with a capture criterion based on the innermost stable circular orbit, and adaptive sub-stepping for close encounters.
• 31 validation cases run in CI; browser version online.

Built with an AI coding assistant. Mine: the decision to validate against measurement, the choice of what to test and the review of the results.
```

Español:

```
Simulador de N cuerpos del Sistema Solar en C++17, validado contra medidas astronómicas.

• Reproduce la precesión relativista del perihelio de Mercurio: 42,81 arcsec por siglo frente a los 42,98 aceptados (0,4 % de error). El control sin perturbaciones da exactamente cero.
• Cuatro integradores comparados. Yoshida 4 (simpléctico, cuarto orden) mantiene el error de energía en 1,4e-11 a 100 años; Euler explícito deriva hasta el 8 %.
• Módulo de agujero negro con un criterio de captura basado en la órbita circular estable más interna, y subdivisión adaptativa del paso en encuentros cercanos.
• 31 casos de validación en CI; versión web en línea.

Construido con un asistente de IA. Lo mío: la decisión de validar contra medidas, la elección de qué comprobar y la revisión de los resultados.
```

### 3.4 KAIROS

- Fechas: 2026
- URL: `https://github.com/didimacveg/kairos`

```
A local-first personal AI assistant that runs on my own machine: voice, semantic memory, desktop control and background tasks.

• 17 agents behind one contract, 300+ automated tests.
• Cloud reasoning with automatic fallback to a local model when there is no internet.
• The model picks actions from a closed whitelist; it never writes commands.
• It can propose changes to its own code, tested in a sandbox with no network. Nothing is merged without my approval.
• 77 decision records written as the decisions were made, including the wrong ones.

I designed the architecture and made the technical decisions; I used Claude as a pair programmer for the implementation.
```

Español:

```
Asistente personal de IA que funciona en mi propio ordenador: voz, memoria semántica, control del escritorio y tareas en segundo plano.

• 17 agentes bajo un mismo contrato, más de 300 tests automáticos.
• Razonamiento en la nube con paso automático a un modelo local cuando no hay internet.
• El modelo elige acciones de una lista cerrada; nunca escribe comandos.
• Puede proponer cambios a su propio código, probados en un entorno aislado sin red. Nada se fusiona sin mi aprobación.
• 77 registros de decisión escritos según se tomaban, incluidas las equivocadas.

Diseñé la arquitectura y tomé las decisiones técnicas; usé Claude como programador de apoyo para la implementación.
```

### 3.5 Chess trainer

- Fechas: 2026
- URL: ninguna (repositorio privado)

```
A local training app for deliberate chess practice with Stockfish and Maia (a network that plays like humans of a given rating): diagnostic, analysis of my own games, calculation, tactics, openings, pawn structures and endgames.

Every explanation is built from verifiable facts (engine, tablebase or board rules), and a test checks that each sentence cites one. 143 unit tests and 5 end-to-end tests.

Written by an AI coding assistant to my specification. Mine: what to train and how, and the rule that no explanation goes unchecked. Personal tool, repository private.
```

Español:

```
App local de entrenamiento de ajedrez con práctica deliberada, con Stockfish y Maia (una red que juega como humanos de un nivel dado): diagnóstico, análisis de mis partidas, cálculo, táctica, aperturas, estructuras de peones y finales.

Cada explicación se construye a partir de hechos verificables (motor, tablas de finales o reglas del tablero), y un test comprueba que cada frase cita uno. 143 tests unitarios y 5 de extremo a extremo.

Escrita por un asistente de IA según mi especificación. Lo mío: qué entrenar y cómo, y la regla de que ninguna explicación quede sin comprobar. Herramienta personal, repositorio privado.
```

### 3.6 Quant Path

- Fechas: nov. 2026 – actualidad
- URL: ninguna (repositorio privado)

```
My preparation programme for quantitative trading: a small web app for daily drills (mental arithmetic, sequences, probability, market making), a bank of 110 problems (101 with solutions verified by code) and nine sets of notes.

Produced with an AI coding assistant to my brief. Mine: the goal, the brief and doing the training. Not deployed yet.
```

Español:

```
Mi programa de preparación para trading cuantitativo: una pequeña app web de ejercicios diarios (cálculo mental, secuencias, probabilidad, market making), un banco de 110 problemas (101 con soluciones verificadas por código) y nueve temas de apuntes.

Hecho con un asistente de IA a partir de mis instrucciones. Lo mío: el objetivo, las instrucciones y hacer el entrenamiento. Aún sin desplegar.
```

### 3.7 TraceGuard

- Fechas: 2026 (en pausa)
- URL: `https://traceguard.eu`

```
An MVP that checks each firmware change against a product's safety rules. A language model proposes findings; a deterministic layer discards any whose rule does not exist or whose evidence is not literally in the diff.

On my own evaluation set (30 hand-labelled commits plus 10 held out, in a demo repository) it reached 100 % precision and recall. No external users. Paused.

Built with AI assistance. Mine: the product idea, the conversations with hardware engineers that shaped it and the evaluation design.
```

Español:

```
MVP que comprueba cada cambio de firmware frente a las reglas de seguridad de un producto. Un modelo de lenguaje propone hallazgos; una capa determinista descarta los que citan una regla inexistente o cuya evidencia no aparece literalmente en el cambio.

En mi propio conjunto de evaluación (30 commits etiquetados a mano y 10 reservados, en un repositorio de demostración) alcanzó un 100 % de precisión y de exhaustividad. Sin usuarios externos. En pausa.

Construido con ayuda de IA. Lo mío: la idea de producto, las conversaciones con ingenieros de hardware que le dieron forma y el diseño de la evaluación.
```

### 3.8 Sympto+

- Fechas: 2026 (en pausa)
- URL: `https://github.com/didimacveg/getsympto`

```
A web app that turns a symptom description and an interactive body map into structured guidance in four languages. An information tool, never a diagnosis. Anonymous by default.

It reached a production MVP and is paused: payment providers rejected a health-adjacent product, which taught me that technical feasibility does not guarantee business feasibility.

Claude implemented parts of the code. Mine: the product, the architecture and the body-map design.
```

Español:

```
Web que convierte una descripción de síntomas y un mapa corporal interactivo en orientación estructurada en cuatro idiomas. Herramienta de información, nunca de diagnóstico. Anónima por defecto.

Llegó a MVP en producción y está en pausa: los proveedores de pago rechazaron un producto relacionado con la salud, y aprendí que la viabilidad técnica no garantiza la viabilidad de negocio.

Claude implementó partes del código. Lo mío: el producto, la arquitectura y el diseño del mapa corporal.
```

### 3.9 ARETÉ

Recomendación: **no lo pongas en LinkedIn**. Es una herramienta personal de estudio, sin
interés para quien lee tu perfil. Está en la web, en «More work», con una línea. Si aun así
lo quieres:

```
An offline-first app I use to plan and audit my own study: timed commitments, a per-subject log of exams and repeated mistakes, and a weekly review. Written by an AI coding assistant; the rules of the system are mine.
```

---

## 4. A quién conectar: 15 tipos de perfil

Cómo usarlo: busca el perfil, pulsa **Conectar → Añadir una nota** y pega el mensaje cambiando
lo que va entre corchetes. Todos caben en 200 caracteres, el límite más estricto que aplica LinkedIn a la nota en las
cuentas gratuitas. Diez por semana como mucho, y siempre
habiendo leído antes algo de la persona: si no puedes rellenar el corchete con algo concreto,
no envíes el mensaje.

Regla: nunca pidas un favor en la nota de conexión. Si aceptan, da las gracias y, pasados
unos días, haz **una** pregunta concreta.

| # | Tipo de perfil | Cómo encontrarlo |
|---|---|---|
| 1 | Ingenieros de dinámica orbital / flight dynamics de GMV | Búsqueda: `GMV flight dynamics`, `GMV space debris` |
| 2 | Ingenieros de Space Situational Awareness (Neuraspace, LeoLabs, Indra, Deimos) | `space situational awareness engineer` |
| 3 | Personal de la ESA Space Debris Office y de ESOC | `ESA Space Debris Office`, `ESOC flight dynamics` |
| 4 | Autores del Collision Avoidance Challenge de la ESA y del benchmark de maniobras | Nombres en los artículos que cita el informe de RAAN |
| 5 | Estudiantes de BSc Aerospace Engineering de TU Delft | Filtro Universidad: `Delft University of Technology` + `Aerospace Engineering` |
| 6 | Estudiantes españoles en TU Delft, TU/e o Twente | Mismo filtro + ubicación de origen España |
| 7 | Miembros de equipos estudiantiles de Delft (DARE, Delfi Space) | `Delft Aerospace Rocket Engineering`, `Delfi` |
| 8 | Estudiantes de Applied Physics de TU/e | Filtro Universidad: `Eindhoven University of Technology` |
| 9 | Estudiantes de Advanced Technology de Twente | Filtro Universidad: `University of Twente` + `Advanced Technology` |
| 10 | Investigadores y doctorandos de QuTech (Delft) en corrección de errores cuánticos | `QuTech quantum error correction` |
| 11 | Ingenieros de empresas de computación cuántica en Europa (IQM, Qilimanjaro, Quantum Inspire) | `quantum error correction engineer`, `Qilimanjaro` |
| 12 | Ingenieros de startups espaciales españolas (PLD Space, Sateliot, Satlantis, FOSSA) | Nombre de la empresa + `engineer` |
| 13 | Quant traders e investigadores en Ámsterdam (Optiver, IMC, Flow Traders, Da Vinci) | Empresa + `trader` o `quantitative researcher` |
| 14 | Antiguos alumnos de institutos de Madrid que estudian ingeniería o física en Holanda | Filtro Universidad holandesa + `Madrid` |
| 15 | Profesores e investigadores de astrodinámica y física en universidades españolas (UPM, UC3M, UAM) | `astrodynamics UPM`, `space debris UC3M` |

### Mensajes

**1. Dinámica orbital en GMV**

```
Hola, [nombre]. Tengo 17 años y he construido RAAN, un laboratorio abierto con datos orbitales públicos. Sigo el trabajo de GMV en [tema] y me gustaría tenerte en mi red. Gracias.
```

**2. Ingenieros de SSA**

```
Hi [name]. I'm 17 and built RAAN, an open lab on public orbital data (SGP4 twin, conjunction study). Your work on [topic] at [company] is what I'd like to learn from. Glad to connect.
```

**3. ESA Space Debris Office / ESOC**

```
Hi [name]. I'm a 17-year-old student in Madrid. I reproduced the baseline of ESA's Collision Avoidance Challenge in an open project and follow your office's work. Glad to connect.
```

**4. Autores de los datasets que uso**

```
Hi [name]. I'm a student using your [dataset/paper] in RAAN, an open orbital-data project, with credit and licence respected. Thank you for publishing it. I'd be glad to connect.
```

**5. Estudiantes de Aerospace Engineering en TU Delft**

```
Hi [name]. I'm 17, from Madrid, applying to Aerospace Engineering at TU Delft for 2027. I'd like to follow how the first year really is. Glad to connect.
```

**6. Españoles en TU Delft, TU/e o Twente**

```
Hola, [nombre]. Estoy en 2.º de Bachillerato en Madrid y quiero empezar en [universidad] en 2027. Me ayudaría mucho ver el camino de alguien que ya lo ha hecho. Gracias por aceptar.
```

**7. Equipos estudiantiles de Delft**

```
Hi [name]. I'm applying to TU Delft AE for 2027 and [team] is one of the reasons. I build orbital and physics software on my own for now. Glad to connect and follow the team's work.
```

**8. Estudiantes de Applied Physics en TU/e**

```
Hi [name]. I'm 17, from Madrid, applying to Applied Physics at TU/e for 2027. I'd like to see what the programme looks like from the inside. Glad to connect.
```

**9. Estudiantes de Advanced Technology en Twente**

```
Hi [name]. I'm 17, from Madrid, and Advanced Technology at Twente is one of my options for 2027. I'd like to follow how students combine physics and engineering there. Glad to connect.
```

**10. Investigadores de QuTech**

```
Hi [name]. I'm a 17-year-old student starting an open project on neural decoders vs MWPM for the surface code. I read your work on [topic] and would be glad to connect.
```

**11. Empresas de computación cuántica**

```
Hi [name]. I'm a student in Madrid starting an open project on surface-code decoding. I follow what [company] is doing on [topic] and would be glad to have you in my network.
```

**12. Startups espaciales españolas**

```
Hola, [nombre]. Tengo 17 años y construyo software de física y órbitas (RAAN, un laboratorio abierto de datos orbitales). Sigo lo que hace [empresa] y me gustaría conectar. Gracias.
```

**13. Quant traders e investigadores**

```
Hi [name]. I'm 17, heading to study physics or engineering in the Netherlands in 2027, and I train probability and mental maths with trading as a long-term goal. Glad to connect.
```

**14. Antiguos alumnos de Madrid en Holanda**

```
Hola, [nombre]. Soy de Madrid, estoy en 2.º de Bachillerato y quiero estudiar en Holanda en 2027. Ver que alguien de aquí lo ha hecho me anima. Me gustaría conectar. Gracias.
```

**15. Profesores e investigadores en España**

```
Hola, [nombre]. Soy estudiante de Bachillerato en Madrid y he construido un laboratorio abierto de datos orbitales con resultados reproducibles. Sigo su trabajo en [tema]. Gracias.
```
