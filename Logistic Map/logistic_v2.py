import marimo

__generated_with = "0.21.1"
app = marimo.App(width="full")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt


    # ---------- HEADER ----------
    return mo, np, plt


@app.cell
def _(mo):
    title = mo.md(
            r"""
    # Interactive Exploration of the Logistic Map  
    ### Bifurcation and Chaos

    \[
    x_{n+1} = r x_n (1 - x_n)
    \]
    """
        )


    # ---------- THEORY ----------
    return (title,)


@app.cell
def _(mo):
    theory = mo.md(
            r"""
    ### Regimes of Behavior

    - **\(0 < r < 1\)** → Extinction  
    - **\(1 < r < 3\)** → Stable fixed point  
    - **\(3 < r < 3.57\)** → Period doubling  
    - **\(r > 3.57\)** → Chaos  
    """
        )


    # ---------- CONTROLS ----------
    return (theory,)


@app.cell
def _(mo):
    x0 = mo.ui.number(value=0.1, label="Initial condition (x₀)")
    nb = mo.ui.number(value=1000, label="Bifurcation steps (n_b)")
    nl = mo.ui.number(value=200, label="Logistic steps (n_l)")
    r = mo.ui.number(value=3.2, label="Control parameter (r)")
    last = mo.ui.number(value=100, label="Samples (steady-state)")

    controls = mo.vstack([x0, nb, nl, r, last], gap=1)



    # ---------- COMPUTATION + PLOTS ----------
    return controls, last, nb, nl, r, x0


@app.cell
def _(last, nb, nl, np, plt, r, x0):
    x0v = x0.value
    n_b = nb.value
    n_l = nl.value
    r0 = r.value
    lastv = last.value

    fig, ax = plt.subplots(1, 2, figsize=(14, 5))

    # -------- Bifurcation --------
    rvals = np.linspace(0, 4, n_b)
    A = np.zeros((n_b, n_b))
    A[0, :] = x0v

    for i in range(n_b):
        for j in range(1, n_b):
            A[j, i] = rvals[i] * A[j - 1, i] * (1 - A[j - 1, i])

    for j in range(n_b - lastv, n_b):
        ax[1].plot(rvals, A[j, :], ',k', alpha=0.6)

    ax[1].axvline(x=r0, linestyle='--', color='red')
    ax[1].set_title("Bifurcation Diagram")
    ax[1].set_xlabel("r")
    ax[1].set_ylabel("x")

    # -------- Logistic map --------
    x = np.zeros(n_l)
    x[0] = x0v

    for i in range(1, n_l):
        x[i] = r0 * x[i - 1] * (1 - x[i - 1])

    ax[0].plot(x, color='orange', alpha=0.3)
    ax[0].plot(x, linestyle='None', marker='o', color='blue', markersize=3)

    ax[0].set_title("Logistic Map Evolution")
    ax[0].set_xlabel("n")
    ax[0].set_ylabel("x")
    ax[0].set_ylim(0, 1)

    fig.tight_layout()



    # ---------- FINAL LAYOUT ----------
    return (fig,)


@app.cell
def _(controls, fig, mo, theory, title):
    layout = mo.vstack([
        title,
        theory,
        mo.hstack([
            controls,
            fig
        ], widths=[1, 3], gap=2)
    ])

    layout
    return


if __name__ == "__main__":
    app.run()
