"""Export the executed APS2 notebook and its tagged figures to MkDocs."""

from base64 import b64decode
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = ROOT / "notebooks" / "APS2_Airbnb_Regressao.ipynb"
DOCS_DIR = ROOT / "docs" / "aps2"
IMAGES_DIR = ROOT / "docs" / "assets" / "images" / "aps2"
FIGURES = {
    "aps2-learning": "curva-aprendizado.png",
    "aps2-real-vs-prev": "reais-vs-previstos.png",
    "aps2-residual-scatter": "residuos-vs-previstos.png",
    "aps2-residual-hist": "distribuicao-residuos.png",
    "aps2-shap-global": "shap-colunas.png",
    "aps2-shap-group": "shap-variaveis.png",
    "aps2-shap-case-low": "shap-caso-baixo.png",
    "aps2-shap-case-mid": "shap-caso-mediano.png",
    "aps2-shap-case-high": "shap-caso-alto.png",
}


def main():
    notebook = nbformat.read(NOTEBOOK_PATH, as_version=4)
    found = {}
    for cell in notebook.cells:
        tags = set(cell.get("metadata", {}).get("tags", []))
        matching = tags.intersection(FIGURES)
        for tag in matching:
            png_outputs = [
                output.get("data", {}).get("image/png")
                for output in cell.get("outputs", [])
                if output.get("data", {}).get("image/png")
            ]
            if len(png_outputs) != 1:
                raise RuntimeError(
                    f"A célula {tag} deve produzir exatamente uma figura PNG; "
                    f"encontradas: {len(png_outputs)}."
                )
            if tag in found:
                raise RuntimeError(f"Tag de figura duplicada: {tag}")
            found[tag] = png_outputs[0]

    if found.keys() != FIGURES.keys():
        missing = FIGURES.keys() - found.keys()
        raise RuntimeError(f"Figuras ausentes no notebook executado: {sorted(missing)}")

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    for tag, filename in FIGURES.items():
        (IMAGES_DIR / filename).write_bytes(b64decode(found[tag]))

    exporter = HTMLExporter(template_name="lab")
    html, _ = exporter.from_notebook_node(notebook)
    (DOCS_DIR / "notebook-completo.html").write_text(html, encoding="utf-8")
    print(f"{len(FIGURES)} figuras e o notebook HTML foram exportados.")


if __name__ == "__main__":
    main()
