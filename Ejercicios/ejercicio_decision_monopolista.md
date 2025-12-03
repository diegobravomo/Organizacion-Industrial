# 📊 EJERCICIO: Decisión Óptima del Monopolista

## 📋 DATOS DEL PROBLEMA

**Costo Total**: 
$$CT = 50Q$$

**Demanda del mercado**: 
$$P = 100 - Q$$

---

## 🔢 SOLUCIÓN DETALLADA

### **PREGUNTA 1: Si produce Q = 20, ¿cuál será el precio?**

#### **Paso 1.1**: Identificar la relación precio-cantidad

La demanda nos dice que el precio depende de la cantidad que el monopolista ofrezca al mercado.

$$P = 100 - Q$$

#### **Paso 1.2**: Sustituir Q = 20

$$P = 100 - 20$$

$$P = 80$$

**✅ RESPUESTA 1**: 
$$\boxed{P = \$80}$$

---

### **PREGUNTA 2: Si produce Q = 40, ¿cuál será el precio?**

#### **Paso 2.1**: Sustituir Q = 40 en la demanda

$$P = 100 - Q$$

$$P = 100 - 40$$

$$P = 60$$

**✅ RESPUESTA 2**: 
$$\boxed{P = \$60}$$

#### **Observación importante**:

Al aumentar la producción de 20 a 40 unidades (duplicar):
- El precio cae de $80 a $60 (caída de $20)
- **Relación inversa**: A mayor cantidad, menor precio
- El monopolista enfrenta la curva de demanda del mercado completo

---

### **PREGUNTA 3: ¿Qué debe considerar el monopolista para decidir Q* y P* óptimos?**

El monopolista debe **maximizar su beneficio**, no solo sus ingresos.

#### **Paso 3.1**: Calcular el Beneficio (π)

$$\pi = IT - CT$$

Donde:
- $IT$ (Ingreso Total) = $P \times Q$
- $CT$ (Costo Total) = $50Q$

#### **Paso 3.2**: Expresar beneficio en función de Q

Sustituimos $P = 100 - Q$:

$$\pi(Q) = P \cdot Q - CT$$

$$\pi(Q) = (100 - Q) \cdot Q - 50Q$$

$$\pi(Q) = 100Q - Q^2 - 50Q$$

$$\pi(Q) = 50Q - Q^2$$

#### **Paso 3.3**: Encontrar la cantidad óptima (maximizar π)

Para maximizar, derivamos e igualamos a cero:

$$\frac{d\pi}{dQ} = 0$$

$$\frac{d}{dQ}(50Q - Q^2) = 0$$

$$50 - 2Q = 0$$

$$2Q = 50$$

$$Q^* = 25$$

#### **Paso 3.4**: Calcular el precio óptimo

$$P^* = 100 - Q^*$$

$$P^* = 100 - 25$$

$$P^* = 75$$

#### **Paso 3.5**: Calcular el beneficio máximo

$$\pi^* = 50(25) - (25)^2$$

$$\pi^* = 1,250 - 625$$

$$\pi^* = 625$$

---

## 📊 ANÁLISIS COMPARATIVO

Comparemos las tres opciones:

| Cantidad (Q) | Precio (P) | Ingreso Total (IT) | Costo Total (CT) | **Beneficio (π)** |
|--------------|------------|-------------------|------------------|-------------------|
| 20 | $80 | $1,600 | $1,000 | **$600** |
| **25 (óptimo)** | **$75** | **$1,875** | **$1,250** | **$625** ✅ |
| 40 | $60 | $2,400 | $2,000 | **$400** |

### **Observaciones clave**:

1. **Q = 20 (subproducción)**:
   - Precio alto ($80) pero pocas ventas
   - Beneficio = $600 (subóptimo)

2. **Q = 25 (óptimo)**:
   - Equilibrio perfecto entre precio y cantidad
   - **Beneficio máximo = $625**

3. **Q = 40 (sobreproducción)**:
   - Muchas ventas pero precio muy bajo ($60)
   - Beneficio = $400 (menor que en Q=20)
   - El IT es máximo ($2,400) pero el costo también es alto

---

## 💡 CONDICIÓN DE MAXIMIZACIÓN (Método Alternativo)

### **Usando IMg = CMg**

#### **Paso 1**: Calcular Ingreso Marginal

$$IT = P \cdot Q = (100 - Q) \cdot Q = 100Q - Q^2$$

