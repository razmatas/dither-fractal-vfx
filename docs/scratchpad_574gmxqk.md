# Dither Tool Analysis: https://dither.neato.fun/

## UI Layout & Structure
- **Sidebar (Left)**: Segmented into sections: Source, Pattern, Parameters, Palette, and Export.
- **Main Preview (Center)**: A large SVG/Canvas rendering of the dithered result. The layout is responsive but generally keeps controls on the left.

## Detailed Controls & Parameters
### Source
- **Load Image**: Standard file input for local images.
- **Gradient Sections (or generate)**:
    - `Type`: Linear, Radial, Conic, Noise.
    - `Angle`: 0° to 360° (rotates the gradient).
    - `Size`: 1:1, 4:3, 16:9, 3:2, 2:1, etc.
    - `Width`: Controls the resolution of the generated grid (256-2048px).

### Pattern
- **Type**:
    - `Bayer 2x2/4x4/8x8`: Ordered dithering using standard matrices.
    - `Halftone`: Circular clusters centered in cells.
    - `Lines`: Horizontal/Vertical scanlines.
    - `Crosses`: Intersecting grid lines.
    - `Dots`: Similar to halftone but can be styled differently.
    - `Grid`: Square grid patterns.
    - `Scales`: Fish-scale / overlapping semi-circles.
- **Mode**: Switches the source between `Image` and the generated `Gradients`.
- **Style**:
    - `Threshold`: Binary (or discrete) choice of color based on threshold.
    - `Scaled`: Sizes the shape (Circle/Square/Diamond) based on the cell's brightness.
- **Shape**: `Square`, `Circle`, `Diamond`.

### Parameters
- `Cell Size`: 2px to 64px. Determines the "pixelation" level.
- `Scale`: (Appears for Radial/Conic) Adjusts the frequency/spread of the gradient.
- `Offset X / Y`: (Appears for Radial/Conic) Pans the center point of the gradient.

### Palette
- `Colors`: Select 2 to 8 colors.
- `Color Pickers`: Hex/RGB input for each slot.
- `Weight Sliders`: Percentages (0-100%) that define the threshold boundaries for each color in the luminance range.
- `Presets`: B/W, GameBoy, CGA, Sepia.

## Technical Implementation (Logic)
- **Luminance Calculation**: `(0.299 * R + 0.587 * G + 0.114 * B) / 255`.
- **Dithering Logic**:
    - The code calculates a `threshold` value `[0, 1]` for each cell based on the selected `Pattern Type` and the cell's `(x, y)` coordinates.
    - It maps the cell's `brightness` to a color by comparing `adjustedBrightness = brightness + (threshold - 0.5) * 0.5` against cumulative palette percentages.
- **Rendering Pipeline**:
    - The tool iterates through a grid of cells.
    - For each cell, it determines the color and (if in `Scaled` mode) the size factor.
    - It groups cells by color to minimize SVG group tags.
    - It generates a large SVG string containing `<circle>`, `<rect>`, or `<polygon>` elements.

## Export & Output
- **SVG**: Scalable vector graphics, ideal for print/plotters.
- **PNG**: Rasterized version of the SVG.
