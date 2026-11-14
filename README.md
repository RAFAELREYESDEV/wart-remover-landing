# Wart Remover 30ml · Landing Page COD Venezuela 🇻🇪

Landing page de alta conversión optimizada para **E-commerce Contra Entrega (Cash On Delivery)** en Venezuela, diseñada bajo la metodología de compra por impulso y estética clínica/Shopify DTC.

---

## 🚀 Características Principales

- **📱 Diseño Mobile-First:** Experiencia optimizada para smartphones con carrusel táctil interactivo (*touch swipe*).
- **💵 Conversión Dinámica BCV en Vivo:** Consulta en tiempo real a la API oficial de [DolarAPI](https://ve.dolarapi.com/v1/dolares/oficial) para calcular automáticamente el total de cada pack en Bolívares.
- **🏢 Directorio Integrado de 134 Sedes Tealca:** Filtro en cascada de `Estado` -> `Ciudad` -> `Sede Tealca Oficial` para retiro en taquilla, además de dirección de entrega obligatoria para despachos directos o couriers alternativos (Zoom/MRW).
- **📲 Checkout Pop-Up a WhatsApp:** Modal directo que envía el pedido estructurado con datos del cliente, paquete, método de pago y ubicación sin fricción.
- **🛡️ Blindaje Legal:** Términos de entrega en 48-72 horas, garantía de transporte, políticas de privacidad y aviso dermatológico.

---

## 🛠️ Stack Tecnológico

- **HTML5 Semántico**
- **Tailwind CSS (CDN)**
- **JavaScript Vanilla (ES6+)**
- **Google Fonts (DM Sans + Playfair Display)**

---

## 📂 Estructura del Proyecto

```text
├── index.html                           # Landing page completa y modal checkout
├── ESTRATEGIA_Y_LANDING_WART_REMOVER.md # Dossier estratégico, pricing y escandallo
├── tealca_master.json                   # Base de datos maestra de sucursales Tealca
├── images/                              # Assets optimizados de producto y hero banner
└── videos_drive/
    └── TRANSCRIPCIONES_VIDEOS_DRIVE.md  # Transcripciones y análisis de videos UGC
```

---

## ⚙️ Despliegue Local

Para previsualizar la landing en tu red local:
```bash
python -m http.server 5500
```
Y abre en tu navegador: `http://localhost:5500/index.html` o desde tu teléfono usando la IP de tu red local.
