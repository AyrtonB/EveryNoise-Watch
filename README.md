# EveryNoise-Watch

[![goodtables.io](https://goodtables.io/badge/github/AyrtonB/EveryNoise-Watch.svg)](https://goodtables.io/github/AyrtonB/EveryNoise-Watch) [![Binder](https://notebooks.gesis.org/binder/badge_logo.svg)](https://notebooks.gesis.org/binder/v2/gh/AyrtonB/EveryNoise-Watch/main?urlpath=lab)

<br>

### Overview

[EveryNoise.com](https://everynoise.com/) is a website that expresses Spotify genres across 3 dimensions, primarily heavy/light and organic/mechanic, with a third 'undefined' colour dimension. Glenn McDonald (Senior Software Engineer at Spotify) is the creator of EveryNoise, the dataset contained in this repository has been derived from his work. You can find more information on how the genres are placed across these dimensions [here](https://everynoise.com/EverynoiseIntro.pdf).

<br>

The `everynoise` Python library can be installed using:

```bash
pip install git+https://github.com/AyrtonB/EveryNoise-Watch
```

<br>

Once the library has been installed you can retrieve the latest dataset by running:

```bash
python -m everynoise.download
```

<br>
<br>

### Dataset Usage

The dataset can be directly downloaded from this repository as a csv, e.g. with:

```python
import pandas as pd
pd.read_csv('https://raw.githubusercontent.com/AyrtonB/EveryNoise-Watch/main/data/genre_attrs.csv')
```

Below is an example of the first five columns in the resulting DataFrame

| genre                      |    x |    y |   r |   g |   b |
|:---------------------------|-----:|-----:|----:|----:|----:|
| piano blues                |  696 | 3870 | 102 | 136 |  45 |
| australian classical piano | 1105 |  613 |  28 | 163 | 194 |
| histoire pour enfants      |  454 | 5661 |  86 | 134 |   8 |
| dutch musical              | 1067 | 6080 | 118 | 140 |  20 |
| blues                      |  600 | 3971 | 105 | 134 |  32 |

<br>

The raw csv dataset is accompanied by a json file detailing it's metadata. This has been created using the Frictionless Data Table Schema, with the two files forming a Frictionless Data Package. This packaged dataset can be loaded using the `datapackage` library.

```python
# Imports
import pandas as pd
import datapackage

# Data Retrieval
url = 'https://raw.githubusercontent.com/AyrtonB/EveryNoise-Watch/main/data/datapackage.json'
dp = datapackage.Package(url)

# DataFrame Loading
df_genre_attrs = pd.DataFrame(dp.resources[0].read(keyed=True))
```

<br>

Which also exposes the metadata in a machine-readable form, e.g.

```python
dp.descriptor['description']

>>> 'This dataset is downloaded from everynoise.com and expresses Spotify genres across 5 dimensions, primarily heavy/light and organic/mechanic. Glenn McDonald (Senior Software Engineer at Spotify) is the creator of EveryyNoise, this dataset has been derived from his work.'
```
