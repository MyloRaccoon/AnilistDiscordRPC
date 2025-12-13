class Activity:

	def __init__(self, status: str, title: str, progress: str):
		self.status: str = status
		self.title: str = title
		self.progress: str = progress

	def __str__(self) -> str:
		return f"{self.status} {self.progress} of {self.title}"