
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x8a\x94\xba\xb3Mc\xf5\xcec\xdc\xfd\x08\x15\x96\xb9\x07'
    
_lr_action_items = {'BAR':([1,2,4,5,7,8,9,],[-1,6,-4,-2,6,-3,-5,]),'LPAREN':([0,1,2,3,4,5,6,7,8,9,],[3,-1,3,3,-4,-2,3,3,-3,-5,]),'RPAREN':([1,4,5,7,8,9,],[-1,-4,-2,9,-3,-5,]),'LETTER':([0,1,2,3,4,5,6,7,8,9,],[1,-1,1,1,-4,-2,1,1,-3,-5,]),'STAR':([1,2,4,5,7,8,9,],[-1,4,-4,4,4,4,-5,]),'$end':([1,2,4,5,8,9,],[-1,0,-4,-2,-3,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'re':([0,2,3,5,6,7,8,],[2,5,7,5,8,5,5,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> re","S'",1,None,None,None),
  ('re -> LETTER','re',1,'p_re_letter','/Users/victor/Dropbox/cs262-Udacity-Programming-Languages/cs262-final-exam-9-implementing-re.py',80),
  ('re -> re re','re',2,'p_re_concat','/Users/victor/Dropbox/cs262-Udacity-Programming-Languages/cs262-final-exam-9-implementing-re.py',84),
  ('re -> re BAR re','re',3,'p_re_bar','/Users/victor/Dropbox/cs262-Udacity-Programming-Languages/cs262-final-exam-9-implementing-re.py',88),
  ('re -> re STAR','re',2,'p_re_star','/Users/victor/Dropbox/cs262-Udacity-Programming-Languages/cs262-final-exam-9-implementing-re.py',92),
  ('re -> LPAREN re RPAREN','re',3,'p_re_paren','/Users/victor/Dropbox/cs262-Udacity-Programming-Languages/cs262-final-exam-9-implementing-re.py',96),
]