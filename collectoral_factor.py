from manim import *

class CollateralLoanScene(Scene):
    def construct(self):
        # Create text labels
        collateral_label = Text("Collateral", color=WHITE).next_to(UP*2+LEFT*7)
        loan_label = Text("Loan", color=WHITE).next_to(collateral_label, DOWN, buff=1.5)
        loan_label.align_to(collateral_label, LEFT)

        # Create the bars
        new_width100 = 8
        new_width70 = 8*0.7
        new_width90 = 8 * 0.9
        
        collateral_bar = RoundedRectangle(width=new_width100, height=1, color=WHITE, corner_radius=0.2).scale(np.array([1e-4, 1, 1])).next_to(collateral_label, RIGHT)
        loan_bar = RoundedRectangle(width=new_width100, height=1, color=WHITE, corner_radius=0.2).scale(np.array([1e-4, 1, 1])).next_to(loan_label, RIGHT)
        loan_bar.align_to(collateral_bar, LEFT)
        
        # Create the percentage text
        factor = Text("0")
        percentage_label = Text("Collateral_Factor =", color=WHITE)
        tempFactor = VGroup(percentage_label, factor).arrange(direction=RIGHT, buff=0.3).next_to(LEFT*8 + DOWN*3.1).scale(0.75)
        
        # Create the brand text
        brand_label = ImageMobject("mediaimages/collectoral_factor/rareskillLogo.png").next_to(RIGHT*3+DOWN*3.1)

        # Group everything together
        self.add(collateral_label, loan_label, collateral_bar, loan_bar, tempFactor, brand_label)
            
        def animate_bar_and_percentage(self, bar, new_width, start_percentage, end_percentage, colorData):
            def update_percentage(mob, alpha):
                percentage = int(start_percentage + (end_percentage - start_percentage) * alpha)
                mob.become(Text(f"{percentage}%", color=colorData).scale(0.75).next_to(percentage_label, RIGHT))
            shift_amount = (bar.width - new_width) / 2 
            tempFactor.set_color(color=colorData)
            self.play(UpdateFromAlphaFunc(tempFactor[1], update_percentage), bar.animate.stretch_to_fit_width(new_width).shift(LEFT * shift_amount), run_time=2, rate_func=linear)
        
        # Animate to 100%
        shift_amountCollactoral = (collateral_bar.width - new_width100) / 2
        def update_percentage(mob, alpha):
                percentage = int( + (100 - 0) * alpha)
                mob.become(Text(f"{percentage}%", color=WHITE).scale(0.75).next_to(percentage_label, RIGHT))
        shift_amount = (loan_bar.width - new_width100) / 2 
        tempFactor.set_color(color=WHITE)
        self.play(UpdateFromAlphaFunc(tempFactor[1], update_percentage), loan_bar.animate.stretch_to_fit_width(new_width100).shift(LEFT * shift_amount), collateral_bar.animate.stretch_to_fit_width(new_width100).shift(LEFT * shift_amountCollactoral), run_time=2, rate_func=linear)

        brace_100 = Brace(
            loan_bar,   # Call the method to get the ending point
            direction=DOWN,
            color=GREEN
        ).shift(DOWN * 0.2)  # Adjust the 0.2 value as needed
        brace_text100 = brace_100.get_text(r"value")
        
        self.play(GrowFromCenter(brace_100), Write(brace_text100))
        self.play(FadeOut(brace_100, brace_text100))
        
        # Animate to 70%
        animate_bar_and_percentage(self, loan_bar, new_width70, 100, 70, YELLOW)
        brace_70 = BraceBetweenPoints(
            loan_bar.get_right(), 
            loan_bar.get_right() + RIGHT * (new_width100 - new_width70), 
            direction=DOWN, 
            color=GREEN
        ).shift(DOWN * 0.2)
        
        brace_text70 = brace_70.get_text(r"Higher Margin \\of Safety")
        self.play(GrowFromCenter(brace_70), Write(brace_text70))
        self.play(FadeOut(brace_70, brace_text70))
        
        # Animate to 90%
        animate_bar_and_percentage(self, loan_bar, new_width90, 70, 90, RED)
        brace_90 = BraceBetweenPoints(
            loan_bar.get_right(), 
            loan_bar.get_right() + RIGHT * (new_width100 - new_width90), 
            direction=DOWN, 
            color=RED
        ).shift(DOWN * 0.2)
        brace_text90 = brace_90.get_text(r"Lower Margin \\of Safety")
        self.play(GrowFromCenter(brace_90), Write(brace_text90))
        self.play(FadeOut(brace_90, brace_text90))
        
