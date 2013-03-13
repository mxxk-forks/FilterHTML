import re
SPEC = {
   "div": {
      "class": [
         "btn",
         "container"
      ]
   },
   "a": {
      "href": "url",
      "target": [
         "_blank"
      ]
   },
   "img": {
      "src": "url",
      "border": "int",
      "width": "int",
      "height": "int"
   },
   "input": {
      "type": "alpha",
      "name": "[abcdefghijklmnopqrstuvwxyz-]",
      "value": "alphanumeric"
   },
   "hr": {},
   "br": {},
   "strong": {},
   "i": {
      "class": re.compile('^icon-[a-z0-9_]+$')
   },
   "span": {
      "style": ["color: red;"]
   },
   "p": {
      "class": [
         "centered"
      ],
      # special style parsing
      "style": {
         "color": re.compile(r'^#[0-9A-Fa-f]{6}$')
      }
   },
   
   # allow attributes on all (previously) allowed tags
   '*': {
      'style': re.compile(r'^text-align:\s*(left|right|center|justify);?$')
   },

   # alias
   "b": "strong",
   "center": "p class=\"centered\""

}
