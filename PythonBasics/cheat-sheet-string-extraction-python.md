# Cheat Sheet: Extraer Pedazos de un String en Python (para Selenium)

Guía de los métodos más usados cuando el texto que trae Selenium (`.text`, atributos, etc.) no viene "limpio" y hay que parsearlo antes de usarlo.

---

## 1. `.strip()` — limpiar espacios y saltos de línea en los bordes

Elimina espacios, tabs y `\n` al principio y al final del string (NO en el medio).

```python
"  hola mundo  ".strip()        # "hola mundo"
"\n mentor@rahul.com \n".strip() # "mentor@rahul.com"
```

- `.lstrip()` → solo el borde izquierdo.
- `.rstrip()` → solo el borde derecho.
- `.strip("xyz")` → saca esos caracteres específicos de los bordes (no espacios): `"xxhola".strip("x")` → `"hola"`.

**Cuándo usarlo:** siempre después de un `.split()`, porque el pedazo que queda a menudo trae un espacio pegado.

---

## 2. `.split()` — cortar el string en una lista de pedazos

Corta el string cada vez que encuentra el separador indicado, y devuelve una **lista**.

```python
"Contact us at mentor@rahulshettyacademy.com now".split("at")
# ['Contact us ', ' mentor@rahulshettyacademy.com now']
```

Para quedarte con un pedazo puntual, indexás la lista:
```python
texto = "Contact us at mentor@rahulshettyacademy.com now"
texto.split("at")[1]        # ' mentor@rahulshettyacademy.com now'
texto.split("at")[1].strip() # 'mentor@rahulshettyacademy.com now'  (ya sin espacio inicial)
```

### 2.1 `.split()` sin argumento — separa por cualquier espacio en blanco
Si no le pasás nada, corta por espacios (y colapsa espacios múltiples), muy útil para quedarte con "la primera palabra" de un pedazo:
```python
"mentor@rahulshettyacademy.com now".split(" ")[0]
# 'mentor@rahulshettyacademy.com'
```

### 2.2 Encadenando `.split()` — el patrón del profesor
Así arma la línea comentada de tu código:
```python
message = "Your credentials are wrong at mentor@rahulshettyacademy.com now, retry"
var = message.split("at")[1].strip().split(" ")[0]
# Paso 1: split("at")      -> [" wrong ", " mentor@rahulshettyacademy.com now, retry"]
# Paso 2: [1]              -> " mentor@rahulshettyacademy.com now, retry"
# Paso 3: .strip()         -> "mentor@rahulshettyacademy.com now, retry"
# Paso 4: split(" ")[0]    -> "mentor@rahulshettyacademy.com"
```
Es una cadena de 4 operaciones: cortar → quedarte con el pedazo de la derecha → limpiar espacios sobrantes → cortar de nuevo por espacio y quedarte con la primera palabra (el email, antes del resto de la frase).

### 2.3 `.split(sep, maxsplit)` — limitar cuántos cortes hace
```python
"a-b-c-d".split("-", 1)   # ['a', 'b-c-d']  (solo corta 1 vez, desde la izquierda)
```

### 2.4 `.rsplit()` — igual que split pero contando desde la derecha
```python
"a-b-c-d".rsplit("-", 1)  # ['a-b-c', 'd']
```
Útil cuando lo que te importa es el ÚLTIMO pedazo (ej: la extensión de un archivo, o el último segmento de una URL).

---

## 3. Slicing `[:]` — cortar por posición de caracteres

```python
texto = "mentor@rahulshettyacademy.com"
texto[0:6]     # "mentor"
texto[7:]      # "rahulshettyacademy.com"  (del índice 7 hasta el final)
texto[:6]      # "mentor" (desde el principio hasta el índice 6, sin incluirlo)
texto[-3:]     # "com"    (los últimos 3 caracteres)
```
Sirve cuando la posición es siempre fija (ej: un código de error que siempre tiene 5 caracteres). Si la posición varía según el contenido, mejor usar `split` o `find`/`index`.

---