class CollateralLoanScene01(Scene):
    def construct(self):
        # Create text labels
        collateral_label = Text("Collateral", color=WHITE).next_to(UP*2+LEFT*7)
        loan_label = Text("Loan", color=WHITE).next_to(collateral_label, DOWN, buff=1.5)
        loan_label.align_to(collateral_label, LEFT)

        # Create the bars
        new_width100 = 8
        new_width70 = 8*0.7
        new_width90 = 8 * 0.9
        
        collateral_bar = RoundedRectangle(width=new_width100, height=1, color=WHITE, corner_radius=0.2).next_to(collateral_label, RIGHT)
        loan_bar = RoundedRectangle(width=new_width70, height=1, color=WHITE, corner_radius=0.2).next_to(loan_label, RIGHT)
        loan_bar.align_to(collateral_bar, LEFT)
        
        # Create the percentage text
        factor = Text("70%")
        percentage_label = Text("Collateral_Factor =", color=WHITE)
        tempFactor = VGroup(percentage_label, factor).arrange(direction=RIGHT, buff=0.3).next_to(LEFT*8 + DOWN*3.1).scale(0.75)
        
        # Create the brand text
        brand_label = ImageMobject("media\images/collectoral_factor/rareskillLogo.png").next_to(RIGHT*3+DOWN*3.1)

        # Group everything together
        self.add(collateral_label, loan_label, collateral_bar, loan_bar, tempFactor, brand_label)
            
        def animate_bar_and_percentage(self, bar, new_width, start_percentage, end_percentage, color):
            def update_percentage(mob, alpha):
                percentage = int(start_percentage + (end_percentage - start_percentage) * alpha)
                mob.become(Text(f"{percentage}%", color=color).scale(0.75).next_to(percentage_label, RIGHT))
            shift_amount = (bar.width - new_width) / 2 
            tempFactor.set_color(color=color)
            self.play(UpdateFromAlphaFunc(tempFactor[1], update_percentage), bar.animate.stretch_to_fit_width(new_width).shift(LEFT * shift_amount), run_time=2, rate_func=linear)
        
        brace_70 = BraceBetweenPoints(
            loan_bar.get_right(), 
            loan_bar.get_right() + RIGHT * (new_width100 - new_width70), 
            direction=DOWN, 
            color=GREEN
        ).shift(DOWN * 0.2)
        brace_text70 = brace_70.get_text(r"Higher Margin \\of Safety")
        
        brace_100 = Brace(
            loan_bar,   # Call the method to get the ending point
            direction=DOWN,
            color=GREEN
        ).shift(DOWN * 0.2)  # Adjust the 0.2 value as needed
        brace_text100 = brace_100.get_text(r"value")
        
        self.play(GrowFromCenter(brace_100), Write(brace_text100))
        self.play(FadeOut(brace_100, brace_text100))
        
        self.play(GrowFromCenter(brace_70), Write(brace_text70))
        self.play(FadeOut(brace_70, brace_text70))
        
        # Animate to 90%
        animate_bar_and_percentage(self, loan_bar, new_width90, 70, 90, RED)
        brace_90 = BraceBetweenPoints(
            loan_bar.get_right(), 
            loan_bar.get_right() + RIGHT * (new_width100 - new_width90), 
            direction=DOWN, 
            color=RED
        ).shift(DOWN * 0.2)
        brace_text90 = brace_90.get_text(r"Lower Margin \\of Safety")
        self.play(GrowFromCenter(brace_90), Write(brace_text90))
        self.play(FadeOut(brace_90, brace_text90))

