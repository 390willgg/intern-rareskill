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