# Revisión de repositorios

Fecha: 12 de noviembre de 2026 (nombres actualizados el 13 de noviembre: QEC Lab pasa a llamarse
Syndrome Lab, repositorio `syndrome-lab`; el estado de `kessler` está en `PASOS_PARA_DIEGO.md`). No he cambiado nada en ningún repositorio que no sea este:
esto es solo la lista de qué arreglar.

**Qué he podido leer y qué no**

- Repositorios **públicos** en `github.com/didimacveg`: `didimacveg.github.io`, `gravity-lab`,
  `kairos` y `getsympto`. Leídos enteros (README, licencias, documentación, workflows).
- Repositorios **privados** que nombraste, leídos solo para describirlos en la web: `kessler`
  (RAAN), `syndrome-lab`, `quant-path`, `compliance-tracer` (TraceGuard), `arete` y `chess-trainer`.
- **No leídos:** tus otros seis repositorios privados, los que no nombraste. No aparecen en
  la web ni opino sobre ellos, y no pongo aquí sus nombres porque este archivo es público.
- **No he podido comprobar desde aquí:** la descripción, los temas («topics») y la web que
  cada repositorio muestra en GitHub (mi acceso a la API está limitado a este repositorio), ni
  si `traceguard.eu`, `getsympto.app` y `didimacveg.github.io/gravity-lab/` responden (la red
  de mi entorno no llega a esos dominios). Abajo te dejo los valores que deberían tener y los
  comandos para ponerlos.

Los comandos usan `gh`, la herramienta oficial de GitHub. Si no la tienes:

```bash
sudo apt install -y gh
```

```bash
gh auth login
```

---

## Qué enseñar y en qué orden

| Orden | Proyecto | Repositorio | Dónde va en la web | Motivo |
|---|---|---|---|---|
| 1 | RAAN | `kessler` (privado) | Destacado, arriba | El más sólido: resultados reproducibles, un resultado negativo bien explicado e informe. **Hay que hacerlo público.** |
| 2 | Syndrome Lab | `syndrome-lab` (privado hasta finales de noviembre) | Segundo, como «in progress» | Sin cifras ni enlace hasta que se publiquen los resultados y el informe. |
| 3 | gravity-lab | público | Ficha completa | Física validada contra medidas y demo en línea. Es el que mejor encaja con Applied Physics. |
| 4 | KAIROS | público | Ficha completa | Es el más grande y el único en el que la arquitectura es claramente tuya. |
| 5 | Chess trainer | `chess-trainer` (privado) | Ficha completa | Bien probado; la idea de «explicaciones verificadas» es buena. |
| 6 | Quant Path | `quant-path` (privado) | «More work», una entrada | Es preparación personal, no un producto. |
| 7 | TraceGuard | `compliance-tracer` (privado) | «More work», una entrada | Baja de primera línea: ver `DECISIONS.md`, decisión 6. |
| 8 | Sympto+ | `getsympto` (público) | «More work», una entrada | En pausa y con un fallo conocido sin arreglar. |
| 9 | ARETÉ | `arete` (privado) | «More work», una entrada | Herramienta personal. |

**Mejor no enseñar:** el resto de tus repositorios privados (material de apoyo de TraceGuard,
apuntes y preparación de solicitudes). Déjalos privados.

---

## 1. `kessler` (RAAN) · privado · prioridad máxima

La web enlaza a su repositorio y a su página, así que **esos dos enlaces dan error 404 hasta
que lo publiques**.

1. `main` solo contiene un README con una palabra. Todo el trabajo está en la rama
   `claude/raan-pre-launch-review-8qqz4h`, sin fusionar. Sigue los pasos 1 a 3 de su propio
   `docs/PASOS_PARA_DIEGO.md` (decidir sobre tu correo en el historial, hacerlo público,
   activar Pages, fusionar).
2. Después, descripción, web y temas:

