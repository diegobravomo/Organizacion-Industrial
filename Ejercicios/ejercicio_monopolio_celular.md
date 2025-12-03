# 📱 EJERCICIO: Monopolio de Teléfonos Celulares

## 📊 DATOS DEL PROBLEMA

**Demanda del mercado**: 
$$P = 100 - \frac{Q}{5}$$

**Costo Marginal**:
$$CMg(Q) = 10 + \frac{Q}{25}$$

---

## 🔢 SOLUCIÓN PASO A PASO

### **1️⃣ Función de Ingreso Total (IT)**

#### **Paso 1.1**: Recordar la definición

El ingreso total es el precio multiplicado por la cantidad vendida:

$$IT = P \cdot Q$$

#### **Paso 1.2**: Identificar la función de demanda

Nos dan: $P = 100 - \frac{Q}{5}$

Esta es la **demanda inversa** (precio en función de cantidad).

#### **Paso 1.3**: Sustituir P en la fórmula de IT

$$IT = P \cdot Q = \left(100 - \frac{Q}{5}\right) \cdot Q$$

#### **Paso 1.4**: Distribuir Q (multiplicar cada término)

$$IT = 100 \cdot Q - \frac{Q}{5} \cdot Q$$

$$IT = 100Q - \frac{Q \cdot Q}{5}$$

$$IT = 100Q - \frac{Q^2}{5}$$

**✅ RESPUESTA 1**: 
$$\boxed{IT(Q) = 100Q - \frac{Q^2}{5}}$$

**💡 Interpretación**: 
- El término $100Q$ representa ingresos si el precio fuera constante en 100
- El término $-\frac{Q^2}{5}$ representa la pérdida de ingresos porque el precio cae al aumentar Q

---

### **2️⃣ Función de Ingreso Marginal (IMg)**

El ingreso marginal es la **derivada** del ingreso total con respecto a Q:

$$IMg = \frac{dIT}{dQ}$$

#### **Paso 2.1**: Escribir la función a derivar

$$IT(Q) = 100Q - \frac{Q^2}{5}$$

#### **Paso 2.2**: Aplicar reglas de derivación

Recordemos las reglas básicas:
- $\frac{d}{dQ}(aQ) = a$ (derivada de término lineal)
- $\frac{d}{dQ}(Q^n) = n \cdot Q^{n-1}$ (regla de la potencia)

**Término 1**: $\frac{d}{dQ}(100Q) = 100$

**Término 2**: $\frac{d}{dQ}\left(\frac{Q^2}{5}\right) = \frac{1}{5} \cdot \frac{d}{dQ}(Q^2) = \frac{1}{5} \cdot 2Q = \frac{2Q}{5}$

#### **Paso 2.3**: Combinar los términos derivados

$$IMg = 100 - \frac{2Q}{5}$$

**💡 Observación importante**: 

Comparemos:
- **Demanda**: $P = 100 - \frac{Q}{5}$ (coeficiente de Q es $-\frac{1}{5}$)
- **IMg**: $IMg = 100 - \frac{2Q}{5}$ (coeficiente de Q es $-\frac{2}{5}$)

El IMg tiene **el doble de pendiente** que la demanda. Esto es una regla general para demandas lineales.

**✅ RESPUESTA 2**: 
$$\boxed{IMg(Q) = 100 - \frac{2Q}{5}}$$

---

### **3️⃣ Cantidad que Maximiza Utilidades**

El monopolista maximiza utilidades donde **IMg = CMg**:

$$100 - \frac{2Q}{5} = 10 + \frac{Q}{25}$$

#### **Paso 3.1**: Eliminar fracciones multiplicando por MCM

El mínimo común múltiplo de 5 y 25 es **25**.

Multiplicamos CADA término por 25:

$$25 \times 100 - 25 \times \frac{2Q}{5} = 25 \times 10 + 25 \times \frac{Q}{25}$$

#### **Paso 3.2**: Simplificar cada término

**Lado izquierdo**:
- $25 \times 100 = 2,500$
- $25 \times \frac{2Q}{5} = \frac{25 \times 2Q}{5} = \frac{50Q}{5} = 10Q$

**Lado derecho**:
- $25 \times 10 = 250$
- $25 \times \frac{Q}{25} = \frac{25Q}{25} = Q$

#### **Paso 3.3**: Ecuación simplificada

$$2,500 - 10Q = 250 + Q$$

#### **Paso 3.4**: Agrupar términos con Q a la izquierda

Sumamos $10Q$ a ambos lados:

$$2,500 = 250 + Q + 10Q$$

$$2,500 = 250 + 11Q$$

#### **Paso 3.5**: Aislar términos con Q

Restamos 250 de ambos lados:

$$2,500 - 250 = 11Q$$

$$2,250 = 11Q$$

#### **Paso 3.6**: Despejar Q

Dividimos ambos lados entre 11:

$$Q^* = \frac{2,250}{11}$$

#### **Paso 3.7**: Calcular valor decimal

$$Q^* = \frac{2,250}{11} = 204.545454...$$

Redondeando a 2 decimales:

$$Q^* \approx 204.55$$

**✅ RESPUESTA 3**: 
$$\boxed{Q^* = \frac{2,250}{11} \approx 204.55 \text{ unidades}}$$

---

### **4️⃣ Precio de Venta**

Sustituimos $Q^*$ en la función de demanda para encontrar el precio:

$$P = 100 - \frac{Q}{5}$$

#### **Paso 4.1**: Sustituir Q* en la función de demanda

$$P^* = 100 - \frac{Q^*}{5}$$

$$P^* = 100 - \frac{2,250/11}{5}$$