$$IMg = \frac{dIT}{dQ} = 100 - 2Q$$

#### **Paso 2**: Calcular Costo Marginal

$$CT = 50Q$$

$$CMg = \frac{dCT}{dQ} = 50$$

**Nota**: El CMg es **constante** en 50 (no depende de Q)

#### **Paso 3**: Igualar IMg = CMg

$$100 - 2Q = 50$$

$$-2Q = 50 - 100$$

$$-2Q = -50$$

$$Q^* = 25$$

#### **Verificación**:

- **IMg(Q=25)**: $100 - 2(25) = 100 - 50 = 50$ ✅
- **CMg**: $50$ ✅
- **IMg = CMg** ✅

---

## 🎯 RESPUESTA A LA PREGUNTA 3

**¿Qué debe considerar el monopolista?**

### **1. Condición de Maximización de Beneficio**

El monopolista debe producir donde:

$$\boxed{IMg = CMg}$$

**NO** donde IT es máximo ni donde P es máximo.

### **2. Análisis de la Curva de Demanda**

- Enfrentar la demanda del mercado completo
- Entender el trade-off: ↑Q → ↓P
- No puede cobrar "cualquier precio" arbitrariamente

### **3. Estructura de Costos**

En este caso:
- $CMg = 50$ (constante)
- No hay costos fijos (CT = 50Q, sin término independiente)
- A mayor Q, mayor CT proporcionalmente

### **4. Evaluar Beneficio, no solo Ingreso**

| Concepto | Fórmula | En Q* = 25 |
|----------|---------|------------|
| Ingreso Marginal | $IMg = 100 - 2Q$ | $50 |
| Costo Marginal | $CMg = 50$ | $50 |
| Precio | $P = 100 - Q$ | $75 |
| Beneficio | $\pi = 50Q - Q^2$ | $625 |

### **5. Markup sobre Costo Marginal**

$$\text{Markup} = \frac{P - CMg}{P} = \frac{75 - 50}{75} = \frac{25}{75} = 0.333 = 33.3\%$$

El monopolista cobra **33.3% por encima del costo marginal**.

---

## 📈 ANÁLISIS GRÁFICO CONCEPTUAL

```
Precio
  |
100|_____ Demanda: P = 100 - Q
  |     \
  |      \
 75|-------●---- P* (precio óptimo)
  |       |\
  |       | \
 50|_______| _\_______ CMg = 50
  |   IMg  |   \
  |        |    \
  |________|_____\______ Cantidad
  0       25     50    100
         Q*     Qcp
```

**Elementos clave**:
- **IMg** tiene doble pendiente que la demanda
- **IMg = CMg** en Q* = 25
- **P* = 75** > CMg = 50 (poder de mercado)
- En competencia perfecta: Q = 50, P = 50

---

## ✅ RESUMEN DE RESPUESTAS

**Pregunta 1**: Si Q = 20 → **P = $80**

**Pregunta 2**: Si Q = 40 → **P = $60**

**Pregunta 3**: El monopolista debe:
1. **Igualar IMg = CMg** para maximizar beneficio
2. **Producir Q* = 25 unidades**
3. **Vender a P* = $75**
4. **Obtener π* = $625**

---

## 🔑 CONCEPTOS CLAVE APLICADOS

✅ **Maximización de beneficios** (no de ingresos)

✅ **Condición IMg = CMg** (regla de oro del monopolista)

✅ **Trade-off precio-cantidad** en la demanda

✅ **Poder de mercado**: P > CMg

✅ **Comparación de escenarios** para decisión óptima

✅ **Costo marginal constante** (pendiente cero)

---

## 💡 ERRORES COMUNES A EVITAR

❌ **Error 1**: Pensar que el monopolista debe maximizar IT
- IT es máximo en Q = 50, pero π es menor ($0 en ese punto)

❌ **Error 2**: Producir donde P = CMg
- Eso sería competencia perfecta, no monopolio
- En monopolio: IMg = CMg, con P > CMg

❌ **Error 3**: Ignorar los costos al decidir
- Precio alto con pocas ventas puede ser peor que precio moderado con más ventas

❌ **Error 4**: Creer que puede cobrar cualquier precio
- Está restringido por la curva de demanda del mercado

---

**¡Ejercicio completo!** 🎉

**Lección principal**: El monopolista maximiza **beneficio** (π), no ingreso, igualando IMg = CMg.
