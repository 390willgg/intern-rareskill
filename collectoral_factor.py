from manim import *

class CollateralLoanScene(Scene):
    def construct(self):
        # Create text labels
        collateral_label = Text("Collateral", color=WHITE).next_to(UP*2+LEFT*7)
        loan_label = Text("Loan", color=WHITE).next_to(collateral_label, DOWN, buff=1.5)
        loan_label.align_to(collateral_label, LEFT)

        # Create the bars
        original_width = 8
        collateral_bar = RoundedRectangle(width=original_width, height=1, color=WHITE, corner_radius=0.2).next_to(collateral_label, RIGHT)
        loan_bar = RoundedRectangle(width=original_width, height=1, color=WHITE, corner_radius=0.2).next_to(loan_label, RIGHT)
        loan_bar.align_to(collateral_bar, LEFT)

        # Create the percentage text
        factor = Text("100")
        percentage_label = Text("Collateral_Factor =", color=WHITE)
        tempFactor = VGroup(percentage_label, factor, Text("%")).arrange(direction=RIGHT, buff=0.3).next_to(LEFT*8 + DOWN*3.1).scale(0.75)
        
        # Create the brand text
        brand_label = ImageMobject("media\images/collectoral_factor/rareskillLogo.png").next_to(RIGHT*3+DOWN*3.1)

        # Group everything together
        self.add(collateral_label, loan_label, collateral_bar, loan_bar, tempFactor, brand_label)
        
        # Calculate the shift to the left ne/ded during stretching
        new_width70 = 8*0.7
        shift_amount70 = (loan_bar.width - new_width70) / 2

        self.play(loan_bar.animate.stretch_to_fit_width(new_width70).shift(LEFT * shift_amount70))
       
        for i in range(100, 69, -1):
            self.play(Transform(tempFactor[1], Tex(f"{i}%").next_to(tempFactor[0], RIGHT)), run_time=0.1, rate_func=linear)
            
        brace_70 = BraceBetweenPoints(
            loan_bar.get_right(), 
            loan_bar.get_right() + RIGHT * (original_width - new_width70), 
            direction=DOWN, 
            color=GREEN
        ).shift(DOWN * 0.2)  # Adjust the 0.2 value as needed
        brace_text70 = brace_70.get_text(r"Higher Margin \\of Safety")
        self.play(GrowFromCenter(brace_70), Write(brace_text70))
        self.play(FadeOut(brace_70, brace_text70))
        
        new_width90 = 8 * 0.9
        shift_amount90 = (loan_bar.width - new_width90) / 2
        self.play(loan_bar.animate.stretch_to_fit_width(new_width90).shift(LEFT * shift_amount90))
        
        for i in range(70, 91, 1):
            self.play(Transform(tempFactor[1], Tex(f"{i}%").next_to(tempFactor[0], RIGHT)), run_time=0.1, rate_func=linear)
       
        # Create a brace for the 90% stretch
        brace_90 = BraceBetweenPoints(
            loan_bar.get_right(), 
            loan_bar.get_right() + RIGHT * (original_width - new_width90), 
            direction=DOWN, 
            color=RED
        ).shift(DOWN * 0.2)
        brace_text90 = brace_90.get_text(r"Lower Margin \\of Safety")

        self.play(GrowFromCenter(brace_90), Write(brace_text90))
        self.play(FadeOut(brace_90, brace_text90))