#### **Paso 4.2**: Simplificar la división de fracciones

$$P^* = 100 - \frac{2,250}{11 \times 5}$$

$$P^* = 100 - \frac{2,250}{55}$$

#### **Paso 4.3**: Simplificar la fracción

Dividimos numerador y denominador entre 5:

$$\frac{2,250}{55} = \frac{2,250 \div 5}{55 \div 5} = \frac{450}{11}$$

Entonces:

$$P^* = 100 - \frac{450}{11}$$

#### **Paso 4.4**: Convertir 100 a fracción con denominador 11

$$100 = \frac{100 \times 11}{11} = \frac{1,100}{11}$$

#### **Paso 4.5**: Restar fracciones con mismo denominador

$$P^* = \frac{1,100}{11} - \frac{450}{11}$$

$$P^* = \frac{1,100 - 450}{11}$$

$$P^* = \frac{650}{11}$$

#### **Paso 4.6**: Calcular valor decimal

$$P^* = \frac{650}{11} = 59.090909...$$

Redondeando a 2 decimales:

$$P^* \approx 59.09$$

**✅ RESPUESTA 4**: 
$$\boxed{P^* = \frac{650}{11} \approx \$59.09}$$

---

## 📈 VERIFICACIÓN

Comprobemos que efectivamente IMg = CMg en el punto de equilibrio:

#### **Verificación del Ingreso Marginal**

Sustituimos $Q^* = 204.55$ en la función de IMg:

$$IMg = 100 - \frac{2Q}{5}$$

$$IMg = 100 - \frac{2 \times 204.55}{5}$$

$$IMg = 100 - \frac{409.1}{5}$$

$$IMg = 100 - 81.82$$

$$IMg = 18.18$$

#### **Verificación del Costo Marginal**

Sustituimos $Q^* = 204.55$ en la función de CMg:

$$CMg = 10 + \frac{Q}{25}$$

$$CMg = 10 + \frac{204.55}{25}$$

$$CMg = 10 + 8.182$$

$$CMg = 18.182$$

#### **Conclusión de verificación**

$$IMg = CMg = 18.18$$

✅ **¡Correcto!** La condición de maximización se cumple perfectamente.

---

## 💰 ANÁLISIS ECONÓMICO

### Beneficio del Monopolista

**Ingreso Total**:
$$IT = P^* \cdot Q^* = 59.09 \times 204.55 = 12,088.72$$

**Costo Total** (necesitamos integrar CMg, pero sin función CT completa, calculamos solo el costo marginal promedio):
$$CMg(Q^*) = 18.18$$

**Markup del monopolio**:
$$\frac{P^* - CMg}{P^*} = \frac{59.09 - 18.18}{59.09} = \frac{40.91}{59.09} = 0.692 = 69.2\%$$

El monopolista cobra un **69% por encima del costo marginal**.

### Comparación con Competencia Perfecta

En competencia perfecta, las empresas producen donde **P = CMg** (no donde IMg = CMg).

#### **Paso 1**: Igualar precio a costo marginal

$$P = CMg$$

$$100 - \frac{Q}{5} = 10 + \frac{Q}{25}$$

#### **Paso 2**: Multiplicar por 25

$$25 \times 100 - 25 \times \frac{Q}{5} = 25 \times 10 + 25 \times \frac{Q}{25}$$

$$2,500 - 5Q = 250 + Q$$

#### **Paso 3**: Agrupar términos

$$2,500 - 250 = Q + 5Q$$

$$2,250 = 6Q$$

#### **Paso 4**: Despejar Q

$$Q^{cp} = \frac{2,250}{6} = 375$$

#### **Paso 5**: Calcular precio competitivo

$$P^{cp} = 100 - \frac{375}{5} = 100 - 75 = 25$$

#### **Comparación detallada**:

| Concepto | Monopolio | Comp. Perfecta | Diferencia |
|----------|-----------|----------------|------------|
| **Cantidad** | 204.55 | 375 | -45.5% (monopolio produce menos) |
| **Precio** | $59.09 | $25 | +136% (monopolio cobra más) |
| **Condición** | IMg = CMg | P = CMg | Diferentes reglas |
| **IMg/CMg en equilibrio** | $18.18 | - | - |

#### **Interpretación económica**:

1. **Restricción de cantidad**: El monopolista produce casi la **mitad** que en competencia perfecta
2. **Sobreprecio**: El monopolista cobra más del **doble** del precio competitivo
3. **Ineficiencia**: Consumidores dispuestos a pagar entre $25 y $59.09 NO pueden comprar
4. **Pérdida social**: Existe una pérdida irrecuperable de eficiencia (triángulo de Harberger)

---

## 📊 RESUMEN DE RESULTADOS

1. **Ingreso Total**: $IT(Q) = 100Q - \frac{Q^2}{5}$

2. **Ingreso Marginal**: $IMg(Q) = 100 - \frac{2Q}{5}$

3. **Cantidad óptima**: $Q^* = 204.55$ unidades

4. **Precio óptimo**: $P^* = \$59.09$

5. **Condición de equilibrio**: $IMg = CMg = 18.18$

---

## 🎯 CONCEPTOS CLAVE APLICADOS

✅ Maximización de beneficios del monopolista (IMg = CMg)

✅ Relación entre demanda e ingreso marginal (IMg tiene doble pendiente)

✅ El monopolista es price-maker pero enfrenta restricción de demanda

✅ Precio monopolístico > CMg → poder de mercado

✅ Cantidad monopolística < cantidad competitiva → ineficiencia

---

**¡Ejercicio completo!** 🎉