```bash
gh repo edit didimacveg/raan --description "RAAN: open, reproducible lab on public orbital data. Digital twin, collision-risk study on ESA's dataset, manoeuvre detection. Research project, not for operational use." --homepage "https://didimacveg.github.io/raan/" --add-topic space-debris --add-topic orbital-mechanics --add-topic sgp4 --add-topic space-situational-awareness --add-topic machine-learning --add-topic reproducible-research --add-topic threejs
```

3. El nombre del repositorio (`kessler`) coincide con una librería de la ESA sobre el mismo
   tema. Plantéate renombrarlo a `raan` **antes** de publicarlo y de compartir enlaces (GitHub
   redirige el nombre antiguo, pero la dirección de Pages cambia y habría que actualizar esta web).
4. Borra la rama antigua `claude/epic-volta-jjkxwt` cuando hayas fusionado la de revisión.
5. Su `STATUS.md` avisa de que las páginas de la app aún tienen rayas largas en el texto.
6. Pendiente tuyo según su documentación: el correo al autor del benchmark de maniobras.

## 2. `gravity-lab` · público

Es el que está mejor. Arreglos pequeños:

1. **Cifras que no coinciden.** El README dice «31 validation cases»; `ORDEN_DE_TRABAJO.md` dice
   «los 17 tests pasan»; la web antigua decía 40. He puesto 31 en la web y el CV (lo que dice el
   README). Compruébalo ejecutando los tests y deja la misma cifra en todas partes.
2. **Archivos de trabajo en la raíz, en español y sin acentos:** `GITHUB.md`,
   `ORDEN_DE_TRABAJO.md`, `SETUP_WSL.md`. Muévelos a `docs/` o bórralos: lo primero que ve un
   visitante debe ser código, README y licencia.
3. **`.vscode/` está subido.** Quítalo y añádelo a `.gitignore`, salvo que lo quieras a propósito.
4. **Raya larga** en el README («Diego Macías Vega — github.com/...»). Cámbiala por «·».
5. **El README no dice que usaste IA.** La web sí. Añade una sección «How it was made» de dos
   frases para que digan lo mismo.
6. `web/simulador.html`: nombre en español en un repositorio en inglés. Opcional: `simulator.html`
   (si lo cambias, revisa `pages.yml`).
7. Falta una captura o GIF del simulador al principio del README.
8. Descripción, web y temas:

```bash
gh repo edit didimacveg/gravity-lab --description "N-body simulator of the Solar System in C++17, validated against astronomical measurement. Reproduces Mercury's relativistic precession." --homepage "https://didimacveg.github.io/gravity-lab/" --add-topic n-body --add-topic numerical-methods --add-topic symplectic-integrator --add-topic general-relativity --add-topic physics-simulation --add-topic cpp17
```

Licencia: MIT, correcta. Enlaces del README: sin enlaces rotos entre archivos.

## 3. `kairos` · público

1. **El vídeo del principio** es un enlace suelto a `user-attachments`. Comprueba en la página del
   repositorio que se reproduce; si no, sustitúyelo por una captura.
2. **Cifras que no coinciden.** El README dice «Seventeen agents» y «76+ documented build phases»;
   la web antigua decía 21 agentes; en `docs/adr/` hay 77 registros. He puesto 17 agentes y 77
   registros. Unifícalo en el README.
3. **Numeración de los ADR con huecos** (faltan 0016, 0018 y 0073). Añade una línea en
   `docs/adr/README.md` que lo explique, o parecerá que se han borrado.
4. **Rayas largas** en el README (hay varias).
5. **Documentos que no pintan nada en un repositorio público:** `docs/GETSYMPTO.md` (es de otro
   proyecto) y `docs/PENDIENTE.md`. Revísalos y quítalos si son notas internas.
6. **Sin CI:** el README presume de más de 300 tests, pero no hay ningún workflow que los ejecute
   ni insignia que lo demuestre. Un workflow que lance los tests unitarios y de arranque sería la
   mejora con más efecto.
7. README en inglés y ADR en español: dilo en una línea del README («Decision records are in
   Spanish»).
