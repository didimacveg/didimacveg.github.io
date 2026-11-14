# Pasos para Diego

Lo que depende de ti, en orden. Comandos para terminal **Ubuntu/WSL**: copia cada bloque tal cual.

Revisión del 14 de noviembre de 2026. El trabajo está en la rama
`claude/cv-honesty-web-updates-9wfh27`, con un pull request abierto contra `main`. **La web
pública no cambia hasta que lo fusiones** (paso 3).

> **Importante: este pull request se fusiona DESPUÉS de renombrar el repositorio `kessler` a
> `raan`** (paso 2). La web ya enlaza a `https://didimacveg.github.io/raan/` y a
> `https://github.com/didimacveg/raan`; si lo fusionas antes, esos dos botones de la ficha de
> RAAN darán 404 hasta que hagas el renombrado.

Qué cambia en esta revisión:

- **Competencias, en la web y en los dos CV:** ahora dicen la verdad sobre cómo trabajas.
  «How I build»: diseñas, diriges, revisas y pruebas proyectos hechos con Claude Code; todavía
  no sabes escribir estos programas desde cero y aprendes Python y algoritmos a la vez. Python
  figura como «beginner, learning». C++17, TypeScript, FastAPI, PostgreSQL y Docker pasan a
  «Used in AI-assisted projects». «Concepts I can explain» incluye solo lo que explican los
  `DEFENSA.md` de `raan` y `syndrome-lab` (los únicos dos que existen). La integración numérica
  **se ha quitado**: ningún `DEFENSA.md` la explica. Si escribes uno para `gravity-lab`, se puede
  volver a poner.
- **Capturas:** gravity-lab (simulador web, versión actual) y el entrenador de ajedrez (inicio y
  un ejercicio de táctica, de `docs/screenshots/despues/`). KAIROS no tiene capturas en su
  repositorio y Sympto+ no lleva imagen.
- **RAAN:** enlaces a `raan` en lugar de `kessler` (web, `docs/LINKEDIN.md`, `docs/REVISION_REPOS.md`).
- **LinkedIn:** el párrafo «How I work» / «Cómo trabajo» de `docs/LINKEDIN.md`, con el mismo
  texto honesto. Cópialo a tu perfil.

---

## 1. Lee lo que ha cambiado (10 minutos)

```bash
cd ~/didimacveg.github.io && git fetch origin && git checkout claude/cv-honesty-web-updates-9wfh27 && git pull
```

```bash
make serve
```

Abre <http://localhost:8000>. Comprueba sobre todo el apartado About (párrafo «How I build» y
la columna de la derecha) y los dos CV: `cv/Diego_Macias_Vega_CV_EN.pdf` y
`cv/Diego_Macias_Vega_CV_ES.pdf`. Lee cada frase y confirma que es verdad tal cual: en una
entrevista te pueden pedir que expliques cualquiera de los «Concepts I can explain».

## 2. Renombra `kessler` a `raan` (5 minutos, ANTES del paso 3)

```bash
gh repo rename raan --repo didimacveg/kessler --yes
```

O en la web: <https://github.com/didimacveg/kessler/settings> → **Repository name** → `raan`
→ **Rename**.

GitHub redirige el repositorio antiguo al nuevo, pero **GitHub Pages no**: la web de RAAN pasa
a `https://didimacveg.github.io/raan/` y la dirección `/kessler/` deja de funcionar. La
compilación usa rutas relativas (`base: './'` en `web/vite.config.ts`), así que no hay que
tocar nada para que funcione en la ruta nueva; si Pages no se vuelve a desplegar solo, lanza
el flujo de despliegue a mano desde la pestaña **Actions** del repositorio.

Si el repositorio sigue privado y ya quieres publicarlo:

```bash
gh repo edit didimacveg/raan --visibility public --accept-visibility-change-consequences
```

Actualiza tu copia local para que apunte al nombre nuevo:

```bash
mv ~/kessler ~/raan && cd ~/raan && git remote set-url origin https://github.com/didimacveg/raan.git
```

Dentro de `raan` quedan referencias a `kessler` (`web/src/brand.ts`, `raan/brand.py`, el
`README.md`, los informes y el PDF técnico, que enlaza a `github.com/didimacveg/kessler`). Esa
dirección redirige, pero conviene cambiarlas en ese repositorio y regenerar el informe (paso 8).

Comprueba en una ventana privada (Ctrl+Mayús+N):

- <https://github.com/didimacveg/raan>
- <https://didimacveg.github.io/raan/>

## 3. Fusiona el pull request (2 minutos, DESPUÉS del paso 2)

