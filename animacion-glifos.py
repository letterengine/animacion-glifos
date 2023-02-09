'''Pasar todos los glifos de una fuente'''

# Módulos
import os
from fontTools.ttLib import TTFont

# Canvas
w, h = 1920, 1080
bg = (0.5, 0, 0.5)

# Rutas
usuario = os.path.expanduser('~')
escritorio = os.path.join(usuario, 'Desktop')
folder = os.path.split(__file__)[0]
fuentes = [f for f in os.listdir(folder) if '.ttf' in f or '.otf' in f]
fuente = os.path.join(folder, fuentes[0])
otf = TTFont(fuente)
glifos = otf.getGlyphOrder()

# Corrida

for glifo in glifos:
    newPage(w, h)
    with savedState(): fill(*bg), rect(0, 0, w, h)
    g = FormattedString('', font=fuente, fill=1, fontSize=400, align='center')
    g.appendGlyph(glifo)
    text(g, (w/2, h/2 + g.fontDescender()))

# Guardado

gif =  os.path.join(escritorio, 'glifos.gif')   
saveImage(gif)