## 4. `.find()` y `.index()` — encontrar la posición de un substring

Ambos devuelven el índice donde empieza el substring buscado. Se usan cuando necesitás la POSICIÓN para después cortar con slicing.

```python
texto = "Contact us at mentor@rahulshettyacademy.com now"
pos = texto.find("mentor")     # 14
texto[pos:]                    # "mentor@rahulshettyacademy.com now"
```

**Diferencia entre `.find()` y `.index()`:**
- `.find()` devuelve `-1` si no lo encuentra (no rompe el programa).
- `.index()` tira `ValueError` si no lo encuentra (rompe el programa si no hacés try/except).

```python
texto.find("xyz")   # -1
texto.index("xyz")  # ValueError: substring not found
```
Para código de test que corre desatendido, `.find()` suele ser más seguro porque podés chequear `if pos != -1:` antes de usar el resultado.

---

## 5. `in` — chequear si un substring existe (sin extraer nada)

```python
"mentor@rahulshettyacademy.com" in alert_text   # True / False
```
Esto es justo lo que usás en tu `assert` al final del script: no extrae nada, solo confirma que el pedazo de texto está contenido en el string más grande.

---

## 6. `.replace()` — reemplazar (o borrar) un pedazo del string

```python
"mentor@rahulshettyacademy.com".replace("@rahulshettyacademy.com", "")
# "mentor"
texto.replace(" ", "")   # saca TODOS los espacios del string
```

---

## 7. `re` (expresiones regulares) — cuando el patrón es más complejo que un separador fijo

Para casos donde el "pedazo" a extraer tiene un formato reconocible (como un email) pero está rodeado de texto variable:

```python
import re

texto = "Your temp password is X7f9Q, valid for 24hs"
match = re.search(r"[A-Za-z0-9]{5}", texto)
if match:
    print(match.group())   # "X7f9Q"

# Extraer un email con regex (más robusto que split si el formato del texto cambia)
match = re.search(r"[\w\.-]+@[\w\.-]+", texto)
```
`re` conviene cuando `split`/`find` te obligarían a encadenar muchos pasos frágiles porque el texto alrededor del dato cambia de formato.

---

## 8. Tabla rápida: ¿cuál uso?

| Necesito...                                          | Método                          |
|-------------------------------------------------------|----------------------------------|
| Sacar espacios/saltos de línea sobrantes en los bordes | `.strip()`                      |
| Cortar el string en pedazos por un separador conocido  | `.split("separador")`           |
| Quedarme con el último pedazo después de un separador  | `.rsplit("sep", 1)[-1]` o `.split("sep")[-1]` |
| Cortar por posición fija de caracteres                 | slicing `texto[a:b]`            |
| Saber en qué posición empieza un substring             | `.find()` / `.index()`          |
| Solo verificar que un substring está presente           | `in`                             |
| Sacar o reemplazar un pedazo puntual                    | `.replace()`                    |
| El patrón es variable/complejo (emails, códigos, etc.)  | `re.search()` / `re.findall()`  |

---

## 9. Aplicado a tu assignment

Tu versión hardcodea el email; la del profesor lo extrae dinámicamente del mensaje de la ventana hija. La lógica completa, explicada paso a paso:

```python
message = driver.find_element(By.CSS_SELECTOR, ".red").text
# Ej: "Your login page is generated for you, use this email at mentor@rahulshettyacademy.com now"

var = message.split("at")[1].strip().split(" ")[0]
# 1) split("at")      -> corta el string en 2 partes, usando "at" como separador
# 2) [1]              -> te quedás con la parte de la DERECHA de "at"
# 3) .strip()         -> saca el espacio en blanco que quedó pegado al principio
# 4) split(" ")[0]    -> corta por espacio y te quedás con la primera palabra (el email solo,
#                        sin el resto de la frase "now" que viene después)
```

Alternativa más robusta si el texto cambia de redacción entre corridas (usando regex, no depende de que la palabra "at" siempre esté ahí):
```python
import re
var = re.search(r"[\w\.-]+@[\w\.-]+", message).group()
```