8. Descripción y temas:

```bash
gh repo edit didimacveg/kairos --description "Local-first personal AI assistant: voice, semantic memory, whitelisted desktop control and sandboxed self-modification." --add-topic ai-assistant --add-topic local-first --add-topic fastapi --add-topic pgvector --add-topic ollama --add-topic nextjs --add-topic multi-agent
```

Licencia: MIT, correcta. Enlaces del README: sin enlaces rotos entre archivos.

## 4. `getsympto` (Sympto+) · público

Es el más flojo de los públicos. Dos opciones: arreglar lo siguiente o **volverlo privado**. Si
no vas a retomarlo, yo lo haría privado y quitaría su enlace de la web (está en «More work» y en
«Writing»).

1. **Licencia contradictoria.** El repositorio es público, pero `LICENSE` dice «software
   propietario y confidencial. Queda prohibida su copia». O lo haces privado o cambias la licencia
   (MIT, o «source available» si quieres que se lea pero no se reutilice). Tal como está da mala
   imagen.
2. **Nombre.** Tú lo llamas «Sympto+», el README «GetSympto+», el repositorio `getsympto` y el
   dominio `getsympto.app`. Elige uno. En la web he puesto «Sympto+», como me pediste.
3. **Estado.** El README dice que está en pausa, con la integración de Stripe sin terminar y con
   la condición de carrera del límite diario **sin arreglar**. La web antigua decía «Completed» y
   daba el arreglo por hecho; lo he corregido. Pon el estado en la primera línea del README.
4. **`getsympto.app`:** comprueba que sigue funcionando. Si el dominio ha caducado, quita el
   enlace del README.
5. **Restos de plantilla:** `public/next.svg`, `vercel.svg`, `file.svg`, `globe.svg`,
   `window.svg`; un `layout.tsx` suelto en la raíz; `CLAUDE.md` y `AGENTS.md`.
6. **Sin tests**, y el propio README lo reconoce. No hace falta arreglarlo si queda en pausa, pero
   no lo presentes como terminado.
7. Descripción y temas, si se queda público:

```bash
gh repo edit didimacveg/getsympto --description "Paused MVP: symptom description and body map to structured health information in four languages. An information tool, not a diagnosis." --add-topic nextjs --add-topic supabase --add-topic i18n --add-topic health-information
```

## 5. `didimacveg.github.io` · público (este)

Hecho en esta sesión: README, `.gitignore`, `Makefile`, CV y documentación. Te queda:

1. Fusionar la rama en `main` (`PASOS_PARA_DIEGO.md`, paso 2).
2. Descripción y web:

```bash
gh repo edit didimacveg/didimacveg.github.io --description "Personal site of Diego Macías Vega: physics and engineering projects." --homepage "https://didimacveg.github.io" --add-topic portfolio
```

3. No tiene licencia. Para una web personal es normal; no hace falta.

## 6. Perfil de GitHub

1. Fija («pin») en este orden: `kessler` (cuando sea público), `gravity-lab`, `kairos`. Se hace en
   <https://github.com/didimacveg> → **Customize your pins**.
2. En el perfil: nombre completo, «Madrid», enlace a `https://didimacveg.github.io` y una
   biografía de una línea: `Physics and engineering student. Building RAAN, an open orbital-data lab.`
3. En <https://github.com/settings/emails>, marca **Keep my email addresses private**.

## 7. Privados que aparecen en la web

No hace falta publicarlos. Si algún día lo haces:

- `chess-trainer`: no tiene archivo de licencia, e incluye Maia-3, que es AGPL-3.0. Publicarlo
  obliga a publicarlo como AGPL. Su README está en español.
- `quant-path` y `arete`: el trabajo está en ramas `claude/...` sin fusionar y `main` está vacío.
  README en español.
- `compliance-tracer`: tiene en la raíz `dashboard-actual.tar.gz`, `fix-pem.sh` e `index.html`,
  que habría que quitar antes.
