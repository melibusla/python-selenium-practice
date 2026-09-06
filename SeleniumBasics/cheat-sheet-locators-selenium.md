# Cheat Sheet: Locators de Selenium (Python)

Guía rápida de cuándo usar cada locator, con el formato del value y ejemplo en Python (`By`).

**Orden de prioridad general:** ID > Name > CSS Selector > XPath > ClassName > LinkText/PartialLinkText > TagName.
Regla de oro: usá siempre el locator más simple y estable que identifique el elemento de forma única.

---

## 1. ID — el primero que hay que probar
Usalo cuando el elemento tiene un `id` único en el HTML. Es el método más rápido y confiable porque los IDs suelen ser únicos en una página.

- **Formato del value:** el valor exacto del atributo `id` (sin `#`).
- **Ejemplo:**
  ```python
  driver.find_element(By.ID, "username")
  ```

## 2. Name — para formularios
Cuando no hay ID pero sí `name`, típico en inputs de login/registro.

- **Formato del value:** el valor del atributo `name`.
- **Ejemplo:**
  ```python
  driver.find_element(By.NAME, "email")
  ```

## 3. CSS Selector — el más versátil y rápido después de ID
Es más rápido y limpio que XPath, ideal cuando ID o Name no están disponibles.

- **Formato del value:** sintaxis CSS normal — `#id`, `.clase`, `tag[attr='valor']`, combinaciones como `.btn.btn-primary`.
- **Ejemplo:**
  ```python
  driver.find_element(By.CSS_SELECTOR, "input.form-control")
  ```

### 3.1 Cómo apuntar a elementos SIN class/id único

Estrategia: buscá el ancestro más cercano que sí tenga algo único, y bajá desde ahí con un combinador.

```css
A B     /* descendiente en cualquier nivel: .header-text span */
A > B   /* hijo directo: div.col-md-6 > h2 */
A + B   /* hermano inmediato siguiente: label + input */
A ~ B   /* cualquier hermano siguiente: h2 ~ p */
```

Ejemplo real: para un `<span>` sin class dentro de `<h2>` sin class, dentro de un `<div class="header-text">`, el selector es `div.header-text h2 span` — no hace falta que `h2` ni `span` tengan class propia, alcanza con bajar desde el ancestro único.

### 3.2 Atributos parciales — para clases/ids dinámicos (React/Angular, etc.)
```css
[class^="valor"]   /* empieza con: [class^="btn-"] */
[class$="valor"]   /* termina con: [class$="-active"] */
[class*="valor"]   /* contiene: [class*="header"] */
[id*="user"]       /* cualquier id que contenga "user" */
```

### 3.3 Selección por posición (último recurso)
```css
li:first-child
li:last-child
li:nth-child(3)     /* 3er hijo, contando TODOS los tipos de tag */
li:nth-of-type(3)   /* 3er hijo del mismo tag */
```
`nth-child` cuenta la posición entre todos los hermanos; `nth-of-type` cuenta solo entre hermanos del mismo tag. Usá `nth-of-type` si hay tags mezclados para no romper el conteo.

### 3.4 Combinando varias condiciones (AND)
```css
div.header-text.hidden-xs         /* tiene ambas clases */
input[type="text"][name="user"]   /* AND de atributos */
```

## 4. XPath — cuando nada de lo anterior alcanza
Se usa cuando los elementos no tienen ID, name o class únicos, cuando son dinámicos, o cuando necesitás ubicarlos por su texto o por su posición relativa a otros elementos.

- **Formato del value:** `//tag[@atributo='valor']` o rutas relativas tipo `//div[@class='card']//button`.
- **Ejemplo:**
  ```python
  driver.find_element(By.XPATH, "//button[text()='Enviar']")
  ```
- **Ventaja sobre CSS:** puede buscar por texto visible y moverse hacia arriba en el DOM (elemento padre), cosa que CSS no puede hacer.

### 4.1 contains() — cuando el valor es parcial o dinámico
```xpath
//div[contains(@class, 'header-text')]
//input[contains(@id, 'user')]
//span[contains(text(), 'Learn Earn')]
```

### 4.2 text() y normalize-space() — localizar por contenido visible
```xpath
//button[text()='Submit']
//span[normalize-space(text())='An Academy to']
```
`normalize-space()` elimina espacios/saltos de línea extra que suelen romper el match exacto con `text()`.