class CollateralLoanScene02(Scene):
    def construct(self):
        # Create text labels
        collateral_label = Text("Collateral", color=WHITE).next_to(UP*3+LEFT*7)
        loan_label = Text("Loan", color=WHITE).next_to(collateral_label, DOWN, buff=1.5)
        loan_label.align_to(collateral_label, LEFT)

        # Create the bars
        new_width100 = 8
        new_width70 = 8*0.5
        new_width90 = 8 * 0.9
        
        collateral_bar = RoundedRectangle(width=new_width100, height=1, color=WHITE, corner_radius=0.2).next_to(collateral_label, RIGHT)
        loan_bar = RoundedRectangle(width=new_width70, height=1, color=WHITE, corner_radius=0.2).next_to(loan_label, RIGHT)
        loan_bar.align_to(collateral_bar, LEFT)
        
        # Create the percentage text
        factor = Text("50%")
        percentage_label = Text("Collateral_Factor =", color=WHITE)
        tempFactor = VGroup(percentage_label, factor).arrange(direction=RIGHT, buff=0.3).next_to(LEFT*8 + DOWN*3.1).scale(0.75)
        
        # Create the brand text
        brand_label = ImageMobject("media\images/collectoral_factor/rareskillLogo.png").next_to(RIGHT*3+DOWN*3.1)

        # Group everything together
        self.add(collateral_label, loan_label, collateral_bar, loan_bar, tempFactor, brand_label)
            
        def animate_bar_and_percentage(self, bar, new_width, start_percentage, end_percentage, color):
            def update_percentage(mob, alpha):
                percentage = int(start_percentage + (end_percentage - start_percentage) * alpha)
                mob.become(Text(f"{percentage}%", color=color).scale(0.75).next_to(percentage_label, RIGHT))
            shift_amount = (bar.width - new_width) / 2 
            tempFactor.set_color(color=color)
            self.play(UpdateFromAlphaFunc(tempFactor[1], update_percentage), bar.animate.stretch_to_fit_width(new_width).shift(LEFT * shift_amount), run_time=2, rate_func=linear)
        
        # Animate to 70%
        line = Line(RIGHT*9, color=WHITE)
        left_cap = Line(UP*0.1, DOWN*0.1, color=WHITE).move_to(line.get_start())
        right_cap = Line(UP*0.1, DOWN*0.1, color=WHITE).move_to(line.get_end())
        line_with_caps = VGroup(left_cap, line, right_cap)

        # Create the text
        value_text = Text("Value", color=WHITE, font_size=22)
        lineTempDown = VGroup(line_with_caps, value_text).arrange(direction=DOWN, buff=0.2).next_to(loan_bar, DOWN)
        lineTempDown.align_to(loan_bar, LEFT)

        # Add everything to the scene
        self.add(lineTempDown)
        
        brace_70 = BraceBetweenPoints(
            loan_bar.get_right(), 
            loan_bar.get_right() + RIGHT * (new_width100 - new_width70), 
            direction=DOWN, 
            color=GREEN
        ).shift(DOWN * 1.5)
        brace_text70 = brace_70.get_tex(r"Higher Margin \\of Safety").scale(0.70)
        
        self.play(GrowFromCenter(brace_70), Write(brace_text70))
        self.play(FadeOut(brace_70, brace_text70))
        
        # Animate to 90%
        animate_bar_and_percentage(self, loan_bar, new_width90, 50, 90, RED)
        brace_90 = BraceBetweenPoints(
            loan_bar.get_right(), 
            loan_bar.get_right() + RIGHT * (new_width100 - new_width90), 
            direction=DOWN, 
            color=RED
        ).shift(DOWN * 1.5)
        brace_text90 = brace_90.get_tex(r"Lower Margin \\of Safety").scale(0.70)
        self.play(GrowFromCenter(brace_90), Write(brace_text90))
        self.play(FadeOut(brace_90, brace_text90))
        

