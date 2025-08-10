import marimo

__generated_with = "0.14.16"
app = marimo.App(width="columns", sql_output="lazy-polars")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import altair as alt
    import matplotlib
    import matplotlib.pyplot as plt
    from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
    import math
    import scipy.stats as st
    return mo, plt


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
    ##**_Kolmogorov's Axioms_**
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
    mo.md(
        r"""
    ##**_Probability Operations_**

    ###**_A. Union of Events_**
    ###**_B. Intersection of Events_**
    ###**_C. Compliment of Events_**
    ###**_D. Mutually Exclusive Events_**
    ###**_E. Exhaustive, Mutually Exclusive Events_**
    ###**_F. Combinations of Operators_**
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ##**_Bayesian Formula_**

    $$
    P(A|+) : \frac{P(+|A).P(A)}{P(+|A).P(A)+P(+|A^c).P(A^c)}
    $$

    $P(A)$ : Probability of Model Happening **(Prior)**

    $P(A^c)$ : Probability of Model **Not** Happening

    $P(+|A)$ : Probability of Positive Result New Data given Model Happening **(Likelihood)**

    $P(+|A^c)$ : Probability of Positive Result New Data given Model **Not** Happening

    $P(-|A)$ : Probability of **Not** Positive Result New Data given Model Happening

    $P(-|A^c)$ : Probability of **Not** Positive Result New Data given Model **Not** Happening

    $P(A|+)$ : Probability of Model Happening given Positive New Data **(Posterior)**
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""##**_Interactive Bayesian Updating_**""")
    return


@app.cell
def _(mo):
    # Slider (Probability Model)
    s_p1 = mo.ui.slider(start=0, stop=1, step=0.01, label="**_P(A)_**", value = 0.65)
    # Slider (Probability New Data Positive given happening model)
    s_p2 = mo.ui.slider(start=0, stop=1, step=0.01, label="**_P(+|A)_**", value = 0.4)
    # Slider (Probability New Data Positive given not happening model)
    s_p3 = mo.ui.slider(start=0, stop=1, step=0.01, label="**_P(+|$A^c$)_**", value = 0.25)
    return s_p1, s_p2, s_p3


@app.cell
def _(s_p1, s_p2, s_p3):
    p1 = s_p1.value
    p2 = s_p2.value
    p3 = s_p3.value
    return p1, p2, p3


@app.cell
def _(mo, s_p1, s_p2, s_p3):
    slider = mo.hstack([s_p1,s_p2,s_p3])
    return (slider,)


@app.cell
def _(mo, s_p1, s_p2, s_p3):
    value_p_choose = mo.hstack([mo.md(f"**_P(A)_ **has value **{s_p1.value}**"),mo.md(f"**_P(+|A)_ **has value **{s_p2.value}**"),mo.md(f"**_P(+|$A^c$)_ **has value **{s_p3.value}**")])
    return (value_p_choose,)


@app.cell
def _(p1, p2, p3):
    #p_negative_given_happen
    p_min_g_happen = 1 - p2
    #p_negative_given_not_happen
    p_min_g_not_happen = 1 - p3
    #p_not_happening
    p_not_happen = 1 - p1
    return p_min_g_happen, p_min_g_not_happen, p_not_happen


@app.cell
def _(mo, p_min_g_happen, p_min_g_not_happen, p_not_happen):
    value_p_depend = mo.hstack([mo.md(f"**_P($A^c$) = 1 - P(A)_  **has value **{p_not_happen:.2f}**"),mo.md(f"**_P(-|A) = 1 - P(+|A)_ **has value **{p_min_g_happen:.2f}**"),mo.md(f"**_P(-|$A^c$) = 1 - P(+|$A^c$)_ **has value **{p_min_g_not_happen:.2f}**")])
    return (value_p_depend,)


@app.cell
def _(p1, p2, p3, p_not_happen):
    #Calculation
    p_result = (p2*p1)/((p2*p1)+(p3*p_not_happen))
    return (p_result,)


@app.cell
def _(p1, p2, p_result):
    posterior = p_result
    prior = p1
    likelihood = p2
    return likelihood, posterior, prior


@app.cell
def _(likelihood, plt, posterior, prior):
    fig, ax = plt.subplots(1,1, figsize = (12,0.5))

    ax.plot(posterior, 0.5,"kD", label = "Posterior", markersize = 10)
    ax.plot(prior, 0.5,"bs", label = "Prior", markersize = 15)
    ax.plot(likelihood, 0.5,"ro", label = "Likelihood", markersize = 15)
    ax.set_xlabel("Probability")
    ax.legend(bbox_to_anchor=(1.05, -0.8), borderaxespad=0., fontsize = 12)
    ax.set_xlim(0.00,1.00)
    ax.get_yaxis().set_visible(False)
    return (fig,)


@app.cell
def _(likelihood, mo, posterior, prior):
    output = mo.vstack([mo.md(f"**_Posterior_  **has value **{posterior:.2f}**"),mo.md(f"**_Likelihood_ **has value **{likelihood:.2f}**"),mo.md(f"**_Prior_ **has value **{prior:.2f}**")])
    return (output,)


@app.cell
def _(fig, mo, output, slider, value_p_choose, value_p_depend):
    mo.vstack([slider, value_p_choose, value_p_depend, fig, output])
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
