from makcu import create_controller, MouseButton
ctl = None
btn = {"left": MouseButton.LEFT, "right": MouseButton.RIGHT, "middle": MouseButton.MIDDLE, "back": MouseButton.MOUSE4, "forward": MouseButton.MOUSE5}
def connect(dbg=False): global ctl; ctl = create_controller(debug=dbg)
def disconnect(): global ctl; ctl = None
def _chk(): assert ctl, "call connect() first"
def _btn(b): return btn[b.lower()]
def move(x, y): _chk(); ctl.move(x, y)
def hold(b="left"): _chk(); ctl.press(_btn(b))
def release(b="left"): _chk(); ctl.release(_btn(b))
def click(b="left"): _chk(); ctl.press(_btn(b)); ctl.release(_btn(b))
def scroll(amt): _chk(); ctl.scroll(amt)
