# Reyson Angeles — Portfolio

A one-page portfolio generated with Python. `build.py` holds the content (profile, services, case studies, process) and writes `index.html`.

## Edit and preview locally

```bash
python3 build.py
```

Open `index.html` in a browser. No dependencies are needed.

## Publish with GitHub Pages

1. Create a new empty repository on GitHub (for example `portfolio`).
2. Upload or push these files: `build.py`, `README.md` and `.github/workflows/pages.yml`.
3. In the repository, go to **Settings → Pages** and set **Source** to **GitHub Actions**.
4. Push to the `main` branch. The workflow runs `build.py` and deploys the site.

The public address appears in the workflow run and under Settings → Pages, usually `https://<your-username>.github.io/<repository-name>/`.

To change the site, edit the data at the top of `build.py` and push again.
