import math
import time
import sys
import os
import shutil
import signal
import select
import tty
import termios

# --- High-Fidelity Color Palettes from fractal_spec.md ---

COBALT_HEX = ["#031438", "#07245C", "#0F3880", "#1A52A8", "#2B6FCC", "#4A8FDE", "#7BB3E8", "#AECFEE", "#D6E4F5", "#EEF3FB"]
CRIMSON_HEX = ["#380303", "#5C0808", "#801010", "#A31E1E", "#C43030", "#D45E5E", "#E08E8E", "#EDB8B8", "#F5D8D8", "#FBF0F0"]

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

COBALT_RGB = [hex_to_rgb(h) for h in COBALT_HEX]
CRIMSON_RGB = [hex_to_rgb(h) for h in CRIMSON_HEX]
# Create a smooth cyclical palette
COMBINED_RGB = COBALT_RGB + CRIMSON_RGB[::-1] + CRIMSON_RGB + COBALT_RGB[::-1]

PALETTES = {
    "Deep Cobalt": COBALT_RGB,
    "Crimson Ember": CRIMSON_RGB,
    "Fractal Wave": COMBINED_RGB,
}

class AdvancedPlasma:
    def __init__(self):
        self.palette_name = "Fractal Wave"
        self.palette = PALETTES[self.palette_name]
        self.running = True
        
        # Physics & Look
        self.speed = 1.0
        self.zoom = 1.0
        self.contrast = 1.4  # Higher contrast for "glow"
        self.complexity = 1.0
        
        # State
        self.show_hud = True
        self.t = 0.0
        
        # ANSI
        self.HIDE_CURSOR = "\033[?25l"
        self.SHOW_CURSOR = "\033[?25h"
        self.HOME = "\033[H"
        self.CLEAR = "\033[2J"
        self.RESET = "\033[0m"

    def stop(self, signum=None, frame=None):
        self.running = False

    def get_color_raw(self, val):
        # Apply contrast curve (sigmoid-like)
        val = 1.0 / (1.0 + math.exp(-10 * (val - 0.5) * self.contrast))
        
        ps = len(self.palette)
        idx = val * (ps - 1)
        i1 = int(idx)
        i2 = min(i1 + 1, ps - 1)
        f = idx - i1
        
        c1, c2 = self.palette[i1], self.palette[i2]
        return (
            int(c1[0] + (c2[0] - c1[0]) * f),
            int(c1[1] + (c2[1] - c1[1]) * f),
            int(c1[2] + (c2[2] - c1[2]) * f)
        )

    def calculate_pixel(self, x, y, t):
        # Multi-layered "Fractal" Plasma Formula
        # Layer 1: Base Waves
        v = math.sin(x * 0.1 * self.zoom + t)
        v += math.sin(y * 0.15 * self.zoom + t * 0.5)
        
        # Layer 2: Moving Center
        cx = x + 0.5 * math.sin(t / 5.0) * 20
        cy = y + 0.5 * math.cos(t / 3.0) * 20
        v += math.sin(math.sqrt(cx*cx + cy*cy + 1) * 0.1 * self.zoom)
        
        # Layer 3: Interference
        v += math.sin((x + y) * 0.05 * self.zoom + t)
        v += math.sin(math.sqrt(x*x + y*y + 1) * 0.02 * self.zoom + t * 0.2)
        
        # Normalize to 0..1
        return (v + 4.0) / 8.0

    def render(self, width, height):
        output = [self.HOME]
        
        # Half-block rendering: 1 character = 2 vertical pixels
        # Top pixel is Background color, Bottom pixel is Foreground color of '▄'
        for y in range(0, height * 2, 2):
            line = []
            for x in range(width):
                # Sample top pixel
                v_top = self.calculate_pixel(x, y, self.t)
                r1, g1, b1 = self.get_color_raw(v_top)
                
                # Sample bottom pixel
                v_bot = self.calculate_pixel(x, y + 1, self.t)
                r2, g2, b2 = self.get_color_raw(v_bot)
                
                # ANSI: \033[38;2;R;G;Bm (Foreground) \033[48;2;R;G;Bm (Background)
                line.append(f"\033[48;2;{r1};{g1};{b1}m\033[38;2;{r2};{g2};{b2}m▄")
            output.append("".join(line))
            output.append("\033[0m\n") # Reset color at end of line
            
        # HUD
        if self.show_hud:
            hud = f"\033[2;2H\033[1;37;48;5;235m MODE: {self.palette_name} | ZOOM: {self.zoom:.2f} | SPEED: {self.speed:.2f} | [Q] Quit [P] Palette [+/-] Zoom [H] Hide \033[0m"
            output.append(hud)

        sys.stdout.write("".join(output))
        sys.stdout.flush()

    def handle_input(self):
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            char = sys.stdin.read(1).lower()
            if char == 'q': self.running = False
            elif char == 'p':
                keys = list(PALETTES.keys())
                self.palette_name = keys[(keys.index(self.palette_name) + 1) % len(keys)]
                self.palette = PALETTES[self.palette_name]
            elif char == '=' or char == '+': self.zoom *= 1.1
            elif char == '-' or char == '_': self.zoom /= 1.1
            elif char == ']': self.speed *= 1.2
            elif char == '[': self.speed /= 1.2
            elif char == 'h': self.show_hud = not self.show_hud

    def run(self):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            sys.stdout.write(self.HIDE_CURSOR + self.CLEAR)
            while self.running:
                start = time.time()
                w, h = shutil.get_terminal_size()
                self.handle_input()
                self.render(w, h - 1) # h-1 to leave room for terminal prompt
                self.t += 0.05 * self.speed
                # Control frame rate
                wait = 0.02 - (time.time() - start)
                if wait > 0: time.sleep(wait)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
            sys.stdout.write(self.SHOW_CURSOR + self.RESET + self.CLEAR + self.HOME)

if __name__ == "__main__":
    AdvancedPlasma().run()