class CollateralLoanScene03(Scene):
    def construct(self):
        # Create text labels
        collateral_label = Text("Collateral", color=WHITE).next_to(UP*3+LEFT*7)
        loan_label = Text("Loan", color=WHITE).next_to(collateral_label, DOWN, buff=1.5)
        loan_label.align_to(collateral_label, LEFT)

        # Create the bars
        new_width100 = 8
        new_width70 = 8*0.7
        new_width80 = 8 * 0.8
        new_width90 = 8 * 0.9
        
        collateral_bar = RoundedRectangle(width=new_width100, height=1, color=WHITE, corner_radius=0.2).next_to(collateral_label, RIGHT)
        loan_bar = RoundedRectangle(width=new_width70, height=1, color=WHITE, corner_radius=0.2).next_to(loan_label, RIGHT)
        loan_bar.align_to(collateral_bar, LEFT)
        
        # Create the percentage text
        factor = Text("70%")
        percentage_label = Text("LTV =", color=WHITE)
        Liquidation_factor = Text("Liquidation factor = 90%", color=WHITE).next_to(LEFT*8 + DOWN*3.1).scale(0.75)
        tempFactor = VGroup(percentage_label, factor).arrange(direction=RIGHT, buff=0.3).next_to(LEFT*8 + DOWN*2.1).scale(0.75)
        tempFactor.align_to(Liquidation_factor, LEFT)
        
        self.add(Liquidation_factor)
        # Create the brand text
        brand_label = ImageMobject("media\images/collectoral_factor/rareskillLogo.png").next_to(RIGHT*3+DOWN*3.1)

        # Group everything together
        self.add(collateral_label, loan_label, collateral_bar, loan_bar, tempFactor, brand_label)
            
        # Animate to 70%
        line = Line(RIGHT*9, color=WHITE)
        left_cap = Line(UP*0.1, DOWN*0.1, color=WHITE).move_to(line.get_start())
        right_cap = Line(UP*0.1, DOWN*0.1, color=WHITE).move_to(line.get_end())
        line_with_caps = VGroup(left_cap, line, right_cap)
       
        self.add(Text("$0", font_size=16, color=WHITE).next_to(LEFT*3.95 + DOWN*0.5))
        self.add(Text("$1000", font_size=16, color=WHITE).next_to(RIGHT*3.87 + DOWN*0.5))

        # Create the text
        line_with_caps.align_to(loan_bar, LEFT)
        
        def create_percent_group(bar, proportion, percentage):
            percent_pos = bar.get_right()
            percent_line = Line(UP * 0.1, DOWN * 0.1, color=WHITE).next_to(percent_pos, DOWN*4.1)
            percent_label = Text(f"{percentage}", color=WHITE, font_size=18).next_to(percent_line, DOWN)
            return VGroup(percent_line, percent_label)
        
        percentage_value = ValueTracker(700)
        
        percent_group = always_redraw(lambda: create_percent_group(
            loan_bar, 0.9, int(percentage_value.get_value())))

        self.add(line_with_caps, percent_group, percentage_value)
        
        def update_percentage70(mob, alpha):
            percentage = int(70 + (80 - 70) * alpha)
            mob.become(Text(f"{percentage}%", color=WHITE).scale(0.75).next_to(percentage_label, RIGHT))
        
        shift_amount = (loan_bar.width - new_width80) / 2     
        tempFactor.set_color(color=WHITE)
        self.play(UpdateFromAlphaFunc(tempFactor[1], update_percentage70), loan_bar.animate.stretch_to_fit_width(new_width80).shift(LEFT * shift_amount), percentage_value.animate.set_value(800), run_time=2, rate_func=linear)
        
        def update_percentage90(mob, alpha):
            percentage = int(80 + (91 - 80) * alpha)
            if percentage < 90:
                tempFactor.set_color(color=WHITE)
                mob.become(Text(f"{percentage}%", color=WHITE).scale(0.75).next_to(percentage_label, RIGHT))
            elif percentage >= 90:
                tempFactor.set_color(RED)
                # Liquidation_factor.set_color(color=RED)
                Liquidation_factor.set_color(color=RED, family=True)
                mob.become(Text(f"{percentage}%", color=RED).scale(0.75).next_to(percentage_label, RIGHT))
                
        shift_amount90 = (loan_bar.width - new_width90) / 2     
        self.play(UpdateFromAlphaFunc(tempFactor[1], update_percentage90), loan_bar.animate.stretch_to_fit_width(new_width90).shift(LEFT * shift_amount90),  percentage_value.animate.set_value(901), run_time=2, rate_func=linear)
        
