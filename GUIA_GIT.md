# 🔧 Guía de Comandos Git para el Proyecto

## 📚 Flujo de Trabajo Git Flow

### Estructura de Ramas
```
master (producción)
  └── development (desarrollo)
        └── feature/* (características)
        └── release/* (releases)
        └── hotfix/* (correcciones urgentes)
```

---

## 🚀 Comandos Principales Utilizados

### 1️⃣ Configuración Inicial

```bash
# Inicializar repositorio
git init

# Conectar con repositorio remoto
git remote add origin https://github.com/SeanOsorio/An-lisis-de-Sentimiento-para-las-Acciones-del-Dow-Jones.git

# Verificar remoto
git remote -v

# Crear archivo .gitignore
# (Ya creado automáticamente)
```

### 2️⃣ Primer Commit

```bash
# Agregar archivos al staging
git add .

# Crear commit inicial
git commit -m "Initial commit: Configuración inicial del proyecto de análisis de sentimiento"

# Crear rama development
git branch development

# Ver ramas
git branch -a
```

### 3️⃣ Trabajo con Features

```bash
# Cambiar a development
git checkout development

# Crear nueva rama feature
git checkout -b feature/etl-eda

# Trabajar en la feature...
# (Desarrollar código, hacer commits frecuentes)

# Ver estado de cambios
git status

# Agregar cambios
git add .

# Commit de la feature
git commit -m "feat: Implementar pipeline completo de ETL y EDA

- Módulo ETL: extracción, transformación y carga
- Módulo EDA: 6 visualizaciones
- Pipeline principal automatizado"

# Volver a development
git checkout development

# Mergear feature en development (--no-ff para mantener historial)
git merge feature/etl-eda --no-ff -m "Merge feature/etl-eda into development"
```

### 4️⃣ Sincronización con GitHub

```bash
# Subir rama master
git push -u origin master

# Subir rama development
git push -u origin development

# Subir rama feature
git push -u origin feature/etl-eda

# Ver estado de ramas remotas
git branch -a

# Ver historial gráfico
git log --oneline --graph --all --decorate
```

### 5️⃣ Actualización de Documentación

```bash
# Agregar documentación
git add RESUMEN_PROYECTO.md

# Commit de documentación
git commit -m "docs: Agregar resumen completo del proyecto"

# Subir cambios
git push origin development
```

---

## 📋 Comandos de Consulta Útiles

### Ver Estado del Repositorio
```bash
# Estado actual
git status

# Ver diferencias
git diff

# Ver historial
git log --oneline

# Ver historial gráfico
git log --oneline --graph --all --decorate -10

# Ver ramas
git branch -a
```

### Ver Commits
```bash
# Últimos 5 commits
git log -5

# Commits con detalles
git log --stat

# Commits de un archivo
git log --follow RESUMEN_PROYECTO.md

# Ver cambios de un commit
git show <commit-hash>
```

### Ver Diferencias
```bash
# Diferencias entre ramas
git diff master..development

# Diferencias de un archivo
git diff stock_senti_analysis.csv

# Archivos cambiados entre commits
git diff --name-only HEAD~1 HEAD
```

---

## 🔄 Flujo Completo para Nueva Feature

```bash
# 1. Actualizar development
git checkout development
git pull origin development

# 2. Crear feature branch
git checkout -b feature/nombre-feature

# 3. Desarrollar y hacer commits
git add .
git commit -m "feat: Descripción del cambio"

# 4. Subir feature a GitHub (opcional)
git push -u origin feature/nombre-feature

# 5. Volver a development y mergear
git checkout development
git merge feature/nombre-feature --no-ff -m "Merge feature/nombre-feature into development"

# 6. Subir development actualizado
git push origin development

# 7. (Opcional) Eliminar feature branch local
git branch -d feature/nombre-feature

# 8. (Opcional) Eliminar feature branch remoto
git push origin --delete feature/nombre-feature
```

---

