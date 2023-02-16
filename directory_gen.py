import argparse
import pathlib 
import sys , os

path = "/sdcard/download"
#path = "/data/data/ru.iiec.pydroid3/files/"
#just = pathlib.Path(path).iterdir()
#path = sorted(just , key = lambda path : path.is_file())

class Generator:
	PIPE = "│"
	ELBOW = "└── "
	TEE = "├── "
	PIPE_PREFIX = "│   "
	SPACE_PREFIX = "    "
	
	def __init__(self, path):
		self.path = pathlib.Path(path)
		self.tree = []
		
	def output(self):
		for x in self.make_tree():
			print(x)
			
	def make_tree(self):
		self.tree.append(f"{self.path}{os.sep}")
		self.tree.append(f" {self.PIPE}")
		self.generate(self.path)
		return self.tree
		
	def generate(self,path,prefix=" "):
		links = path.iterdir()
		links = sorted(links , key = lambda link : link.is_file())
		lent = len(links)
		for num, link in enumerate(links):
			conn = self.TEE if num != lent -1 else self.ELBOW
			if link.is_dir():
				self.isdir(num,link,conn,prefix,lent)
			if link.is_file():
				self.isfile(link,conn,prefix)
		
	def isfile(self,link,conn,prefix):
		self.tree.append(f"{prefix}{conn}{link.name}")
		
	def isdir(self,num,link,conn,prefix,lent):
		self.tree.append(f"{prefix}{conn}{link.name}{os.sep}")
		if num != lent-1:
			prefix += self.PIPE_PREFIX
		else :
			prefix += self.SPACE_PREFIX
		#print(path)
		self.generate(path=link,prefix=prefix)
		
gen = Generator(path)
gen.output()

