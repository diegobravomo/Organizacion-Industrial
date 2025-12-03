# 📐 PROCESO ESTÁNDAR: DISCRIMINACIÓN DE PRECIOS (2 MERCADOS)

## 🎯 OBJETIVO
Calcular y comparar beneficios con y sin discriminación de precios en dos mercados.

---

## 📋 DATOS NECESARIOS

```
✅ Demanda Mercado 1: Q₁ = f(P₁)
✅ Demanda Mercado 2: Q₂ = g(P₂)
✅ Función de Costo Total: CT = CF + cQ
✅ Costo Marginal: CMg = c
```

---

# 🔵 PARTE A: SIN DISCRIMINAR (Precio Único)

> **Restricción:** P₁ = P₂ = P (mismo precio en ambos mercados)

---

## PASO 1️⃣: Convertir Demandas a Forma Inversa

**De:** Q = f(P)  
**A:** P = P(Q)

```
Mercado 1: Q₁ = a - bP₁  →  P₁ = (a/b) - (1/b)Q₁
Mercado 2: Q₂ = c - dP₂  →  P₂ = (c/d) - (1/d)Q₂
```

**✍️ Ejemplo:**
```
Q₁ = 15 - 0.2P₁  →  P₁ = 75 - 5Q₁
Q₂ = 7.5 - 0.05P₂  →  P₂ = 150 - 20Q₂
```

---

## PASO 2️⃣: Igualar Precios

**Condición:** P₁ = P₂

```
P₁(Q₁) = P₂(Q₂)
```

**Despejar Q₂ en función de Q₁:**
```
Q₂ = f(Q₁)
```

**✍️ Ejemplo:**
```
75 - 5Q₁ = 150 - 20Q₂
20Q₂ = 75 + 5Q₁
Q₂ = 3.75 + 0.25Q₁
```

---

## PASO 3️⃣: Cantidad Total

```
Q_total = Q₁ + Q₂
Q_total = Q₁ + f(Q₁)
Q_total = g(Q₁)
```

**✍️ Ejemplo:**
```
Q = Q₁ + (3.75 + 0.25Q₁)
Q = 1.25Q₁ + 3.75
```

---

## PASO 4️⃣: Ingreso Total

```
IT = P × Q_total
IT = P₁(Q₁) × g(Q₁)
```

**Expandir y simplificar:**
```
IT = h(Q₁)
```

**✍️ Ejemplo:**
```
IT = (75 - 5Q₁)(1.25Q₁ + 3.75)
IT = 75Q₁ - 6.25Q₁² + 281.25
```

---

## PASO 5️⃣: Costo Total

```
CT = CF + CMg × Q_total
CT = CF + c × g(Q₁)
```

**✍️ Ejemplo:**
```
CT = 100 + 10(1.25Q₁ + 3.75)
CT = 137.5 + 12.5Q₁
```

---

## PASO 6️⃣: Función de Beneficio

```
π = IT - CT
π = h(Q₁) - [CF + c × g(Q₁)]
```

**✍️ Ejemplo:**
```
π = (75Q₁ - 6.25Q₁² + 281.25) - (137.5 + 12.5Q₁)
π = 62.5Q₁ - 6.25Q₁² + 143.75
```

---

## PASO 7️⃣: Maximizar Beneficio

**Condición Primera Orden:**
```
dπ/dQ₁ = 0
```

**Resolver para Q₁*:**
```
Q₁* = ...
```

**Calcular Q₂*:**
```
Q₂* = f(Q₁*)
```

**Calcular P*:**
```
P* = P₁(Q₁*)  o  P* = P₂(Q₂*)  [son iguales]
```

**✍️ Ejemplo:**
```
dπ/dQ₁ = 62.5 - 12.5Q₁ = 0
Q₁* = 5

Q₂* = 3.75 + 0.25(5) = 5

P* = 75 - 5(5) = 50
```

---

## PASO 8️⃣: Beneficio Sin Discriminar

```
Q_total = Q₁* + Q₂*
IT = P* × Q_total
CT = CF + CMg × Q_total
π_sin = IT - CT
```

**✍️ Ejemplo:**
```
Q_total = 10
IT = 50 × 10 = 500
CT = 100 + 10(10) = 200
π_sin = 300
```

**📊 RESULTADO:** π_sin = $300

---

---