```bash
cd ~/didimacveg.github.io && git fetch origin && git checkout main && git pull origin main && git merge --no-ff origin/claude/cv-honesty-web-updates-9wfh27 -m "Merge honest skills, RAAN rename and project screenshots" && git push origin main
```

O en el navegador: <https://github.com/didimacveg/didimacveg.github.io/pulls> → el pull
request → **Merge pull request** → **Confirm merge**.

Espera un par de minutos y abre <https://didimacveg.github.io>. Si ves la versión antigua,
recarga con Ctrl+F5.

## 4. Comprueba los enlaces que yo no alcanzo (5 minutos)

Con la web ya publicada, pulsa cada uno:

- [ ] RAAN: «Live site» y «Repository» (llevan a `raan`; paso 2).
- [ ] gravity-lab: «Live simulator» (<https://didimacveg.github.io/gravity-lab/>).
- [ ] <https://traceguard.eu>
- [ ] LinkedIn (botón de Contact y enlace del CV).
- [ ] El correo: envíate uno desde el enlace.

Y mírala en tu móvil: que la nube se mueva con fluidez y nada se salga por la derecha. Solo la
he probado en un móvil emulado de 390 px.

## 5. Actualizar el CV (cuando haga falta)

Requisitos, una sola vez:

```bash
sudo apt update && sudo apt install -y python3-venv make
```

Edita `cv/cv.en.json` (inglés) y `cv/cv.es.json` (español) y ejecuta:

```bash
cd ~/didimacveg.github.io && make cv
```

Genera `cv/Diego_Macias_Vega_CV_EN.pdf` y `cv/Diego_Macias_Vega_CV_ES.pdf`. Si el texto ya no
cabe en una página, el comando falla y te dice cuál acortar. Para publicarlos:

```bash
git add cv && git commit -m "Update CV" && git push
```

La web enlaza a esos dos PDF, así que se actualizan solos al subirlos a `main`.

Ábrelos una vez y revisa los datos igual que en el paso 1. El CV no lleva teléfono: si una
solicitud lo pide, añádelo a la lista `contact` de los JSON.

## 6. LinkedIn (30 minutos)

Abre `docs/LINKEDIN.md`. En orden:

1. **Titular:** tu perfil → lápiz junto a tu nombre → campo «Titular».
2. **Acerca de:** tu perfil → «Añadir sección» → «Acerca de».
3. **Proyectos:** «Añadir sección» → «Recomendado» → «Añadir proyecto». Uno por cada proyecto del
   archivo, en el mismo orden. RAAN, solo después del paso 2 de aquí. Syndrome Lab, cuando
   publiques el informe.
4. **Certificaciones:** «Añadir sección» → «Licencias y certificaciones»: Cambridge C1 Advanced
   (Cambridge University Press & Assessment, 2025) y YCT 2.
5. **Destacado:** añade el enlace a <https://didimacveg.github.io> y el PDF del informe de RAAN.
6. **Conexiones:** la tabla del final. Diez por semana como máximo.

## 7. Arregla los repositorios públicos (1 hora)

Lista completa con comandos en `docs/REVISION_REPOS.md`. Lo más urgente:

1. `getsympto`: es público pero su licencia dice «propietario y confidencial». Hazlo privado o
   cambia la licencia.
2. `gravity-lab` y `kairos`: las cifras del README no coinciden con otros documentos.
3. Descripción y temas de cada repositorio (un comando por repositorio).

## 8. Cuando cambie algo

- **RAAN regenera su informe:** copia el PDF nuevo y sube el cambio.

```bash
cp ~/raan/reports/RAAN_technical_report.pdf ~/didimacveg.github.io/assets/raan/
```

```bash
cd ~/didimacveg.github.io && git add assets && git commit -m "Update RAAN report" && git push
```

  Si cambian las cifras de RAAN, cámbialas también en `index.html`, en los dos `cv/*.json` y en
  `docs/LINKEDIN.md` (busca `0.694`, `0.81` y `20,152`).
- **gravity-lab termina su mejora:** sustituye `assets/gravity-lab/simulator.webp` por una
  captura nueva (WebP, 1200 px de ancho como mucho) y quita la nota «The simulator is being
  improved…» de su ficha en `index.html`.
- **Syndrome Lab publica resultados (finales de noviembre):** sustituye su ficha en `index.html`
  (busca `id="p-syn"`), su entrada en los dos `cv/*.json` y el apartado 3.2 de `docs/LINKEDIN.md`.
  Pídemelo en una sesión nueva con el repositorio `syndrome-lab` y lo redacto a partir de sus datos.
- **Antes de cada subida:**

```bash
cd ~/didimacveg.github.io && make check
```

  Falla si se ha colado una raya larga, el naranja antiguo o texto retirado (Aerospace, QEC Lab).
