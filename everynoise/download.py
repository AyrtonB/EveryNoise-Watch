# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01-library-gen.ipynb (unless otherwise specified).

__all__ = ['get_every_noise_canvas', 'extract_canvas_height_width', 'extract_style_elems', 'genre_elem_to_name',
           'get_genre_xy', 'extract_genre_attrs', 'get_df_genre_attrs', 'app', 'download_genre_attrs']

# Cell
import pandas as pd
import typer
import textwrap
import requests
from bs4 import BeautifulSoup as bs

# Cell
def get_every_noise_canvas(everynoise_url='https://everynoise.com/'):
    r = requests.get(everynoise_url)
    soup = bs(r.text, features='lxml')

    canvases = soup.find_all('div', attrs={'class': 'canvas'})
    assert len(canvases) == 1, ''
    canvas = canvases[0]

    return canvas

# Cell
extract_style_elems = lambda genre_elem: {
    style_elem.split(': ')[0].strip(): style_elem.split(': ')[1].replace('px', '')
    for style_elem
    in genre_elem['style'].split(';')
}

def extract_canvas_height_width(canvas):
    canvas_style_elems = extract_style_elems(canvas)

    canvas_height = int(canvas_style_elems['height'])
    canvas_width = int(canvas_style_elems['width'])

    return canvas_height, canvas_width

# Cell
genre_elem_to_name = lambda genre_elem: genre_elem.text.replace('» ', '')

# Cell
def get_genre_xy(genre_style_elems, canvas_width, canvas_height):
    x = int(genre_style_elems['left'].replace('px', ''))
    y = canvas_height - int(genre_style_elems['top'].replace('px', ''))

    return x, y

# Cell
def extract_genre_attrs(genre_elem, canvas_width, canvas_height):
    genre_attrs = {}

    genre_style_elems = extract_style_elems(genre_elem)

    genre_attrs['genre'] = genre_elem_to_name(genre_elem)
    genre_attrs['hex_colour'] = genre_style_elems['color']
    genre_attrs['x'], genre_attrs['y'] = get_genre_xy(genre_style_elems, canvas_width, canvas_height)

    return genre_attrs

# Cell
def get_df_genre_attrs(everynoise_url='https://everynoise.com/'):
    canvas = get_every_noise_canvas(everynoise_url=everynoise_url)
    canvas_height, canvas_width = extract_canvas_height_width(canvas)

    genre_elems = canvas.find_all('div')
    all_genre_attrs = []

    for genre_elem in genre_elems:
        genre_attrs = extract_genre_attrs(genre_elem, canvas_width, canvas_height)
        all_genre_attrs += [genre_attrs]

    df_genre_attrs = pd.DataFrame(all_genre_attrs)

    return df_genre_attrs

# Cell
app = typer.Typer()

# Cell
@app.command()
def download_genre_attrs(fp='data/genre_attrs.csv'):
    # TODO if dir does not exist then create it
    df_genre_attrs = get_df_genre_attrs()
    df_genre_attrs.to_csv(fp, index=False)

    return

# Cell
if __name__ == '__main__' and '__file__' in globals():
    app()