# 🧪 Dither Fractal VFX

A high-performance, interactive 2D Canvas fractal plasma animation with a comprehensive post-processing dithering engine and custom palette editor.

![Dither Fractal VFX Preview](https://github.com/razmatas/dither-fractal-vfx/raw/main/docs/preview.png) *(Placeholder: You can replace this with a real screenshot/GIF)*

## ✨ Features

- **🌀 Fractal Plasma Engine**: Real-time animated fractal gradients with controllable speed, magnification (zoom), and contrast.
- **🏁 Advanced Dither Engine**: Comprehensive post-processing inspired by classic ordered dithering and halftone techniques.
  - **Patterns**: Bayer (2x2, 4x4, 8x8), Radial Halftone, and Pseudo-random Noise.
  - **Styles**: `Threshold` (binary mapping) and `Scaled` (size-based mapping/halftone).
  - **Shapes**: Render each cell as a `Square`, `Circle`, or `Diamond`.
- **🎨 Custom Palette Editor**:
  - Hand-pick between 2 and 8 color stops.
  - Interactive color picker and hex code input.
  - Quick-start presets: `B/W`, `GameBoy`, `CGA`, `Sepia`, and `Neon`.
- **🖥️ Responsive HUD**: A sleek, translucent control panel to override system parameters in real-time.

## 🚀 Getting Started

No build step required. This project is built using pure Vanilla JavaScript and HTML5 Canvas.

1. Clone this repository.
2. Open `index.html` in any modern web browser.

## ⌨️ Controls

### UI Panel (HUD)
- **Color Engine**: Select built-in palettes or switch to `CUSTOM` to unlock the palette editor.
- **Block Size**: Adjust the resolution/pixelation of the output.
- **Dither Strength**: Blend between the raw plasma and the dithered output.
- **Dither Colors**: Quantize the output to a specific number of color levels.

### Keyboard Shortcuts
- **[H]**: Toggle the System Override HUD visibility.

## 🛠️ Built With
- **HTML5 Canvas** (2D Context)
- **Vanilla JavaScript** (ES6+)
- **CSS3** (Glassmorphism & Custom UI)

## 💡 Inspiration
- [dither.neato.fun](https://dither.neato.fun/) for the UI pattern and dithering concepts.
- Classic **Bayer Ordered Dithering** algorithms for the 8x8 matrix logic.

---
Built with ❤️ by Antigravity.
