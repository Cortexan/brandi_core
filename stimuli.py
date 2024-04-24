# env imports
import numpy as np
from numpy import cos, pi, sin
from psychopy import visual

# local imports
from startup import win


def Shape(shape, scale):
	# calculate verticies for gate
	arc_angles = np.linspace(pi / 2, 3 * pi / 2, 180)
	# generate verticies for arc + bottom corners, centre to origin
	gate_verts = tuple(
		(round(-sin(angle), 3), round(0.618 - cos(angle), 3)) for angle in arc_angles
	) + ((1.0, -1.0), (-1.0, -1.0))
	gate_verts = tuple((x, y - 0.214) for x, y in gate_verts)

	# shapes dictionary
	shapes = {
		"square": {
			"vertices": ((-1, -1), (-1, 1), (1, 1), (1, -1)),
			"size": scale * 0.5,
			"ori": 0,
		},
		"diamond": {
			"vertices": ((-1, -1), (-1, 1), (1, 1), (1, -1)),
			"size": scale * 0.5,
			"ori": 45,
		},
		"triangle": {
			"vertices": ((0, 1.7546), (-1.5195, -0.8773), (1.5195, -0.8773)),
			"size": scale * 0.5,
			"ori": 0,
		},
		"circle": {"vertices": 360, "size": scale * 1.1284, "ori": 0},
		"cross": {
			"vertices": (
				(-1.341, 0.447),
				(-1.341, -0.447),
				(-0.447, -0.447),
				(-0.447, -1.341),
				(0.447, -1.341),
				(0.447, -0.447),
				(1.341, -0.447),
				(1.341, 0.447),
				(0.447, 0.447),
				(0.447, 1.341),
				(-0.447, 1.341),
				(-0.447, 0.447),
			),
			"size": scale * 0.5,
			"ori": 0,
		},
		"hexagon": {
			"vertices": (
				(1.2408, 0.0),
				(0.6204, 1.0746),
				(-0.6204, 1.0746),
				(-1.2408, 0.0),
				(-0.6204, -1.0746),
				(0.6204, -1.0746),
			),
			"size": scale * 0.5,
			"ori": 0,
		},
		"rectangle": {
			"vertices": (
				(-1.272, -0.7862),
				(1.272, -0.7862),
				(1.272, 0.7862),
				(-1.272, 0.7862),
			),
			"size": scale * 0.5,
			"ori": 0,
		},
		"oval": {"vertices": 360, "size": (scale * 0.8871, scale * 1.4353), "ori": 0},
		"gate": {"vertices": gate_verts, "size": (scale * 0.5) * 0.9122, "ori": 0},
	}

	return visual.ShapeStim(
		win=win,
		vertices=shapes[shape]["vertices"],
		size=shapes[shape]["size"],
		ori=shapes[shape]["ori"],
		units="deg",
		colorSpace="hex",
		fillColor="white",
		lineColor="black",
		lineWidth=1,
		opacity=1,
		interpolate=True,
	)


class Fix:
	def __init__(self, shape="x", scale=0.1, color="white", **kwargs):
		global win
		self.win = win
		self.shape = shape
		self.scale = scale
		self.col = color
		self.stim = None
		self.stim_kwargs = kwargs
		self.create()
		self.apply_stim_settings()

	def create(self):
		shapes = {"crosses": ["x", "+"], "dots": ["o", "dot"]}
		try:
			self.stim = visual.ShapeStim(
				win=win,
				pos=(0, 0),
				vertices=(
					(
						(-1.341, 0.447),
						(-1.341, -0.447),
						(-0.447, -0.447),
						(-0.447, -1.341),
						(0.447, -1.341),
						(0.447, -0.447),
						(1.341, -0.447),
						(1.341, 0.447),
						(0.447, 0.447),
						(0.447, 1.341),
						(-0.447, 1.341),
						(-0.447, 0.447),
					)
					if self.shape in shapes["crosses"]
					else 360
				),
				size=self.scale if self.shape in shapes["crosses"] else self.scale * 2,
				ori=0 if self.shape != "x" else 45,
				units="deg",
				colorSpace="hex",
				fillColor=None if self.shape == "o" else self.col,
				lineColor=self.col,
				lineWidth=0 if self.shape != "o" else 2,
				interpolate=True,
			)
		except KeyError:
			raise ValueError(f"Invalid shape '{self.shape}'")

	def color(self, color):
		if self.shape == "o":
			self.stim.lineColor = color
		else:
			self.stim.color = color

	def __getattr__(self, attr):
		try:
			return getattr(self.stim, attr)
		except AttributeError:
			raise AttributeError(f"'Fix' object has no attribute '{attr}'")

	def apply_stim_settings(self):
		# Apply additional settings passed through kwargs
		for key, value in self.stim_kwargs.items():
			try:
				setattr(self.stim, key, value)
			except AttributeError:
				raise AttributeError(f"'Fix' object has no attribute '{key}'")