class CollateralLoanScene04(Scene):
    def construct(self):
        # Create text labels
        collateral_label = Text("Collateral", color=WHITE).next_to(UP*3+LEFT*7)
        loan_label = Text("Loan", color=WHITE).next_to(collateral_label, DOWN, buff=1.5)
        loan_label.align_to(collateral_label, LEFT)

        # Create the bars
        new_width100 = 10
        new_width80 = 10 * 0.75
        new_width85 = 10 * 0.85
        new_width90 = 10 * 0.9
        new_width95 = 10 * 0.95
        
        collateral_bar = RoundedRectangle(width=new_width100, height=1, color=WHITE, corner_radius=0.2).next_to(collateral_label, RIGHT)
        loan_bar = RoundedRectangle(width=new_width80, height=1, color=WHITE, corner_radius=0.2).next_to(loan_label, RIGHT)
        loan_bar.align_to(collateral_bar, LEFT)
        eth_label = Text("Eth", color=WHITE).scale(0.5).move_to(collateral_bar.get_center())
        usdc_label = Text("USDC", color=WHITE).scale(0.5).move_to(loan_bar.get_center())
        
        # Create the percentage text
        factor = Text("80%")
        percentage_label = Text("LTV =", color=WHITE)
        Liquidation_factor = Text("Liquidation factor = 90%", color=WHITE).next_to(LEFT*8 + DOWN*3.1).scale(0.75)
        tempFactor = VGroup(percentage_label, factor).arrange(direction=RIGHT, buff=0.3).next_to(LEFT*8 + DOWN*2.1).scale(0.75)
        tempFactor.align_to(Liquidation_factor, LEFT)
        
        self.add(Liquidation_factor)
        brand_label = ImageMobject("media/images/collectoral_factor/rareskillLogo.png").next_to(RIGHT*3+DOWN*3.1)

        self.add(collateral_label, loan_label, collateral_bar, loan_bar, tempFactor, brand_label, eth_label, usdc_label)
            
        line = Line(LEFT*3.65, RIGHT*6.3, color=WHITE)
        left_cap = Line(UP*0.1, DOWN*0.1, color=WHITE).next_to(line.get_start(), LEFT, buff=0)
        right_cap = Line(UP*0.1, DOWN*0.1, color=WHITE).next_to(line.get_center() + RIGHT*2.5, RIGHT, buff=0)
        
        line_with_caps = VGroup(line, left_cap, right_cap)
        line_with_caps.align_to(loan_bar, LEFT)
       
        zero_text = Text("$0", font_size=18, color=WHITE).next_to(line.get_start(), DOWN, buff=0.5)
        thousand_text = Text("$800", font_size=18, color=WHITE).next_to(line.get_center() + RIGHT*2.5, DOWN, buff=0.5)
        
        self.add(line_with_caps, zero_text, thousand_text)
        
        percent_line = Line(UP * 0.1, DOWN * 0.1, color=WHITE)
        def create_percent_group(bar, percentage):
            percent_pos = bar.get_right()
            percent_line.next_to(percent_pos, DOWN*11.6)
            percent_label = Text(f"${percentage}", color=WHITE, font_size=16).next_to(percent_line, DOWN*1.5)
            return VGroup(percent_line, percent_label)
        
        percentage_value = ValueTracker(1000)
        
        percent_group = always_redraw(lambda: create_percent_group(collateral_bar, int(percentage_value.get_value())))
        line_with_caps[0].add_updater(lambda m: m.put_start_and_end_on(LEFT*3.65, percent_line.get_center()-RIGHT*0.01))
        
        self.add(line_with_caps, percent_group, percentage_value)
        
        def update_percentage70(mob, alpha):
            percentage = round(float(80 + (84.21 - 80) * alpha), 2)
            tempFactor.set_color(color=WHITE)   
            mob.become(Text(f"{percentage}%", color=WHITE).scale(0.75).next_to(percentage_label, RIGHT))
        
        shift_amount = (collateral_bar.width - new_width95) / 2     
        self.play(UpdateFromAlphaFunc(tempFactor[1], update_percentage70), collateral_bar.animate.stretch_to_fit_width(new_width95).shift(LEFT * shift_amount), percentage_value.animate.set_value(950), run_time=2, rate_func=linear)
        
        def update_percentage90(mob, alpha):
            percentage = round(float(84.21 + (88.89 - 84.21) * alpha), 2)
            tempFactor.set_color(color=WHITE)
            mob.become(Text(f"{percentage}%", color=WHITE).scale(0.75).next_to(percentage_label, RIGHT))
                
        shift_amount90 = (collateral_bar.width - new_width90) / 2     
        self.play(UpdateFromAlphaFunc(tempFactor[1], update_percentage90), collateral_bar.animate.stretch_to_fit_width(new_width90).shift(LEFT * shift_amount90),  percentage_value.animate.set_value(900), run_time=2, rate_func=linear)
        
        def update_percentage85(mob, alpha):
            percentage = round(float(88.89 + (94.11 - 88.89) * alpha), 2)
            if percentage < 94.11:
                tempFactor.set_color(color=WHITE)
                mob.become(Text(f"{percentage}%", color=WHITE).scale(0.75).next_to(percentage_label, RIGHT))
            elif percentage >= 94.11:
                tempFactor.set_color(RED)
                Liquidation_factor.set_color(color=RED, family=True)
                mob.become(Text(f"{percentage}%", color=RED).scale(0.75).next_to(percentage_label, RIGHT))
                
        shift_amount85 = (collateral_bar.width - new_width85) / 2     
        self.play(UpdateFromAlphaFunc(tempFactor[1], update_percentage85), collateral_bar.animate.stretch_to_fit_width(new_width85).shift(LEFT * shift_amount85),  percentage_value.animate.set_value(850), run_time=2, rate_func=linear)
        line_with_caps[0].clear_updaters()
        self.wait(duration=0.2)
        
