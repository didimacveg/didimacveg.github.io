# Pasos para Diego

Lo que depende de ti, en orden. Comandos para terminal **Ubuntu/WSL**: copia cada bloque tal cual.

Revisión del 13 de noviembre de 2026. El trabajo está en la rama `claude/upbeat-davinci-m61j9h`,
con un pull request abierto contra `main`. **La web pública no cambia hasta que lo fusiones**
(paso 3).

---

## 1. Lee lo que ha cambiado (10 minutos)

```bash
cd ~/didimacveg.github.io && git fetch origin && git checkout claude/upbeat-davinci-m61j9h && git pull
```

```bash
make serve
```

Abre <http://localhost:8000>. (Si no tienes el repositorio clonado:
`cd ~ && git clone https://github.com/didimacveg/didimacveg.github.io.git` y repite.)

Comprueba lo que **yo no puedo verificar**:

- [ ] Solicitudes: Computer Science and Engineering (TU Delft, selection test), Applied Physics
      (TU Eindhoven), Advanced Technology (University of Twente).
- [ ] «Preparing the TU Delft selection test» (apartado About, «Currently»).
- [ ] Syndrome Lab: «Results and report to be published late November 2026». Si la fecha se
      mueve, cámbiala en `index.html`, en los dos `cv/*.json` y en `docs/LINKEDIN.md`.
- [ ] CS50x: «Started 2026».
- [ ] Los dos CV: `cv/Diego_Macias_Vega_CV_EN.pdf` y `cv/Diego_Macias_Vega_CV_ES.pdf`.
- [ ] Lo de siempre: C1 (2025, 186, a los 16), instituto, «EU citizen», clases particulares y
      los apartados «How it was made».

## 2. RAAN: el repositorio sigue sin ser público (5 minutos)

Hoy, 13 de noviembre, `https://github.com/didimacveg/kessler` **da error 404 a quien no ha
iniciado sesión**, y GitHub lo lista como privado. El botón «Repository» de la ficha de RAAN
lleva ahí. El despliegue de la web de RAAN sí terminó bien (a las 12:16 UTC), pero desde mi
entorno no puedo abrir `https://didimacveg.github.io/kessler/`.

Compruébalo en una ventana privada del navegador (Ctrl+Mayús+N):

- <https://github.com/didimacveg/kessler>
- <https://didimacveg.github.io/kessler/>

Si el primero da 404, hazlo público:

```bash
gh repo edit didimacveg/kessler --visibility public --accept-visibility-change-consequences
```

O en la web: <https://github.com/didimacveg/kessler/settings> → abajo del todo, **Change
visibility** → **Make public**.

Si aún no quieres publicarlo, quita los dos botones antes de fusionar:

```bash
cd ~/didimacveg.github.io && sed -i '/kessler\/">Live site<\/a>/d; /github.com\/didimacveg\/kessler">Repository<\/a>/d' index.html && git commit -am "Hide RAAN links until the repository is public" && git push
```

## 3. Fusiona el pull request (2 minutos)

El comando exacto, desde Ubuntu/WSL:

```bash
cd ~/didimacveg.github.io && git fetch origin && git checkout main && git pull origin main && git merge --no-ff origin/claude/upbeat-davinci-m61j9h -m "Merge content review: applications, Syndrome Lab, CV and LinkedIn" && git push origin main
```

Con `gh`, si lo tienes instalado, es equivalente:

```bash
gh pr merge claude/upbeat-davinci-m61j9h --repo didimacveg/didimacveg.github.io --merge
```

O en el navegador: <https://github.com/didimacveg/didimacveg.github.io/pulls> → el pull
request → **Merge pull request** → **Confirm merge**.

Espera un par de minutos y abre <https://didimacveg.github.io>. Si ves la versión antigua,
recarga con Ctrl+F5.

## 4. Comprueba los enlaces que yo no alcanzo (5 minutos)

Con la web ya publicada, pulsa cada uno:

- [ ] RAAN: «Live site» y «Repository» (paso 2).
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
cp ~/kessler/reports/RAAN_technical_report.pdf ~/didimacveg.github.io/assets/raan/
```

```bash
cd ~/didimacveg.github.io && git add assets && git commit -m "Update RAAN report" && git push
```

  Si cambian las cifras de RAAN, cámbialas también en `index.html`, en los dos `cv/*.json` y en
  `docs/LINKEDIN.md` (busca `0.694`, `0.81` y `20,152`).
- **Syndrome Lab publica resultados (finales de noviembre):** sustituye su ficha en `index.html`
  (busca `id="p-syn"`), su entrada en los dos `cv/*.json` y el apartado 3.2 de `docs/LINKEDIN.md`.
  Pídemelo en una sesión nueva con el repositorio `syndrome-lab` y lo redacto a partir de sus datos.
- **Antes de cada subida:**

```bash
cd ~/didimacveg.github.io && make check
```

  Falla si se ha colado una raya larga, el naranja antiguo o texto retirado (Aerospace, QEC Lab).
