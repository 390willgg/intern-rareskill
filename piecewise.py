from manim import *

class PiecewiseFunction2(Scene):
    def construct(self):
        # Define the piecewise function
        piecewise_function = MathTex(
            r"R_{borrow} = \begin{cases} R_{intercept} + \frac{U}{U_{optimal}}R_{slope1} & \text{if } U \leq U_{optimal} \\ R_{intercept} + R_{slope1} + \frac{U-U_{optimal}}{1-U_{optimal}}R_{slope2}, & \text{if } U > U_{optimal} \end{cases}", font_size=38
        )
        # piecewise_function[0][49:109].set_color(BLACK)
        self.play(Write(piecewise_function), duration=2)
        self.play(piecewise_function.animate.shift(UP*2.5).scale(1), duration=2)
        
        plane = Axes(
            x_range = (0, 7),
            y_range = (0, 5),
            x_length = 10,
            y_length=5,
            tips=False,
            axis_config={
                "font_size": 10,
            },
        ).scale(0.7)
        plane.next_to(piecewise_function, DOWN*3)
        label_x = plane.get_x_axis_label(MathTex(r'Utilization', font_size=38).scale(0.65), edge=DOWN, direction=DOWN, buff=0.5)

        labels = plane.get_axis_labels(
            Tex("").scale(0.3).set_opacity(0), MathTex(r"Interest Rate", font_size=38).scale(0.65).next_to(plane, UP+RIGHT)
        )
        
         # Plotting the first part of the piecewise function on the graph
        plot = plane.plot_line_graph(x_values=[0,5], y_values=[1, 3], line_color=WHITE)
        # Plotting the second part of the piecewise function on the graph
        plot_2 = plane.plot_line_graph(x_values=[5,7], y_values=[3, 5], line_color=WHITE)
        
        # Creating the y-axis label and positioning it
        y_label = MathTex(r"R_{intercept}", font_size=30)
        y_label.next_to(plane.coords_to_point(0, 1), LEFT*3, buff = 0.2)
        
        # Creating the U_optimal label and positioning it
        u_optimal = MathTex(r"U_{optimal}", font_size=30)
        u_optimal.next_to(plane.coords_to_point(5,0), DOWN, buff=0.2)
        
        # Creating the 100% label and positioning it at the end of the x-axis
        oneHundred_persent = MathTex('100\\%', font_size=20)
        oneHundred_persent.next_to(plane.coords_to_point(7, 0), DOWN, buff=0.2)
        
        # Creating the 0% label and positioning it at the start of the x-axis
        zero_persent = MathTex('0\\%', font_size=20)
        zero_persent.next_to(plane.coords_to_point(0, 0), DOWN, buff=0.2)
        
        # Displaying the whole setup on the screen
        self.play(Create(plane), Create(label_x),Create(labels), Create(zero_persent),Create(oneHundred_persent), duration=2)
        self.wait(1)

        # Dimming the entire setup
        self.play(
            labels.animate.set_opacity(0.5),
            piecewise_function.animate.set_opacity(0.5),
            plane.animate.set_opacity(0.5),
            label_x.animate.set_opacity(0.5),
            zero_persent.animate.set_opacity(0.5),
            oneHundred_persent.animate.set_opacity(0.5),
            run_time=1
        )

        # Highlighting R_intercept and U_optimal
        self.play(Create(y_label), Create(u_optimal),piecewise_function[0][9:19].animate.set_opacity(1),piecewise_function[0][39:49].animate.set_opacity(1), duration=2)
        self.play(ScaleInPlace(piecewise_function[0][9:19], scale_factor=1.15),ScaleInPlace(y_label, scale_factor=1.2), rate_func=there_and_back, run_time=2)
        self.play(ScaleInPlace(piecewise_function[0][39:49], scale_factor=1.15),ScaleInPlace(u_optimal, scale_factor=1.2), rate_func=there_and_back, run_time=2)
        self.wait(1)

        # Restoring the opacity of the entire setup
        self.play(
            labels.animate.set_opacity(1),
            piecewise_function.animate.set_opacity(1),
            plane.animate.set_opacity(1),
            label_x.animate.set_opacity(1),
            zero_persent.animate.set_opacity(1),
            oneHundred_persent.animate.set_opacity(1),
            run_time=1
        )
        
        # Creating the first plot
        R_interestTracker = ValueTracker(0)

        def calculate_y(x):
            return 0.4 * x + 1

        uOptimal_label = always_redraw(
            lambda: MathTex(r"U", font_size=24).next_to(plane.c2p(R_interestTracker.get_value(), calculate_y(R_interestTracker.get_value())), UP*1.5)
        )
        

        # # Create a line that will act as the 'revealer'
        revealer_line = always_redraw(
            lambda: Line(
                start=plane.c2p(R_interestTracker.get_value(), 0),
                end=plane.c2p(R_interestTracker.get_value(), calculate_y(R_interestTracker.get_value())),
                stroke_width=3,
                color=GREEN
            )
        )
        self.add(uOptimal_label, revealer_line)
        # Animate the ValueTracker changing from 0 to 100
        
        self.play(Create(plot), R_interestTracker.animate.set_value(5), run_time=4,rate_func=smooth, duration=2)
        
        # Highlighting the components of the first equation
        self.play(plot.animate.set_color(GREEN), piecewise_function[0][20:37].animate.set_color(GREEN), piecewise_function[0][39:49].animate.set_color(GREEN),y_label.animate.set_color(GREEN),piecewise_function[0][9:19].animate.set_color(GREEN),piecewise_function[0][49:109].animate.set_opacity(0.5),u_optimal.animate.set_color(GREEN),zero_persent.animate.set_color(GREEN), duration = 2)
        self.wait(3)
        
        # Reversing the highlight of the first equation components
        self.play(plot.animate.set_color(WHITE), piecewise_function[0][20:37].animate.set_color(WHITE), piecewise_function[0][39:49].animate.set_color(WHITE),y_label.animate.set_color(WHITE),piecewise_function[0][9:19].animate.set_color(WHITE),piecewise_function[0][49:109].animate.set_opacity(1)  ,u_optimal.animate.set_color(WHITE),zero_persent.animate.set_color(WHITE), duration = 2)
        self.wait(1)        

        # Creating a vertical line to represent the slope
        line_branch = Line(
            start = plane.coords_to_point(0, 1),
            end = plane.coords_to_point(0, 3),
            stroke_width = 2,
            color = WHITE,
        )
        
        # Highlighting the slope1 part of the function
        self.play(piecewise_function[0][60:67].animate.set_color(YELLOW),piecewise_function[0][9:49].animate.set_opacity(0.5),duration=2 )
        
        # Creating a brace to represent the slope1 on the graph and labeling it
        b2 = Brace(line_branch, direction=line_branch.copy().rotate(PI / 2).get_unit_vector(), stroke_width=-100, color=YELLOW, buff=0.2)
        b2_label = MathTex(r'R_{slope1}', font_size=30).next_to(b2, LEFT*0.5).set_color(YELLOW)
        self.play(Create(b2), Create(b2_label), duration=2)
        self.wait(0.5)
        
        # Dimming the first plot and creating the second plot
        R_interestTracker2 = ValueTracker(5)

        def calculate_y2(x):
            return x - 2

        uOptimal_label2 = always_redraw(
            lambda: MathTex(r"U", font_size=24).next_to(plane.c2p(R_interestTracker2.get_value(), calculate_y2(R_interestTracker2.get_value())), UP*1.5)
        )

        # # Create a line that will act as the 'revealer'
        revealer_line2 = always_redraw(
            lambda: Line(
                start=plane.c2p(R_interestTracker2.get_value(), 0),
                end=plane.c2p(R_interestTracker2.get_value(), calculate_y2(R_interestTracker2.get_value())),
                stroke_width=3,
                color=RED
            )
        )
        self.play(FadeOut(uOptimal_label, revealer_line, R_interestTracker))
        self.add(uOptimal_label2, revealer_line2)
        self.play(plot.animate.set_opacity(0.5),Create(plot_2), R_interestTracker2.animate.set_value(7), run_time=4,rate_func=smooth, duration=1.5)

        # Highlighting the second part of the piecewise function
        self.play(piecewise_function[0][68:96].animate.set_color(RED), piecewise_function[0][99:109].animate.set_color(RED), u_optimal.animate.set_color(RED),oneHundred_persent.animate.set_color(RED),plot_2.animate.set_color(RED), duration=2)
        # Changing the color of the second plot to red to match the highlighted function
        self.wait(4) # Waiting for 4 seconds before the end of the scene