class LoanCollateralAnimation(Scene):
    def construct(self):
        # Create the initial line
        line = Line(LEFT*3, LEFT*3 + RIGHT*9, color=WHITE)

        # Create caps for the line
        left_cap = Line(UP*0.1, DOWN*0.1, color=WHITE).next_to(line.get_start(), LEFT, buff=0)
        right_cap = Line(UP*0.1, DOWN*0.1, color=WHITE)

        # Set up an updater for the right_cap to follow the end of the line
        right_cap.add_updater(lambda cap: cap.next_to(line.get_end(), RIGHT, buff=0))

        # Group the line and its caps
        line_with_caps = VGroup(line, left_cap, right_cap)

        # Add text labels for the start and end values of the line
        zero_text = Text("$0", font_size=16, color=WHITE).next_to(line.get_start(), DOWN, buff=0.5)
        thousand_text = Text("$1000", font_size=16, color=WHITE).next_to(line.get_end(), DOWN, buff=0.5)
        
        # Add the line and text to the scene
        self.add(line_with_caps, zero_text, thousand_text)

        # Animate the change in length of the line
        new_line_end = LEFT*3 + RIGHT*7
        new_thousand_text = Text("$850", font_size=16, color=WHITE).next_to(new_line_end, DOWN, buff=0.5)
        self.play(
            line.animate.put_start_and_end_on(LEFT*3, new_line_end),
            Transform(thousand_text, new_thousand_text),
            run_time=2
        )
        right_cap.clear_updaters()

        self.wait(1)

class LinePercentageAnimation(Scene):
    def construct(self):
        # Create the line and caps
        line_start = LEFT * 3
        line_end_initial = line_start + RIGHT * 8
        line = Line(line_start, line_end_initial, color=WHITE)

        left_cap = Line(UP * 0.1, DOWN * 0.1, color=WHITE).next_to(line.get_start(), LEFT, buff=0)
        right_cap = Line(UP * 0.1, DOWN * 0.1, color=WHITE).next_to(line.get_end(), RIGHT, buff=0)
        
        # Function to update the position of the right cap
        right_cap.add_updater(lambda m: m.next_to(line.get_end(), RIGHT, buff=0))

        # Group the line and its caps
        line_with_caps = VGroup(line, left_cap, right_cap)

        # Add line with caps to the scene
        self.add(line_with_caps)

        # Animation to change the length of the line
        new_line_end = line_start + RIGHT * 5  # New end point for the line
        self.play(
            line.animate.put_start_and_end_on(line_start, new_line_end),
            run_time=2,
            rate_func=linear
        )

        # Remove the updater after the animation
        right_cap.clear_updaters()
        self.wait(1)

class LinePercentageAnimation2(Scene):
    def construct(self):
        # Create the line and caps
        line_start = LEFT * 3
        line_end_initial = line_start + RIGHT * 8
        line = Line(line_start, line_end_initial, color=WHITE)

        left_cap = Line(UP * 0.1, DOWN * 0.1, color=WHITE).next_to(line.get_start(), LEFT, buff=0)
        right_cap = Line(UP * 0.1, DOWN * 0.1, color=WHITE).next_to(line.get_end(), RIGHT, buff=0)

        # Function to update the position of the right cap
        right_cap.add_updater(lambda m: m.next_to(line.get_end(), RIGHT, buff=0))

        # Group the line and its caps
        line_with_caps = VGroup(line, left_cap, right_cap)

        # Create text for the start and end of the line
        start_text = Text("Start", color=WHITE, font_size=16).next_to(line.get_start(), DOWN, buff=0.2)
        end_text = Text("End", color=WHITE, font_size=16).next_to(line.get_end(), DOWN, buff=0.2)

        # Add line with caps and text to the scene
        self.add(line_with_caps, start_text, end_text)

        # Animation to change the length of the line
        new_line_end = line_start + RIGHT * 5  # New end point for the line
        self.play(
            line.animate.put_start_and_end_on(line_start, new_line_end),
            end_text.animate.next_to(new_line_end, DOWN, buff=0.2),
            run_time=2,
            rate_func=linear
        )
        right_cap.clear_updaters()

        self.wait(1)