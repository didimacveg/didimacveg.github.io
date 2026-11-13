# Pasos para Diego

Lo que depende de ti, en orden. Comandos para terminal **Ubuntu/WSL**: copia cada bloque tal cual.

El trabajo está en la rama `claude/epic-fermat-pxzd1k`. **La web pública no cambia hasta que
la fusiones en `main`** (paso 3).

---

## 1. Comprueba que todo lo que dice la web es verdad (15 minutos)

Baja la rama y abre la web en tu ordenador:

```bash
cd ~ && git clone https://github.com/didimacveg/didimacveg.github.io.git
```

```bash
cd ~/didimacveg.github.io && git checkout claude/epic-fermat-pxzd1k
```

```bash
make serve
```

Abre <http://localhost:8000> y lee la página entera. (Si ya tenías el repositorio clonado,
sustituye el primer comando por `cd ~/didimacveg.github.io && git fetch origin`.)

Comprueba en especial lo que **yo no puedo verificar**:

- [ ] **«How it was made» de cada proyecto.** Dice qué hizo la IA y qué es tuyo. En gravity-lab,
      Chess trainer, Quant Path, ARETÉ y TraceGuard lo he deducido. Si una frase no es exacta,
      cámbiala. Frases que debes mirar: «using it on my own games», «using it on my own
      machine», «doing the training», «the conversations with hardware engineers that shaped it».
- [ ] Cambridge C1 Advanced: año **2025**, nota **186**, «obtained at 16». ¿Quieres la nota a la vista?
- [ ] Instituto: «IES San Agustín del Guadalix», Bachillerato 2025 – 2027.
- [ ] «CS50x, in progress»: si lo has dejado o terminado, cámbialo.
- [ ] «Preparing the TU Delft selection exam» (apartado About).
- [ ] «Madrid champion at 12» y «black belt».
- [ ] «I also tutor school students privately».
- [ ] «EU citizen».
- [ ] Que funcionan <https://traceguard.eu>, <https://getsympto.app>,
      <https://didimacveg.github.io/gravity-lab/> y tu enlace de LinkedIn.

Para cambiar un texto: edita `index.html` con VS Code (`code index.html`), guarda y recarga.

## 2. Publica RAAN antes que la web (15 minutos)

La ficha de RAAN enlaza a `https://github.com/didimacveg/kessler` y a
`https://didimacveg.github.io/kessler/`. **Hoy los dos dan error 404** porque el repositorio es
privado y `main` está vacío.

**Opción A (recomendada):** haz primero los pasos 1 a 3 de `docs/PASOS_PARA_DIEGO.md` del
repositorio `kessler` (rama `claude/raan-pre-launch-review-8qqz4h`): hacerlo público, activar
Pages y fusionar. Cuando <https://didimacveg.github.io/kessler/> cargue, sigue con el paso 3 de aquí.

**Opción B:** si aún no quieres publicar RAAN, quita esos dos botones antes de fusionar:

```bash
cd ~/didimacveg.github.io && sed -i '/kessler\/">Live site<\/a>/d; /github.com\/didimacveg\/kessler">Repository<\/a>/d' index.html
```

```bash
git commit -am "Hide RAAN links until the repository is public" && git push
```

El enlace al informe técnico funciona en los dos casos (hay una copia en `assets/raan/`).
Ten en cuenta que con la opción B las capturas, las cifras y el informe de RAAN se publican
igualmente en esta web.

## 3. Publica la web (5 minutos)

1. Abre <https://github.com/didimacveg/didimacveg.github.io/pull/new/claude/epic-fermat-pxzd1k>
2. **Create pull request** → **Merge pull request** → **Confirm merge**.
3. Espera un par de minutos y abre <https://didimacveg.github.io>. Si ves la versión antigua,
   recarga con Ctrl+F5.

Sin navegador, desde la terminal:

```bash
cd ~/didimacveg.github.io && git checkout main && git pull && git merge --no-ff origin/claude/epic-fermat-pxzd1k && git push
```

## 4. Míralo en tu móvil (5 minutos)

Abre <https://didimacveg.github.io> en el móvil. Comprueba que la nube de partículas se mueve
con fluidez, que nada se sale por la derecha y que las capturas de RAAN se amplían al tocarlas.
Solo lo he probado en un móvil emulado. Si algo falla, dime el modelo y qué ves.

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
   archivo, en el mismo orden. RAAN, solo después del paso 2 de aquí.
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
- **QEC Lab tiene resultados:** sustituye su ficha en `index.html` (busca `id="p-qec"`). Pídemelo
  en una sesión nueva con el repositorio `qec-lab` y lo redacto a partir de sus datos.
- **Antes de cada subida:**

```bash
cd ~/didimacveg.github.io && make check
```

  Falla si se ha colado una raya larga o el naranja antiguo.
