import time
from color import Color
from console import Console

class Transition:
    steps = 0
    pulse = 0
    
    def conf(self, steps, pulse):
        self.steps = steps
        self.pulse = pulse
    
    def run(self, start_color, end_color, set_color):
        step = 0
                
        console = Console()
        console.log(' ---  START  ---')
        console.log('TARGET ' + str(float(end_color.get_red())) + ', ' + str(end_color.get_green()) + ', ' + str(end_color.get_blue()))
        
        while (step < self.steps):
            next_color = self.step(step, start_color, end_color)
            set_color(next_color)
            
            step += 1
            time.sleep(self.pulse)
            
    
    def step(self, step, start_color, end_color):
        red = self.single_step(step, start_color.get_red(), end_color.get_red())
        green = self.single_step(step, start_color.get_green(), end_color.get_green())
        blue = self.single_step(step, start_color.get_blue(), end_color.get_blue())
        
        console = Console()
        console.log('STEP ' + str(red) + ', ' + str(green) + ', ' + str(blue))
        
        return Color(int(red), int(green), int(blue))
    
    def single_step(self, step, start, end):
        if (float(start) > float(end)):
            diff = float(start) - float(end)
            
            step_diff = diff / self.steps
            
            return float(start) - (float(step_diff) * float(step + 1))
        elif (float(start) == float(end)):
            return float(start)
        else:
            diff = float(end) - float(start)
            
            step_diff = diff / self.steps
            
            return float(start) + (float(step_diff) * float(step))