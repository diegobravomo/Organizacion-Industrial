# EJERCICIO 2 - DISCRIMINACIÓN - PASO A PASO COMPLETO

## 📋 ENUNCIADO

```
Mercado 1: Q₁ = 15 - 0.2P₁
Mercado 2: Q₂ = 7.5 - 0.05P₂
CT = 100 + 10Q

Calcular: Cambio en beneficio con discriminación vs sin discriminación
```

---

## 🔵 PARTE A: SIN DISCRIMINAR (Precio único)

### PASO 1: Convertir demandas a P(Q)

```
Mercado 1:
Q₁ = 15 - 0.2P₁
0.2P₁ = 15 - Q₁
P₁ = 75 - 5Q₁

Mercado 2:
Q₂ = 7.5 - 0.05P₂
0.05P₂ = 7.5 - Q₂
P₂ = 150 - 20Q₂
```

**Resultado:** P₁ = 75 - 5Q₁  y  P₂ = 150 - 20Q₂

---

### PASO 2: Igualar precios (sin discriminar → mismo P)

```
P₁ = P₂

75 - 5Q₁ = 150 - 20Q₂
20Q₂ = 150 - 75 + 5Q₁
20Q₂ = 75 + 5Q₁
Q₂ = 3.75 + 0.25Q₁
```

**¿Por qué igualamos?** Para encontrar la relación entre Q₁ y Q₂ cuando hay un solo precio.

**Resultado:** Q₂ = 3.75 + 0.25Q₁

---

### PASO 3: Cantidad total

```
Q_total = Q₁ + Q₂
Q_total = Q₁ + (3.75 + 0.25Q₁)
Q_total = 1.25Q₁ + 3.75
```

**Resultado:** Q = 1.25Q₁ + 3.75

---

### PASO 4: Ingreso Total

```
IT = P × Q_total

Usamos P₁ (podríamos usar P₂, da lo mismo):
P = 75 - 5Q₁

IT = (75 - 5Q₁)(1.25Q₁ + 3.75)

Expandiendo:
= 75 × 1.25Q₁ + 75 × 3.75 - 5Q₁ × 1.25Q₁ - 5Q₁ × 3.75
= 93.75Q₁ + 281.25 - 6.25Q₁² - 18.75Q₁
= 75Q₁ - 6.25Q₁² + 281.25
```

**Resultado:** IT = 75Q₁ - 6.25Q₁² + 281.25

---

### PASO 5: Costo Total

```
CT = 100 + 10Q
CT = 100 + 10(1.25Q₁ + 3.75)
CT = 100 + 12.5Q₁ + 37.5
CT = 137.5 + 12.5Q₁
```

**Resultado:** CT = 137.5 + 12.5Q₁

---

### PASO 6: Beneficio

```
π = IT - CT
π = (75Q₁ - 6.25Q₁² + 281.25) - (137.5 + 12.5Q₁)
π = 75Q₁ - 6.25Q₁² + 281.25 - 137.5 - 12.5Q₁
π = 62.5Q₁ - 6.25Q₁² + 143.75
```

**Resultado:** π = 62.5Q₁ - 6.25Q₁² + 143.75

---

### PASO 7: Maximizar

```
dπ/dQ₁ = 62.5 - 12.5Q₁ = 0

12.5Q₁ = 62.5
Q₁* = 5
```

**Calcular Q₂:**
```
Q₂* = 3.75 + 0.25(5) = 5
```

**Calcular P:**
```
P = 75 - 5(5) = 50
```

**Resultado:** Q₁ = 5, Q₂ = 5, P = $50

---

### PASO 8: Beneficio sin discriminar

```
Q_total = 10
IT = 50 × 10 = 500
CT = 100 + 10(10) = 200
π = 500 - 200 = 300
```

**BENEFICIO SIN DISCRIMINAR = $300**

---

## 🔴 PARTE B: CON DISCRIMINACIÓN (Precio por mercado)

**Dato:** CMg = 10 (de CT = 100 + 10Q)

---

### PASO 9: MERCADO 1 (solo)

```
P₁ = 75 - 5Q₁

IT₁ = P₁ × Q₁ = (75 - 5Q₁)Q₁ = 75Q₁ - 5Q₁²

IMg₁ = 75 - 10Q₁

IMg₁ = CMg:
75 - 10Q₁ = 10
Q₁* = 6.5

P₁* = 75 - 5(6.5) = 42.5
```

**Resultado Mercado 1:** Q₁ = 6.5, P₁ = $42.5

---

### PASO 10: MERCADO 2 (solo)

```
P₂ = 150 - 20Q₂

IT₂ = P₂ × Q₂ = (150 - 20Q₂)Q₂ = 150Q₂ - 20Q₂²

IMg₂ = 150 - 40Q₂

IMg₂ = CMg:
150 - 40Q₂ = 10
Q₂* = 3.5

P₂* = 150 - 20(3.5) = 80
```

**Resultado Mercado 2:** Q₂ = 3.5, P₂ = $80

---

### PASO 11: Beneficio con discriminación

```
IT₁ = 42.5 × 6.5 = 276.25
IT₂ = 80 × 3.5 = 280
IT_total = 556.25

Q_total = 10
CT = 100 + 10(10) = 200

π = 556.25 - 200 = 356.25
```

**BENEFICIO CON DISCRIMINAR = $356.25**

---

## ✅ RESPUESTA FINAL

```
Sin discriminar: π = $300
Con discriminar: π = $356.25

CAMBIO = 356.25 - 300 = $56.25
```

**La discriminación aumenta el beneficio en $56.25**

---

## 📊 TABLA RESUMEN

```
┌──────────────┬─────────┬─────────┬─────────┐
│              │ Merc 1  │ Merc 2  │  Total  │
├──────────────┼─────────┼─────────┼─────────┤
│ SIN DISCRIM  │         │         │         │
│ Q            │   5     │   5     │   10    │
│ P            │  $50    │  $50    │         │
│ π            │         │         │  $300   │
├──────────────┼─────────┼─────────┼─────────┤
│ CON DISCRIM  │         │         │         │
│ Q            │  6.5    │  3.5    │   10    │
│ P            │ $42.5   │  $80    │         │
│ π            │         │         │ $356.25 │
├──────────────┼─────────┼─────────┼─────────┤
│ DIFERENCIA   │         │         │ +$56.25 │
└──────────────┴─────────┴─────────┴─────────┘
```

---

## 🎯 CONCEPTOS CLAVE

**¿Por qué igualamos P₁ = P₂ en Parte A?**
Para encontrar la relación Q₂(Q₁) cuando hay precio único.

**¿Por qué usamos P₁ en el IT?**
Porque P₁ = P₂ (mismo precio), da igual cuál usar.

**¿Por qué en Parte B calculamos por separado?**
Porque CON discriminación cada mercado tiene su propio precio óptimo.

**¿Por qué Mercado 2 paga más ($80 vs $42.5)?**
Porque es menos elástico (pendiente -20 vs -5 más pronunciada).

---

_Documento creado: 3 dic 2025, 6:30 AM_
