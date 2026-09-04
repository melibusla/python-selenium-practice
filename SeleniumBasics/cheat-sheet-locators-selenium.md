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

## 4. XPath — cuando nada de lo anterior alcanza
Se usa cuando los elementos no tienen ID, name o class únicos, cuando son dinámicos, o cuando necesitás ubicarlos por su texto o por su posición relativa a otros elementos.

- **Formato del value:** `//tag[@atributo='valor']` o rutas relativas tipo `//div[@class='card']//button`.
- **Ejemplo:**
  ```python
  driver.find_element(By.XPATH, "//button[text()='Enviar']")
  ```
- **Ventaja sobre CSS:** puede buscar por texto visible y moverse hacia arriba en el DOM (elemento padre), cosa que CSS no puede hacer.

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

## Tip práctico para decidir rápido

Cuando inspecciones un elemento en el navegador, preguntate en este orden:

1. ¿Tiene `id`? → usá **ID**.
2. ¿Es un input/select con `name`? → usá **Name**.
3. ¿Tiene clase o atributo único? → **CSS Selector**.
4. ¿Necesito buscarlo por texto o por relación con otro elemento (padre/hermano)? → **XPath**.
5. ¿Es un link con texto claro y único? → **LinkText**.

---

## Fuentes consultadas
- [Selenium Locators Made Easy: Types & Examples](https://www.testmuai.com/blog/locators-in-selenium-webdriver-with-examples/)
- [XPath in Selenium: Cheat Sheet & Dynamic Locators](https://testomat.io/blog/xpath-in-selenium/)
- [Selenium Locators Cheat Sheet (Java, mismos conceptos)](https://www.sdetpath.com/java-selenium-locators-cheat-sheet/)
