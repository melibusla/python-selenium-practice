# Selenium Notes

## Locating an element with multiple classes

This selector:

```python
".alert.alert-danger.col-md-12"
```

targets an element with three CSS classes:

1. `alert`
2. `alert-danger`
3. `col-md-12`

For example:

```html
<div class="alert alert-danger col-md-12">
    Incorrect username/password.
</div>
```

`By.CLASS_NAME` accepts only one class name:

```python
By.CLASS_NAME, "alert"
```

For multiple classes, use a CSS selector. Each `.` means the element must
also have that class:

```python
By.CSS_SELECTOR, ".alert.alert-danger.col-md-12"
```

## Selenium wait conditions

### `presence_of_element_located`

Waits until the element exists in the page DOM:

```python
wait.until(
    expected_conditions.presence_of_element_located(alert_locator)
)
```

The element may still be hidden or have empty text.

### `text_to_be_present_in_element`

Waits until the element exists and contains the specified text:

```python
wait.until(
    expected_conditions.text_to_be_present_in_element(
        alert_locator,
        "Incorrect username/password."
    )
)
```

This is useful when an alert element appears before its message is populated.

### Related conditions

- `visibility_of_element_located`: the element exists and is visible.
- `element_to_be_clickable`: the element is visible and enabled.
- `presence_of_element_located`: the element exists, but may be hidden or empty.

## Tuple unpacking with `*`

This locator is a tuple:

```python
alert_locator = (
    By.CSS_SELECTOR,
    ".alert.alert-danger.col-md-12"
)
```

The `*` unpacks the tuple when calling `find_element`:

```python
driver.find_element(*alert_locator)
```

This is equivalent to:

```python
driver.find_element(
    By.CSS_SELECTOR,
    ".alert.alert-danger.col-md-12"
)
```

Without `*`, Python would pass the whole tuple as one argument:

```python
driver.find_element(alert_locator)
```

That is incorrect because `find_element` expects two separate arguments:
the locating strategy and the locator value.
