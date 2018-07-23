# This python file uses the following encoding: utf-8

def process_document():
	# MODAL USE OF THE SANDBOX
	print """<?xml version='1.0' encoding='utf-8'?>
<!--
	(c)2016-2018, SARL MEZZONOMY
-->
<?stop always?>
<?xml-stylesheet  type='text/xsl' href='djs/agreement.xsl'?>
<bhb:host 
  xmlns:bhb="bhb://the.hypertext.blockchain"
  xmlns:on = "bhb://sourced.events"
  bhb:link="temps" socket="canal">
  <sandbox:map xmlns:sandbox="bhb://the.sandbox" bhb:path="/djs-v1-admin" bhb:stylesheet="sandbox/static.xsl">
  </sandbox:map>
  <bhb:default bhb:path="/djs-v1-default" bhb:stylesheet="hyper/defaultss.xsl">
  </bhb:default>
</bhb:host>
<?bhb-document on:id='debruyin' on:clock='2018-07-21T09:52:05Z' on:source='admin'  bhb:sign='auto'?>
"""

def process_number(number):
	# DEBRUYIN CORE
	print """<bhb:link append="debruyin/bhb:soup">
	<bhb:host number="%(number)s" right="%(right_tail)s.%(right_head)s" left="%(left_head)s.%(left_tail)s">
		<socket bhb:symbol="0.%(right_tail)s.%(right_head)s"/> 
		<socket bhb:symbol="%(left_head)s.%(left_tail)s.0"/>  
		<socket bhb:symbol="%(left_head)s.%(left_tail)s.1"/>  
		<socket bhb:symbol="1.%(right_tail)s.%(right_head)s"/>  
	</bhb:host> 
</bhb:link>"""% {'right_tail': number[:-1], 'right_head': number[-1],
	  'left_head' : number[ 0], 'left_tail' : number[ 1:],
	  'number' : number
	} 
	print """<?bhb-block on:id="%(number)s" on:source='bhb://admin@{block 0}' on:clock='2018-07-21T10:20:05Z' bhb:sign='auto'?>
"""% {'right_tail': number[:-1], 'right_head': number[-1],
	  'left_head' : number[ 0], 'left_tail' : number[ 1:],
	  'number' : number
	} 

# ENUMERATION ENGINE

def next_number(number):
	def next_digit(digit):
		assert digit in symbols
		next = symbols.find(digit) + 1
		if next < len(symbols):
			return False, symbols[next]
		return True, symbols[0]
	if number == "":
		print "<!-- Finish -->"; return ""
	tail, head   = number[:-1], number[-1]
	carry, digit = next_digit(head)
	if carry:
		return next_number(tail) + digit
	return tail + digit

symbols   = "01"
assert 2 <= len(symbols) 

length    = 3
start     = symbols[0] * length

# MAIN

process_document()
current = next_number(start)
while not current == start:
	process_number(current)
	current = next_number(current)
process_number(current)

	