# 🔴 PARTE B: CON DISCRIMINACIÓN (Precio por Mercado)

> **Libertad:** P₁ ≠ P₂ (cada mercado tiene su precio óptimo)

---

## PASO 9️⃣: Maximizar en Mercado 1

**Ingreso Marginal = Costo Marginal**

```
P₁ = a₁ - b₁Q₁
IT₁ = P₁ × Q₁ = a₁Q₁ - b₁Q₁²
IMg₁ = a₁ - 2b₁Q₁

IMg₁ = CMg:
a₁ - 2b₁Q₁ = c
Q₁* = (a₁ - c)/(2b₁)
P₁* = a₁ - b₁Q₁*
```

**✍️ Ejemplo:**
```
P₁ = 75 - 5Q₁
IT₁ = 75Q₁ - 5Q₁²
IMg₁ = 75 - 10Q₁

75 - 10Q₁ = 10
Q₁* = 6.5
P₁* = 75 - 5(6.5) = 42.5
```

---

## PASO 🔟: Maximizar en Mercado 2

**Ingreso Marginal = Costo Marginal**

```
P₂ = a₂ - b₂Q₂
IT₂ = P₂ × Q₂ = a₂Q₂ - b₂Q₂²
IMg₂ = a₂ - 2b₂Q₂

IMg₂ = CMg:
a₂ - 2b₂Q₂ = c
Q₂* = (a₂ - c)/(2b₂)
P₂* = a₂ - b₂Q₂*
```

**✍️ Ejemplo:**
```
P₂ = 150 - 20Q₂
IT₂ = 150Q₂ - 20Q₂²
IMg₂ = 150 - 40Q₂

150 - 40Q₂ = 10
Q₂* = 3.5
P₂* = 150 - 20(3.5) = 80
```

---

## PASO 1️⃣1️⃣: Beneficio Con Discriminación

```
IT₁ = P₁* × Q₁*
IT₂ = P₂* × Q₂*
IT_total = IT₁ + IT₂

Q_total = Q₁* + Q₂*
CT = CF + CMg × Q_total

π_con = IT_total - CT
```

**✍️ Ejemplo:**
```
IT₁ = 42.5 × 6.5 = 276.25
IT₂ = 80 × 3.5 = 280
IT_total = 556.25

Q_total = 10
CT = 100 + 10(10) = 200

π_con = 556.25 - 200 = 356.25
```

**📊 RESULTADO:** π_con = $356.25

---

---

# ✅ PASO FINAL: COMPARACIÓN

## CAMBIO EN BENEFICIO

```
Δπ = π_con - π_sin
```

**✍️ Ejemplo:**
```
Δπ = 356.25 - 300 = 56.25
```

**💰 RESPUESTA:** La discriminación aumenta el beneficio en $56.25

---

## 📊 TABLA COMPARATIVA ESTÁNDAR

```
┌────────────────┬─────────────┬─────────────┬─────────────┐
│                │  Mercado 1  │  Mercado 2  │    TOTAL    │
├────────────────┼─────────────┼─────────────┼─────────────┤
│ SIN DISCRIMINAR                                           │
│ Cantidad (Q)   │     Q₁*     │     Q₂*     │  Q₁* + Q₂*  │
│ Precio (P)     │      P*     │      P*     │      -      │
│ Beneficio (π)  │      -      │      -      │    π_sin    │
├────────────────┼─────────────┼─────────────┼─────────────┤
│ CON DISCRIMINAR                                           │
│ Cantidad (Q)   │     Q₁**    │     Q₂**    │ Q₁** + Q₂** │
│ Precio (P)     │     P₁**    │     P₂**    │      -      │
│ Beneficio (π)  │      -      │      -      │    π_con    │
├────────────────┼─────────────┼─────────────┼─────────────┤
│ DIFERENCIA     │             │             │     Δπ      │
└────────────────┴─────────────┴─────────────┴─────────────┘
```

---

---

# 🎓 CONCEPTOS CLAVE DEL PROCESO

## 🔵 Sin Discriminar

**¿Por qué igualamos P₁ = P₂?**
- Porque el monopolista NO puede discriminar
- Debe cobrar el mismo precio en ambos mercados
- Esta restricción crea una relación Q₂(Q₁)

**¿Qué estamos maximizando?**
- Beneficio total respecto a Q₁
- Q₂ se ajusta automáticamente vía la relación Q₂(Q₁)

