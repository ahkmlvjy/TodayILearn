import marimo

__generated_with = "0.14.16"
app = marimo.App(width="columns", sql_output="lazy-polars")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import altair as alt
    import matplotlib.pyplot as plt
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #**_Probability Concepts_**

    (Michael J. Pyrcz, 2024)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ###_**A. Non-negativity**_
    $P(A)&ge;0$
    ###_**B. Normalization**_
    $P(\Omega)=1$
    ###_**C. Additivity**_
    $P(A_i)=\sum{P(A_i)}$
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""##**_Probability Operations_**""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #**_Refferences_**

    - Pyrcz, M.J., 2024, Applied Geostatistics in Python: a Hands-on Guide with GeostatsPy [e-book]. Zenodo. doi:10.5281/zenodo.15169133 DOI

    - Pyrcz, M.J., 2024, GeostatsPyDemos: GeostatsPy Python Package for Spatial Data Analytics and Geostatistics Demonstration Workflows Repository (0.0.1) [Software]. Zenodo. doi:10.5281/zenodo.12667036. GitHub Repository: GeostatsGuy/GeostatsPyDemos DOI
    """
    )
    return


if __name__ == "__main__":
    app.run()
