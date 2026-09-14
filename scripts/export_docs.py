from base64 import b64decode
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = ROOT / "notebooks" / "APS1_Airbnb_EDA.ipynb"
DOCS_DIR = ROOT / "docs"
IMAGES_DIR = DOCS_DIR / "assets" / "images"

FIGURE_NAMES = [
    "distribuicao-preco.png",
    "distribuicoes-numericas.png",
    "frequencias-categoricas.png",
    "matriz-correlacao.png",
    "relacoes-numericas.png",
    "preco-por-categoria.png",
    "medianas-bairros.png",
    "numericas-por-categoria.png",
    "pca-room-type.png",
]


def main():
    notebook = nbformat.read(NOTEBOOK_PATH, as_version=4)
    image_outputs = []

    for cell in notebook.cells:
        for output in cell.get("outputs", []):
            png_data = output.get("data", {}).get("image/png")
            if png_data:
                image_outputs.append(png_data)

    if len(image_outputs) != len(FIGURE_NAMES):
        raise RuntimeError(
            f"Esperadas {len(FIGURE_NAMES)} figuras, "
            f"mas foram encontradas {len(image_outputs)}."
        )

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    for filename, encoded_image in zip(
        FIGURE_NAMES,
        image_outputs,
        strict=True,
    ):
        (IMAGES_DIR / filename).write_bytes(b64decode(encoded_image))

    exporter = HTMLExporter(template_name="lab")
    html, _ = exporter.from_notebook_node(notebook)
    (DOCS_DIR / "notebook-completo.html").write_text(
        html,
        encoding="utf-8",
    )

    print(f"{len(image_outputs)} figuras exportadas.")
    print("Notebook HTML exportado para docs/notebook-completo.html.")


if __name__ == "__main__":
    main()
