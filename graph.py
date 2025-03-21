import matplotlib.pyplot as plt


def plot_line_graph(x: list[float], y: list[float]) -> None:
    """
    Plot a line graph of y against x
    Args:
    - x (list[float]): List of x values (required)
    - y (list[float]): List of y values (required)
    """
    plt.plot(x, y)
    plt.savefig("test.png")
    return None
