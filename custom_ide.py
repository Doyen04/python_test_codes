import sys
from PyQt5.QtCore import QDir, Qt, QEvent,QSize,QRect,QRegExp
from PyQt5.QtGui import QPainter,QPen,QBrush,QTextBlock,QFont,QFontMetrics,QSyntaxHighlighter,QTextCharFormat,QColor ,QTextFormat
from PyQt5.QtWidgets import (QToolBar,QScrollArea,QScroller,QVBoxLayout,QSwipeGesture,QWidget,QStatusBar ,QMainWindow, QPlainTextEdit,QTextEdit,QTabWidget,QScrollerProperties,QApplication)


class area(QPlainTextEdit):
	def __init__(self,scroll,line):
		super().__init__()
		self.LineNumber = line(self)
		self.viewport().setCursor(Qt.BitmapCursor)
		self.setCursor(Qt.BitmapCursor)
		
		#tab is figure i width multiply by no of tim
		#space is font divided byfour
		self.fontV = 18
		self.font = QFont("Sans-serif", self.fontV)
		self.setStyleSheet("background-color:black;color:white;")
		self.setFont(self.font)
		self.spc = self.fontMetrics().width(' ')
		self.tab = self.spc*4
		self.setTabStopWidth(self.tab)
		scroll.init(self)
		try :
			global f 
			f = open("mytext.txt" ,'r') 
		except FileNotFoundError:
			self.appendPlainText('fail')
			pass 
		else :
			self.setPlainText(f.read())
			f.close()
		
	def paintEvent(self,event):
		painter = QPainter(self.viewport())
		pen = QPen(Qt.SolidLine)
		pen.setColor(Qt.white)
		pen.setWidth(1)
		painter.setPen(pen)
		#painter.setBrush(QBrush(Qt.gray,Qt.SolidPattern))
		self.cur  = self.textCursor().block()
		rect = self.blockBoundingGeometry(self.cur).translated(self.contentOffset()).toRect()
		painter.drawRect(4,rect.y(),rect.right()-4,rect.height())
		for x  , y1 , y2 in self.lineCal():
			if y1 != y2:
				painter.drawLine(int(x+6), int(y1), int(x+6), int(y2))
		super().paintEvent(event)
		#with open("mytext.txt" ,"w") as f:
			#f.write(self.document().toPlainText())
		
	def keyPressEvent(self,event):
		
		super().keyPressEvent(event)
		
	def locate(self,x,array):
		find  = None 
		for num , value in enumerate(array):
			if value == x :
				find = num
		return find 

	def lineNumberAreaWidth(self):
		count = max(1, self.blockCount())
		space = 3+self.fontMetrics().width('9') * len(str(count))
		return space
        
	def updateLineNumberAreaWidth(self, _):
		self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

	def resizeEvent(self, event):
		super().resizeEvent(event)
		cr = self.contentsRect();
		self.LineNumber.setGeometry(QRect(cr.left(), cr.top(),self.lineNumberAreaWidth(), cr.height()))  

		
	def lineCal(self):
		boxes = self.blockCount()
		self.space = self.fontMetrics().width(' ')
		#self.setPlainText(str( self.space))
		self.tab_space = self.tab  / self.space
		indentarray = []
		toupdate = []
		coords = []
		for box in range(boxes):
			indent = 0
			block = self.document().findBlockByNumber(box)
			text = block.text()
			text_array =[txt for txt in text ]
			for num, char in enumerate(text_array):
				if len(text.strip()) > 0:
					if char == '\t':
						indent += (self.tab_space*self.space)
					elif char == ' ':
						indent += self.space
					else :
						break 
			grid = self.blockBoundingGeometry(block).translated(self.contentOffset()).bottomLeft()
			x , y1 = grid.x()+indent, grid.y()
			if len(text.strip()) > 0:
				for key in [chr for chr in toupdate]:
					if key >= indent :
						toupdate.remove(key)
				for num in toupdate:
					index = self.locate(num,indentarray)
					if index != None :
						coords[index][2] = y1
			
				toupdate.append(indent)
				indentarray.append(indent)
				coords.append([x, y1,y1])
		return coords 

