"""
Ejemplo temas

✅ 1. Expresiones Regulares

📧 Correo electrónico válido

**Respuesta correcta:**

```
c) ^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$
```

### 📱 Número telefónico (+57 300 1234567)

**Respuesta correcta (corregida):**

```
^\+57 \d{3} \d{7}$
```

---

2. Optimización de Recursividad

### 🔹 Problema

La función original tiene complejidad exponencial.

### 🔹 Solución con Memoización

```python
def contar_rutas(m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0 or n == 0:
        return 1

    memo[(m, n)] = contar_rutas(m-1, n, memo) + contar_rutas(m, n-1, memo)
    return memo[(m, n)]
```

### 🔹 Complejidad

* Antes: O(2^(m+n))
* Después: O(m*n)

---

✅ 3. Operaciones con Conjuntos

```python
plan_cine = {"Ana", "Luis", "Pedro", "Sofía", "Carlos", "Lucía"}
plan_series = {"Pedro", "Sofía", "Marta", "Andrés", "Lucía", "Valentina"}
```

### 🔹 Unión (usuarios únicos)

```python
todos = plan_cine | plan_series
```

### 🔹 Intersección (ambos planes)

```python
ambos = plan_cine & plan_series
```

### 🔹 Solo cine

```python
solo_cine = plan_cine - plan_series
```

### 🔹 Exclusivos (uno solo)

```python
exclusivos = plan_cine ^ plan_series
```

### 🔹 Verificar usuario

```python
"Carlos" in plan_series
```

### 🔹 Porcentaje plan premium

```python
total = len(plan_cine | plan_series)
ambos = len(plan_cine & plan_series)
porcentaje = (ambos / total) * 100
```

---

## ✅ 4. Complejidad Algorítmica

### 🔹 Complejidad original

```python
O(n^2)
```

### 🔹 Si duplicamos n

```
Tiempo ≈ 4 veces mayor
```

### 🔹 Solución optimizada

```python
def encontrar_pares(lista, objetivo):
    vistos = set()

    for num in lista:
        complemento = objetivo - num
        if complemento in vistos:
            print(f"Par encontrado: ({complemento}, {num})")
        vistos.add(num)
```

### 🔹 Complejidad optimizada

```
O(n)
```

---

## 🎯 Resumen Final

* Regex correcta: opción C
* Optimización: memoización o programación dinámica
* Conjuntos: | & - ^
* Complejidad:

  * O(n^2) → doble ciclo
  * O(n) → usando set

"""


