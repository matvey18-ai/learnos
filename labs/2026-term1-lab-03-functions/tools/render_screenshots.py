"""Рендер «скриншотов» терминала для лабораторной работы №3.

Скрипт читает исходники taskNN.py и реальные выводы из output/taskNN.txt
(получены запуском в PowerShell) и рисует PNG в стиле окна консоли:
команда Get-Content + код, затем команда запуска + вывод программы.
Запуск: py tools/render_screenshots.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

LAB = Path(__file__).resolve().parent.parent
SCREENSHOTS = LAB / "screenshots"
PROMPT = r"PS C:\Users\isil7\OneDrive\Документы\learnos-main\labs\2026-term1-lab-03-functions> "

BG = (12, 12, 12)
C_PROMPT = (118, 118, 118)
C_COMMAND = (238, 238, 238)
C_CODE = (152, 168, 152)
C_OUTPUT = (208, 208, 208)
C_ERROR = (224, 108, 96)
PAD = 14
LINE_GAP = 6
FONT_SIZE = 15

ERROR_MARKERS = ("Traceback", "Error:", 'File "', "^")


def load_font(path: str, size: int, fallback: str) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.truetype(fallback, size)


def classify(line: str) -> tuple[int, int, int]:
    stripped = line.lstrip()
    if any(stripped.startswith(m) for m in ("Traceback", "NameError", "TypeError", "ValueError")):
        return C_ERROR
    if stripped.startswith("^") or (stripped.startswith("File") and stripped.endswith('"')):
        return C_ERROR
    if "Error:" in line:
        return C_ERROR
    return C_OUTPUT


def build_lines(task: str) -> list[tuple[str, tuple[int, int, int], bool]]:
    source = (LAB / f"task{task}.py").read_text(encoding="utf-8").splitlines()
    output = (LAB / "output" / f"task{task}.txt").read_text(encoding="utf-8").splitlines()
    run_cmd = "echo 6.4 | py task{}.py" if task == "12" else "py task{}.py"

    lines: list[tuple[str, tuple[int, int, int], bool]] = []
    lines.append((PROMPT + f"Get-Content task{task}.py", C_PROMPT, True))
    for code_line in source:
        lines.append((code_line or " ", C_CODE, False))
    lines.append(("", C_OUTPUT, False))
    lines.append((PROMPT + run_cmd.format(task), C_PROMPT, True))
    for out_line in output:
        lines.append((out_line or " ", classify(out_line), False))
    lines.append((PROMPT + "█", C_PROMPT, True))
    return lines


def render(task: str) -> Path:
    lines = build_lines(task)
    font = load_font(r"C:\Windows\Fonts\consola.ttf", FONT_SIZE, r"C:\Windows\Fonts\cour.ttf")
    bold = load_font(r"C:\Windows\Fonts\consolab.ttf", FONT_SIZE, r"C:\Windows\Fonts\courbd.ttf")

    def width_of(text: str, is_cmd: bool) -> float:
        return (bold if is_cmd else font).getlength(text)

    text_w = max(width_of(t, is_cmd) for t, _, is_cmd in lines)
    ascent, descent = font.getmetrics()
    line_h = ascent + descent + LINE_GAP
    img_w = int(text_w) + 2 * PAD
    img_h = len(lines) * line_h + 2 * PAD

    img = Image.new("RGB", (img_w, img_h), BG)
    draw = ImageDraw.Draw(img)
    y = PAD
    for text, color, is_cmd in lines:
        if text:
            fnt = bold if is_cmd else font
            if is_cmd:
                prompt_w = width_of(PROMPT, True)
                draw.text((PAD, y), PROMPT, font=fnt, fill=C_PROMPT)
                draw.text((PAD + prompt_w, y), text[len(PROMPT):], font=fnt, fill=C_COMMAND)
            else:
                draw.text((PAD, y), text, font=fnt, fill=color)
        y += line_h

    SCREENSHOTS.mkdir(exist_ok=True)
    out = SCREENSHOTS / f"task{task}.png"
    img.save(out)
    return out


if __name__ == "__main__":
    for n in range(1, 13):
        path = render(f"{n:02d}")
        print("saved", path.name, path.stat().st_size, "bytes")
