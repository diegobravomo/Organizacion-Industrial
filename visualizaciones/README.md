# 📊 Visualizaciones: Diagramas y Dashboards de Modelos

> Representaciones visuales de estructuras de mercado y modelos de competencia.

## 📑 Catálogo de Visualizaciones

1. [Estructuras de Mercado](#estructuras-de-mercado)
2. [Modelo de Cournot](#modelo-de-cournot)
3. [Modelo de Bertrand](#modelo-de-bertrand)
4. [Modelo de Stackelberg](#modelo-de-stackelberg)
5. [Teoría de Juegos](#teoría-de-juegos)

---

## Estructuras de Mercado

### Clasificación de Mercados

```mermaid
flowchart TD
    A[Estructuras de Mercado] --> B[Competencia Perfecta]
    A --> C[Competencia Imperfecta]
    
    C --> D[Monopolio]
    C --> E[Oligopolio]
    C --> F[Competencia Monopolística]
    
    E --> G[Cournot<br/>Cantidades]
    E --> H[Bertrand<br/>Precios]
    E --> I[Stackelberg<br/>Líder-Seguidor]
    
    style A fill:#e1f5fe
    style B fill:#c8e6c9
    style D fill:#ffcdd2
    style E fill:#fff9c4
    style F fill:#f3e5f5
```

### Comparación de Eficiencia

```mermaid
flowchart LR
    subgraph Eficiencia["Eficiencia de Mercado"]
        CP[Competencia Perfecta<br/>P = CMg<br/>Máxima Eficiencia]
        B[Bertrand<br/>P = CMg<br/>Paradoja]
        CO[Cournot<br/>CMg < P < P_m]
        M[Monopolio<br/>P > CMg<br/>Pérdida de Eficiencia]
    end
    
    CP --> B
    B --> CO
    CO --> M
    
    style CP fill:#c8e6c9
    style B fill:#c8e6c9
    style CO fill:#fff9c4
    style M fill:#ffcdd2
```

---

## Modelo de Cournot

### Funciones de Reacción

```mermaid
xychart-beta
    title "Funciones de Reacción en Duopolio de Cournot"
    x-axis "Cantidad Empresa 1 (q₁)" [0, 10, 20, 30, 40, 50]
    y-axis "Cantidad Empresa 2 (q₂)" 0 --> 50
    line "FR Empresa 2" [50, 40, 30, 20, 10, 0]
    line "FR Empresa 1" [0, 10, 20, 30, 40, 50]
```

### Proceso de Decisión Cournot

```mermaid
flowchart TD
    A[Empresa maximiza π] --> B[Max π_i = P·q_i - C_i]
    B --> C[Sustituir P = a - b·Q]
    C --> D[Derivar respecto a q_i]
    D --> E[Igualar a cero]
    E --> F[Obtener Función de Reacción]
    F --> G[q_i* = f·q_j]
    G --> H[Equilibrio de Nash]
    H --> I["q_i* = (a-c)/(n+1)b"]
    
    style H fill:#fff9c4
    style I fill:#c8e6c9
```

---

## Modelo de Bertrand

### Paradoja de Bertrand

```mermaid
flowchart TD
    subgraph Supuestos
        S1[Productos Homogéneos]
        S2[2 Empresas]
        S3[Competencia en Precios]
    end
    
    S1 --> R[Resultado]
    S2 --> R
    S3 --> R
    
    R --> C["P = CMg<br/>(Precio Competitivo)"]
    R --> B["π = 0<br/>(Beneficio Cero)"]
    
    C --> P[PARADOJA:<br/>Solo 2 empresas<br/>logran resultado competitivo]
    B --> P
    
    style P fill:#ffcdd2
    style C fill:#c8e6c9
```

### Soluciones a la Paradoja

```mermaid
mindmap
    root((Soluciones<br/>Paradoja<br/>Bertrand))
        Diferenciación
            Productos Diferenciados
            Localización Espacial
        Capacidad
            Restricciones de Capacidad
            Edgeworth
        Dinámica
            Juegos Repetidos
            Colusión Tácita
        Costos
            Costos de Cambio
            Información Imperfecta
```

---

## Modelo de Stackelberg

### Secuencia de Decisiones

```mermaid
sequenceDiagram
    participant L as Líder
    participant M as Mercado
    participant F as Seguidor
    
    Note over L: Etapa 1
    L->>M: Elige q_L primero
    
    Note over F: Etapa 2
    M->>F: Observa q_L
    F->>M: Elige q_F = FR(q_L)
    
    Note over L,F: Equilibrio
    M->>L: π_L > π_Cournot
    M->>F: π_F < π_Cournot
```

### Comparación de Resultados

```mermaid
flowchart LR
    subgraph Cantidades
        QL["q_L = (a-c)/2b"]
        QF["q_F = (a-c)/4b"]
        QC["q_Cournot = (a-c)/3b"]
    end
    
    subgraph Orden
        O1["q_L > q_Cournot > q_F"]
    end
    
    QL --> O1
    QF --> O1
    QC --> O1
    
    style QL fill:#c8e6c9
    style QF fill:#ffcdd2
```

---

## Teoría de Juegos

### Dilema del Prisionero (Colusión)

```mermaid
flowchart TD
    subgraph Matriz["Matriz de Pagos"]
        direction TB
        A["E1 Coopera, E2 Coopera<br/>(5, 5)"]
        B["E1 Coopera, E2 Defecta<br/>(0, 8)"]
        C["E1 Defecta, E2 Coopera<br/>(8, 0)"]
        D["E1 Defecta, E2 Defecta<br/>(2, 2)"]
    end
    
    D --> EN["Equilibrio de Nash<br/>(Defecta, Defecta)"]
    A --> OP["Óptimo de Pareto<br/>(Coopera, Coopera)"]
    
    style D fill:#fff9c4
    style A fill:#c8e6c9
    style EN fill:#ffcdd2
```

### Árbol de Juego Secuencial

```mermaid
flowchart TD
    R[Empresa 1] -->|Alta| A1[Empresa 2]
    R -->|Baja| A2[Empresa 2]
    
    A1 -->|Alta| P1["(2, 2)"]
    A1 -->|Baja| P2["(4, 1)"]
    
    A2 -->|Alta| P3["(1, 4)"]
    A2 -->|Baja| P4["(3, 3)"]
    
    style P4 fill:#c8e6c9
```

---

## 📊 Dashboard: Comparación de Modelos

### Resumen Visual

```mermaid
pie title Distribución del Excedente Total
    "Excedente Consumidor" : 35
    "Beneficio Empresas" : 40
    "Pérdida de Eficiencia" : 25
```

### Jerarquía de Precios

```mermaid
flowchart TB
    subgraph Precios["Orden de Precios por Modelo"]
        PM["P_Monopolio<br/>(Más Alto)"]
        PS["P_Stackelberg"]
        PC["P_Cournot"]
        PB["P_Bertrand = P_Competitivo<br/>(Más Bajo)"]
    end
    
    PM --> PS --> PC --> PB
    
    style PM fill:#ffcdd2
    style PB fill:#c8e6c9
```

---

## 🎨 Uso de Diagramas

Los diagramas Mermaid se renderizan automáticamente en GitHub. Para verlos:
1. Navega a este archivo en GitHub
2. Los diagramas se mostrarán como imágenes interactivas

Para editar o crear nuevos diagramas, consulta la [documentación de Mermaid](https://mermaid.js.org/intro/).
