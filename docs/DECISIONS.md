# Decisiones

Lo que decidí sin preguntarte, por qué, y cómo deshacerlo. Fecha: 12 de noviembre de 2026.

## Alcance y fuentes

1. **Solo he escrito en este repositorio.** Los demás los he leído para describirlos, nada más.
2. **He leído también tus repositorios privados que nombraste** (`kessler`, `qec-lab`,
   `quant-path`, `compliance-tracer`, `arete`, `chess-trainer`), porque sin leerlos habría tenido
   que inventar. En cuatro de ellos `main` está vacío y el trabajo está en ramas `claude/...`: he
   leído esas ramas. Los otros seis privados, los que no nombraste, no los he abierto.
3. **Cada cifra de la web sale de un archivo del repositorio correspondiente**, no de la web
   anterior. Donde no coincidían he usado la del repositorio:
   - KAIROS: 17 agentes (README), no 21. 77 registros de decisión (archivos en `docs/adr/`).
     He quitado «< 2 s de latencia de voz» y el dato de microsegundos: no los encontré en el README.
   - gravity-lab: 31 casos de validación (README), no 40. He cambiado «orden medido 4.00» por el
     error de energía a 100 años (1,4e-11), que sí está en el README.
   - Chess trainer: 143 tests unitarios y 5 de extremo a extremo (`docs/STATUS.md`). He quitado
     «11 módulos» y «100 % de explicaciones verificadas».
   - Sympto+: la web decía «Completed» y daba por arreglada la condición de carrera. El README
     dice que está en pausa y que el arreglo es «the long-term solution». Corregido.
   - RAAN: todas las cifras son las de la ejecución del 12 de noviembre tras la revisión
     (maniobras 0,81 / 0,74 / 0,52 sobre 803 eventos).

## Web

4. **Solo modo oscuro.** La web anterior era clara por defecto y oscura si el sistema lo pedía.
   Pediste fondo oscuro y capturas que encajen con él, así que ahora es siempre oscura, con los
   mismos tonos que ya tenía el modo oscuro. Deshacer: recuperar el bloque `:root` claro del
   commit `87dbeb0`.
5. **Un solo acento: azul Cherenkov.** `#3D8BFF` para elementos gráficos (borde, subrayados,
   partículas) y `#5EC8FF` para texto pequeño (mejor contraste sobre negro). Sustituyen al
   naranja en los mismos sitios y en ninguno más. Los enlaces ya no son azul lavanda: son del
   color del texto con subrayado azul, para que haya un único azul.
6. **TraceGuard baja de primera línea.** Motivos: lleva parado desde finales de septiembre, no
   tiene usuarios, el repositorio es privado y no encaja con la nueva identidad (física e
   ingeniería). Queda en «More work» con una entrada honesta. He quitado «Founder of» del
   apartado About: con un MVP sin usuarios suena a más de lo que es. Sus cifras (100 % de
   precisión) ahora dicen sobre qué se midieron: 30 + 10 commits etiquetados por ti en un
   repositorio de demostración.
7. **Orden de proyectos:** RAAN, QEC Lab, gravity-lab, KAIROS, Chess trainer con ficha completa;
   Quant Path, TraceGuard, Sympto+ y ARETÉ en una lista corta («More work»). Razones en
   `REVISION_REPOS.md`.
8. **QEC Lab aparece como «In progress · no results yet»**, sin cifras ni enlace. El
   repositorio solo tiene el commit inicial. La descripción es la que me diste tú.
9. **Animación: nube de probabilidad del hidrógeno**, no la red cuántica. Es más ligera, se
   entiende sin explicación y es física real: cada partícula es una muestra de |ψ(n,l,m)|²
   obtenida por muestreo de rechazo de la función de onda exacta (polinomios de Laguerre y de
   Legendre asociados). Recorre seis orbitales (2p, 3d, 3p, 4d, 3d, 4f) cada 9 segundos, gira
   despacio y muestra el nombre del orbital. Sin librerías, 2.800 partículas en escritorio y
   1.700 en móvil, se detiene cuando no está en pantalla y queda fija si el sistema pide menos
   movimiento. Debajo, la ecuación de Schrödinger en pequeño.
10. **Capturas de RAAN con la luminosidad invertida.** La app de RAAN tiene interfaz clara y no
    tiene modo oscuro. En lugar de pegar tres rectángulos blancos, he invertido la luminosidad
    de las capturas conservando los colores (el script está descrito abajo). La web lo dice
    debajo de las capturas. No se ha editado ningún número ni ningún gráfico. Deshacer: volver
    a sacar las capturas con `web/scripts/shot.cjs` de `kessler` y sustituir los tres `.webp`.