**¿Por qué usamos P₁ en el IT?**
- Porque P₁ = P₂ = P (son el mismo precio)
- Da igual cuál usar, pero P₁ está en función de Q₁

---

## 🔴 Con Discriminar

**¿Por qué maximizamos por separado?**
- Cada mercado es independiente
- El monopolista elige P₁ y P₂ óptimos por separado
- Aplica IMg = CMg en cada mercado

**¿Qué sucede con los precios?**
- El mercado menos elástico paga más
- El mercado más elástico paga menos
- P₁ ≠ P₂ en general

**¿Por qué aumenta el beneficio?**
- Extrae más excedente del consumidor
- Ajusta precio a la disposición de pago de cada mercado

---

---

# 🚨 ERRORES COMUNES

## ❌ ERROR 1: Usar P₂ en vez de P₁ sin justificar
**✅ Correcto:** Como P₁ = P₂, usar P₁ expresado en función de Q₁

## ❌ ERROR 2: No igualar precios en Parte A
**✅ Correcto:** Sin discriminar → P₁ = P₂ obligatorio

## ❌ ERROR 3: Sumar IMg₁ + IMg₂ en Parte A
**✅ Correcto:** No se suman. Se iguala precios y se trabaja con Q₁

## ❌ ERROR 4: Usar mismo precio en Parte B
**✅ Correcto:** Con discriminar → P₁ ≠ P₂ (cada mercado su precio)

## ❌ ERROR 5: Olvidar costo fijo en CT
**✅ Correcto:** CT = CF + CMg × Q (incluir siempre CF)

## ❌ ERROR 6: Calcular CT₁ y CT₂ por separado
**✅ Correcto:** CT es único (costos no se separan por mercado)

---

---

# 📝 PLANTILLA PARA APLICAR

## DATOS

```
Mercado 1: Q₁ = ___ - ___P₁
Mercado 2: Q₂ = ___ - ___P₂
CT = ___ + ___Q
CMg = ___
```

---

## SIN DISCRIMINAR

1. P₁ = ___ - ___Q₁
2. P₂ = ___ - ___Q₂
3. P₁ = P₂  →  Q₂ = ___ + ___Q₁
4. Q = ___ + ___Q₁
5. IT = (___ - ___Q₁)(___ + ___Q₁) = ___
6. CT = ___ + ___Q₁
7. π = ___ - ___Q₁²
8. dπ/dQ₁ = 0  →  Q₁* = ___
9. Q₂* = ___, P* = ___
10. **π_sin = ___**

---

## CON DISCRIMINAR

### Mercado 1:
11. IMg₁ = ___ - ___Q₁
12. IMg₁ = CMg  →  Q₁** = ___
13. P₁** = ___

### Mercado 2:
14. IMg₂ = ___ - ___Q₂
15. IMg₂ = CMg  →  Q₂** = ___
16. P₂** = ___

### Total:
17. IT_total = ___ + ___ = ___
18. CT = ___ + ___(___) = ___
19. **π_con = ___**

---

## RESPUESTA

```
Cambio en beneficio: Δπ = π_con - π_sin = ___
```

---

---

# 🎯 VERIFICACIONES RÁPIDAS

## ✅ Checklist Final

- [ ] Sin discriminar: P₁ = P₂ = P* (mismo precio)
- [ ] Con discriminar: P₁** ≠ P₂** (precios distintos)
- [ ] Con discriminar: Q_total puede ser igual o distinto que sin discriminar
- [ ] π_con > π_sin (siempre, la discriminación aumenta beneficio)
- [ ] Mercado menos elástico paga más
- [ ] Mercado más elástico paga menos
- [ ] CT usa Q_total (no se separa por mercado)
- [ ] CMg es constante (de CT lineal)

---

## 🔍 Validación de Resultados

**Si π_con < π_sin:** ¡ERROR! Revisa cálculos.

**Si P₁** = P₂**:** Coincidencia especial (elasticidades iguales), pero generalmente P₁** ≠ P₂**

**Si Q_total difiere mucho:** Revisa Q₂(Q₁) en Parte A

---

---

# 📚 EJEMPLO COMPLETO APLICADO

Ver: `EJERCICIO_2_DISCRIMINACION_COMPLETO.md`

---

**Última actualización:** 3 diciembre 2025, 6:55 AM
