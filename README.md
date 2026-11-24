# mahdi0082.github.io

Personal portfolio of Mahdi Hasan Bhuiyan, live at https://mahdi0082.github.io (GitHub Pages, served from `main`, root folder).

## Layout

- `index.html`: the whole site. Markup, styles and scripts are in this one file.
- `assets/`: photos, campus images, portrait and favicon.
- `Mahdi_Hasan_Bhuiyan_CV.pdf`: the CV that every "Download CV" button links to.
- `source/cv/make_cv.py`: builds the CV PDF (Python, `reportlab`, Fira Sans fonts).
- `404.html`, `.nojekyll`: GitHub Pages housekeeping.

## Editing notes

- Text that never changes is plain HTML in `index.html`; edit it in place.
- Parts that react to clicks (the federated bilevel optimization demo, the photo viewer, the copy-email button)
  use `{{name}}` placeholders. A small script near the end of `index.html` fills them from
  `Component.renderVals()`, repeats `<sc-for>` blocks and shows `<sc-if>` blocks. Attributes that hold a
  placeholder are written as `data-dc-a-<attribute>`, and click or input handlers as `data-dc-on-<event>`.
- To add a photo: put the file in `assets/`, add a button in the Photography section, and add its entry to
  `this.PHOTOS` in the script.
- To update the CV: edit `source/cv/make_cv.py`, run `python3 source/cv/make_cv.py Mahdi_Hasan_Bhuiyan_CV.pdf`,
  and keep it to one page.
