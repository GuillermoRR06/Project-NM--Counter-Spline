import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# Widget para mostrar el gráfico
class GraphWidget(FigureCanvasQTAgg):

    def __init__(self, parent=None):
        self.figure = Figure(figsize=(6, 4))
        super().__init__(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.draw_graph()

    def draw_graph(self):
        self.figure.patch.set_facecolor("#151F32")
        self.ax.clear()
        self.ax.set_facecolor("#0B1120")

        x = np.linspace(-5, 5, 300)
        y = 0.15 * x**3 - x

        self.ax.plot(
            x, y,
            color="#00D9FF",
            linewidth=2,
            label="Test trajectory"
        )

        self.ax.axhline(0, color="#52647D", linewidth=0.8)
        self.ax.axvline(0, color="#52647D", linewidth=0.8)

        self.ax.grid(
            True,
            color="#293B55",
            linestyle="--",
            alpha=0.7
        )

        self.ax.tick_params(colors="#91A4BD")
        self.ax.set_xlabel("X", color="#EAF2FF")
        self.ax.set_ylabel("Y", color="#EAF2FF")
        self.ax.set_title("Function Mapping", color="#00D9FF")

        for spine in self.ax.spines.values():
            spine.set_color("#293B55")

        legend = self.ax.legend()
        legend.get_frame().set_facecolor("#151F32")
        legend.get_frame().set_edgecolor("#293B55")

        for text in legend.get_texts():
            text.set_color("#EAF2FF")

        self.figure.tight_layout()
        self.draw()