### 4.3 Ejes (axes) — moverse por el árbol desde un punto conocido
```xpath
//label[text()='Usuario']/following-sibling::input
//input[@id='user']/parent::div
//div[@class='card']/ancestor::section
//h2/following::span[1]
//tr[td[text()='Juan']]/preceding-sibling::tr[1]
```
- `parent::` sube un nivel; `ancestor::` sube cuantos niveles haga falta.
- `following-sibling::` / `preceding-sibling::` se mueve entre hermanos.
- `following::` / `preceding::` busca en TODO el documento después/antes del nodo, no solo hermanos.
- Esto es lo que hace a XPath insustituible cuando el dato único está en un elemento HERMANO o HIJO del que necesitás clickear (ej: un ícono sin atributos, al lado de un texto con el nombre del usuario).

### 4.4 Posición
```xpath
(//li)[3]              # 3er <li> de TODO el documento
//ul/li[2]              # 2do <li> hijo directo de ese <ul>
//table/tbody/tr[last()]
```
Ojo: `//li[3]` (sin paréntesis) NO trae "el 3er li global" — trae "todo li que sea el 3er hijo de su padre". Para el 3er resultado global, usá `(//li)[3]`.

### 4.5 Combinando condiciones (AND / OR)
```xpath
//input[@type='text' and @name='user']
//div[@class='a' or @class='b']
```

### 4.6 Ejemplo aplicado: traducir un CSS a XPath
Para `div.header-text h2 span`:
```xpath
//div[@class='header-text hidden-xs']//h2/span
//div[contains(@class, 'header-text')]//h2/span   # más flexible si la clase trae más tokens
```

## 5. ClassName — con cuidado
Funciona bien con una sola clase, pero si el elemento tiene varias clases (ej. `"btn btn-primary"`) no podés pasarlas juntas — ahí conviene usar CSS Selector en su lugar.

- **Formato del value:** el nombre de una sola clase, sin el punto.
- **Ejemplo:**
  ```python
  driver.find_element(By.CLASS_NAME, "error-message")
  ```

## 6. LinkText / PartialLinkText — solo para enlaces `<a>`
`linkText` busca el texto exacto y completo del link; `partialLinkText` busca una parte de ese texto. Ambos son sensibles a mayúsculas y solo funcionan sobre elementos ancla.

- **Formato del value:** el texto visible del link (completo o parcial).
- **Ejemplo:**
  ```python
  driver.find_element(By.LINK_TEXT, "Iniciar sesión")
  driver.find_element(By.PARTIAL_LINK_TEXT, "Iniciar")
  ```

---

## 7. Tabla rápida CSS ↔ XPath (equivalencias)

| Necesito                          | CSS                          | XPath                                      |
|-----------------------------------|-------------------------------|---------------------------------------------|
| Descendiente en cualquier nivel   | `A B`                        | `//A//B`                                    |
| Hijo directo                      | `A > B`                      | `//A/B`                                     |
| Hermano siguiente inmediato       | `A + B`                      | `//A/following-sibling::B[1]`               |
| Contiene texto                    | *(no existe en CSS puro)*    | `//tag[contains(text(),'x')]`               |
| Atributo contiene valor           | `[attr*='x']`                | `//tag[contains(@attr,'x')]`                |
| Subir al padre                    | *(no existe en CSS puro)*    | `//tag/parent::div`                         |
| n-ésimo hijo del mismo tag        | `tag:nth-of-type(n)`         | `(//tag)[n]` o `//parent/tag[n]`            |

**Diferencia clave:** CSS solo baja en el árbol (padre → hijo). XPath también sube (`parent`, `ancestor`), por eso es el único recurso cuando el único dato único está en un hermano o hijo del elemento que necesitás.

---

## Tip práctico para decidir rápido

Cuando inspecciones un elemento en el navegador, preguntate en este orden:

1. ¿Tiene `id`? → usá **ID**.
2. ¿Es un input/select con `name`? → usá **Name**.
3. ¿Tiene clase o atributo único? → **CSS Selector**.
4. ¿No tiene nada único pero un ANCESTRO sí? → **CSS Selector** con combinador (`A B`, `A > B`) desde el ancestro.
5. ¿Necesito buscarlo por texto, o por relación con un HERMANO/PADRE? → **XPath** (`contains(text())`, `parent::`, `following-sibling::`).
6. ¿Es un link con texto claro y único? → **LinkText**.
7. Si nada de lo anterior es único, último recurso: posición (`nth-of-type` en CSS o `(//tag)[n]` en XPath) — pero verificá primero en la consola del navegador que matchea exactamente 1 elemento (`$$('selector')` o `$x("xpath")`).

---

## Fuentes consultadas
- [Selenium Locators Made Easy: Types & Examples](https://www.testmuai.com/blog/locators-in-selenium-webdriver-with-examples/)
- [XPath in Selenium: Cheat Sheet & Dynamic Locators](https://testomat.io/blog/xpath-in-selenium/)
- [Selenium Locators Cheat Sheet (Java, mismos conceptos)](https://www.sdetpath.com/java-selenium-locators-cheat-sheet/)
