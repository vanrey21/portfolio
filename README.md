# Reyson Angeles — Portfolio

A one-page portfolio generated with Python. `build.py` holds the content (profile, services, case studies, process) and writes `index.html`.

## Edit and preview locally

```bash
python3 build.py
```

Open `index.html` in a browser. No dependencies are needed.

## Publish with GitHub Pages

1. In the repository, open **Settings → Pages**.
2. Set **Source** to **Deploy from a branch**, then choose branch `main` and folder `/ (root)`.
3. The site appears at `https://<your-username>.github.io/<repository-name>/`.

To change the site, edit the data at the top of `build.py`, run `python3 build.py`, and commit both `build.py` and the regenerated `index.html`.