class MyHighlighter( QSyntaxHighlighter ):
	def __init__( self, parent):
		super().__init__(parent)
		self.keyword= "break|else|for|if|in|next|repeat|return|import|try|while|def|class|self|pass|from|except"
		self.syntax = []
		self.keys = self.keyword.split('|')
		for key in self.keys :
			regex = QRegExp('\\b'+key+'\\b')
			rule = self.update_syntax(regex,Qt.darkMagenta)
			self.syntax.append(rule)
			
		regex = QRegExp("\#[^\n]+")#Qt.darkCyan
		rule = self.update_syntax(regex,QColor('brown'))
		self.syntax.append(rule)
		
		self.string = [ "\'.+\'" , '\".+\"' ]
		self.syntax += [self.update_syntax(QRegExp(rgx),Qt.green) for rgx in self.string ]
		
		regex = QRegExp("\'''[\w\s]+\'''")
		rule = self.update_syntax(regex,Qt.darkCyan)
		self.syntax.append(rule)
	def update_syntax(self,regex,color):
		format = QTextCharFormat()
		brush = QBrush( color, Qt.SolidPattern )
		format.setForeground( brush )
		return (regex, format)
	def highlightBlock( self, text ):
		for regex,format in self.syntax:
			expression = regex
			index = expression.indexIn(text,0)
			while index >= 0:
				length = expression.matchedLength()
				self.setFormat( index, length, format )
				index = expression.indexIn(text,index + length )

#      self.setCurrentBlockState( 0)
#             
class LineNumber(QWidget):

	def __init__(self, editor):
		super().__init__(editor)
		self.editor = editor
	def sizeHint(self):
		return Qsize(self.editor.lineNumberAreaWidth(), 0)
		
	def lineNumberPaintEvent(self, event):
		mypainter = QPainter(self)
		mypainter.fillRect(event.rect(), Qt.black)
		block = self.editor.firstVisibleBlock()
		blockNumber = block.blockNumber()
		top = self.editor.blockBoundingGeometry(block).translated(self.editor.contentOffset()).top()
		bottom = top + self.editor.blockBoundingRect(block).height()
		height = self.editor.fontMetrics().height()
		while block.isValid() and (top <= event.rect().bottom()):
			if block.isVisible() and (bottom >= event.rect().top()):
				number = str(blockNumber + 1)
				mypainter.setPen(Qt.gray)
				#mypainter.drawText(0, top, self.width(), height,Qt.AlignCenter, number)
			block = block.next()
			top = bottom
			bottom = top + self.editor.blockBoundingRect(block).height()
			blockNumber += 1

	def paintEvent(self, event):
		self.lineNumberPaintEvent(event)
		self.editor.updateLineNumberAreaWidth(0)
		self.scroll(0,2)

			
		
class scroll(QScroller):
	def init(editor):
		mouse = scroll.scroller(editor.viewport())
		mouse.grabGesture(
		editor.viewport(), QScroller.LeftMouseButtonGesture )
		props =  mouse.scrollerProperties()
		props.setScrollMetric(QScrollerProperties.VerticalOvershootPolicy,QScrollerProperties.OvershootAlwaysOff)
		props.setScrollMetric(QScrollerProperties.FrameRate, QScrollerProperties.Fps60)
		mouse.setScrollerProperties(props)
	def event(self,e):
		if e.ScrollState() == QScrollEvent.ScrollStarted:
			self.setScrollerProperties()
    	#super().event(e)

class window(QMainWindow):
	def __init__(self,area,scroll,line):
		super().__init__()
		#self.tab = QTabWidget()
		#for _ in range(90):
		#	self.tab.addTab(self.area(_),f'text edit{_}')
		#editor = area()
		self.editor = area(scroll,line)
		self.highlight = MyHighlighter(self.editor.document())
		self.setCentralWidget(self.editor)
		self._createMenu()
		self._createToolBar()
		self._createStatusBar()
	def _createMenu(self):
		self.menu = self.menuBar().addMenu("menu")
		self.menu.addAction('&rExit', self.close)

	def _createToolBar(self):
		tools = QToolBar()
		tools.setStyleSheet('height:20px; background:grey;')
		self.addToolBar(tools)
		tools.addAction('rExit', self.close)

	def _createStatusBar(self):
		status = QStatusBar()
		status.showMessage("I'm the Status Bar")
		self.setStatusBar(status)
		
    	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = window(area,scroll,LineNumber)
	win.show()
	sys.exit(app.exec())