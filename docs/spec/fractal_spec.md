# fractal_spec.md
> Colour palette reference for plasma/fractal terminal effects

---

## Palette A — Cobalt Depth (Blue)

A cool, high-contrast blue ramp from near-white to deep navy. Use for plasma wave crests, electric field lines, or cold-temperature zones.

| Swatch | Name | Hex |
|--------|------|-----|
| ![](https://via.placeholder.com/20/EEF3FB/EEF3FB) | Frost | `#EEF3FB` |
| ![](https://via.placeholder.com/20/D6E4F5/D6E4F5) | Ice | `#D6E4F5` |
| ![](https://via.placeholder.com/20/AECFEE/AECFEE) | Mist | `#AECFEE` |
| ![](https://via.placeholder.com/20/7BB3E8/7BB3E8) | Sky | `#7BB3E8` |
| ![](https://via.placeholder.com/20/4A8FDE/4A8FDE) | Cobalt | `#4A8FDE` |
| ![](https://via.placeholder.com/20/2B6FCC/2B6FCC) | Royal | `#2B6FCC` |
| ![](https://via.placeholder.com/20/1A52A8/1A52A8) | Sapphire | `#1A52A8` |
| ![](https://via.placeholder.com/20/0F3880/0F3880) | Midnight | `#0F3880` |
| ![](https://via.placeholder.com/20/07245C/07245C) | Abyss | `#07245C` |
| ![](https://via.placeholder.com/20/031438/031438) | Void | `#031438` |

### Usage in Effects
- **Plasma base layer**: Animate through `Frost → Sky → Cobalt` for wave motion
- **Field lines / lightning**: Use `Royal → Void` for sharp, high-contrast streaks
- **Glow bloom**: Layer `Cobalt` at low opacity over `Midnight` background

---

## Palette B — Crimson Ember (Red)

A warm, saturated red ramp from blush white to deep blood crimson. Use for heat-map zones, chaotic fractal edges, or high-energy particle bursts.

| Swatch | Name | Hex |
|--------|------|-----|
| ![](https://via.placeholder.com/20/FBF0F0/FBF0F0) | Blush White | `#FBF0F0` |
| ![](https://via.placeholder.com/20/F5D8D8/F5D8D8) | Rose Tint | `#F5D8D8` |
| ![](https://via.placeholder.com/20/EDB8B8/EDB8B8) | Petal | `#EDB8B8` |
| ![](https://via.placeholder.com/20/E08E8E/E08E8E) | Blush | `#E08E8E` |
| ![](https://via.placeholder.com/20/D45E5E/D45E5E) | Coral Red | `#D45E5E` |
| ![](https://via.placeholder.com/20/C43030/C43030) | Crimson | `#C43030` |
| ![](https://via.placeholder.com/20/A31E1E/A31E1E) | Scarlet | `#A31E1E` |
| ![](https://via.placeholder.com/20/801010/801010) | Blood | `#801010` |
| ![](https://via.placeholder.com/20/5C0808/5C0808) | Maroon | `#5C0808` |
| ![](https://via.placeholder.com/20/380303/380303) | Ember | `#380303` |

### Usage in Effects
- **Heat zones**: Map `Blush → Coral Red` to high-frequency oscillation regions
- **Fractal edges**: Use `Crimson → Ember` for sharp boundary contrast
- **Particle decay**: Fade `Scarlet → Ember` for trailing particle effects

---

## Combined Gradient Ramps

For dual-palette plasma effects (e.g. blue-cold vs red-hot zones):

```
Cold  →  Warm
#4A8FDE → #C43030   (Cobalt to Crimson)
#031438 → #380303   (Void to Ember)
#7BB3E8 → #E08E8E   (Sky to Blush)
```

---

## Terminal ANSI Approximations

For terminal rendering, map to closest 256-colour ANSI codes:

| Palette | Light end | Mid | Dark end |
|---------|-----------|-----|----------|
| Cobalt  | `\e[38;5;153m` | `\e[38;5;69m` | `\e[38;5;17m` |
| Crimson | `\e[38;5;224m` | `\e[38;5;160m` | `\e[38;5;52m` |

---

*Reference this file as `@fractal_spec.md` in prompts to apply these palettes to plasma/fractal terminal scripts.*