## 🎯 Crear un Release

```bash
# 1. Desde development, crear release branch
git checkout development
git checkout -b release/v1.0.0

# 2. Hacer ajustes finales (versiones, documentación, etc.)
git add .
git commit -m "chore: Preparar release v1.0.0"

# 3. Mergear release a master
git checkout master
git merge release/v1.0.0 --no-ff -m "Release v1.0.0"

# 4. Crear tag
git tag -a v1.0.0 -m "Release versión 1.0.0"

# 5. Mergear release de vuelta a development
git checkout development
git merge release/v1.0.0 --no-ff -m "Merge release v1.0.0 back to development"

# 6. Subir todo
git push origin master
git push origin development
git push origin --tags

# 7. Eliminar rama release
git branch -d release/v1.0.0
```

---

## 🚨 Hotfix (Corrección Urgente)

```bash
# 1. Desde master, crear hotfix
git checkout master
git checkout -b hotfix/nombre-fix

# 2. Hacer corrección
git add .
git commit -m "fix: Corrección urgente"

# 3. Mergear a master
git checkout master
git merge hotfix/nombre-fix --no-ff -m "Hotfix aplicado"

# 4. Crear tag de versión menor
git tag -a v1.0.1 -m "Hotfix v1.0.1"

# 5. Mergear también a development
git checkout development
git merge hotfix/nombre-fix --no-ff -m "Merge hotfix to development"

# 6. Subir cambios
git push origin master
git push origin development
git push origin --tags

# 7. Eliminar rama hotfix
git branch -d hotfix/nombre-fix
```

---

## 🔍 Comandos de Inspección

```bash
# Ver configuración
git config --list

# Ver commits de un autor
git log --author="Sean Osorio"

# Ver archivos en un commit
git ls-tree --name-only HEAD

# Ver tamaño del repositorio
git count-objects -vH

# Ver estadísticas de contribuciones
git shortlog -sn --all
```

---

## 🛠️ Comandos de Mantenimiento

```bash
# Limpiar archivos no trackeados
git clean -fd

# Descartar cambios locales
git checkout -- archivo.txt

# Deshacer último commit (mantener cambios)
git reset --soft HEAD~1

# Deshacer último commit (descartar cambios)
git reset --hard HEAD~1

# Ver archivos ignorados
git ls-files --others --ignored --exclude-standard

# Comprimir repositorio
git gc --aggressive
```

---

## 📊 Convenciones de Commits

### Tipos de commit:
- `feat:` Nueva característica
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Formato, punto y coma, etc (no afecta código)
- `refactor:` Refactorización de código
- `test:` Agregar o modificar tests
- `chore:` Mantenimiento, configuración, etc

### Formato:
```
<tipo>: <descripción breve>

[Cuerpo opcional con más detalles]

[Footer opcional con referencias]
```

### Ejemplos:
```bash
git commit -m "feat: Agregar módulo de predicción ML"
git commit -m "fix: Corregir error en carga de CSV"
git commit -m "docs: Actualizar README con instrucciones"
```

---

## 🎓 Resumen de Ramas Actuales

### Estado del Proyecto
```
✅ master:          Commit inicial
✅ development:     ETL + EDA + Documentación
✅ feature/etl-eda: Feature completa (mergeada)
```

### Próximas Ramas Recomendadas
```
📌 feature/ml-prediction:  Modelos de Machine Learning
📌 feature/dashboard:      Dashboard interactivo
📌 feature/text-analysis:  Análisis de texto de noticias
📌 release/v1.0.0:        Preparar primera versión oficial
```

---

## 🔗 Links Útiles

- **Repositorio**: https://github.com/SeanOsorio/An-lisis-de-Sentimiento-para-las-Acciones-del-Dow-Jones
- **Git Flow**: https://nvie.com/posts/a-successful-git-branching-model/
- **Conventional Commits**: https://www.conventionalcommits.org/

---

**Última actualización**: 14 de octubre de 2025