11. **El informe técnico de RAAN está copiado en `assets/raan/`** para que el enlace funcione
    aunque `kessler` siga privado. Cuando regeneres el informe, vuelve a copiarlo (comando en
    `PASOS_PARA_DIEGO.md`).
12. **Los enlaces «Live site» y «Repository» de RAAN apuntan a direcciones que hoy dan 404**
    (repositorio privado, Pages sin activar). Los he dejado porque publicar RAAN es tu
    siguiente paso; si no vas a hacerlo ya, `PASOS_PARA_DIEGO.md` tiene el comando para
    quitarlos.
13. **Cada proyecto tiene un apartado «How it was made»** con qué hizo la IA y qué es tuyo.
    Lo he redactado a partir de lo que dice cada repositorio. En RAAN, KAIROS y Sympto+ el
    reparto está escrito en sus README. En gravity-lab, Chess trainer, Quant Path, ARETÉ y
    TraceGuard lo he deducido de la documentación y de tu encargo («decisiones, revisión,
    uso»): **revísalos tú**, porque solo tú sabes si son exactos.
14. **Nota del C1 (186).** Tu primer mensaje pedía no poner la cifra; el segundo ya no lo decía.
    He seguido el segundo: aparece en Certifications y en el CV. Quitarla: borrar «· score 186»
    en `index.html` y «(score 186, obtained at 16)» en los dos `cv/*.json`, y ejecutar `make cv`.
15. **Sección Writing:** solo hay cosas que existen y se pueden leer: el informe de RAAN, la
    explicación del criterio de captura (README de gravity-lab), los registros de decisión de
    KAIROS y la condición de carrera de Sympto+. No he puesto las 13 publicaciones de LinkedIn
    de RAAN porque aún no están publicadas.
16. **Clases particulares:** una frase en About y una entrada en el CV, sin detalles (asignaturas,
    número de alumnos), porque no los tengo.
17. **Rayas largas:** ninguna en `index.html`, `docs/LINKEDIN.md` ni en el CV. `make check` falla
    si vuelve a aparecer una (o el naranja).
18. **Navegación en móvil:** se ocultan «Education» y «Certifications» del menú (no caben en 360 px);
    las secciones siguen en la página.

## CV

19. **Generado con Python y `reportlab`** desde `cv/cv.en.json` y `cv/cv.es.json`. Un comando:
    `make cv`. Elegí `reportlab` porque no necesita LaTeX ni un navegador: se instala solo en un
    entorno virtual. El script falla si el CV pasa de una página o contiene una raya larga.
20. **Contenido:** mismo orden que la web. Incluye las tres solicitudes para 2027 como «en
    preparación». Sin foto, sin teléfono, sin dirección postal. Azul más oscuro que el de la web
    para que se imprima bien.

## LinkedIn

21. **Textos en inglés y en español.** Recomiendo el inglés como perfil principal.
22. **Mensajes de conexión de 200 caracteres como máximo**, que es el límite más estricto de
    las cuentas gratuitas. Ninguno pide nada.
23. **Recomiendo no poner ARETÉ en LinkedIn** y no añadir QEC Lab hasta que tenga resultados.

## Cómo se hicieron las capturas de RAAN

Desde la rama `claude/raan-pre-launch-review-8qqz4h` de `kessler`: `npm ci`, servidor de
desarrollo, y `node scripts/shot.cjs` sobre `/`, `/collision` y `/maneuvers` a 2×. Después,
por cada píxel, `c' = c + 1 - max(r,g,b) - min(r,g,b)` (invierte la luminosidad y conserva el
tono), reescalado al fondo `#101214`, recorte y exportación a WebP.

## Lo que no he podido comprobar

- Que `traceguard.eu`, `getsympto.app`, `didimacveg.github.io/gravity-lab/` y tu URL de LinkedIn
  respondan: la red de mi entorno no llega a esos dominios. Los enlaces son los que ya tenía la web.
- La web en un móvil real. La he probado en Chromium emulando un iPhone 13 y una pantalla de
  360 px: sin desbordes horizontales ni errores de consola.
- Los datos personales que no están en ningún repositorio: año del C1 (2025, heredado de la web
  anterior), nombre del instituto, CS50x «in progress», judo y clases. Lista en `PASOS_PARA_DIEGO.md`.
