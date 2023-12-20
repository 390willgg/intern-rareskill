from manim import *

from manim import *

class CollateralLoan(Scene):
    def construct(self):
        # Create the logo and the text
        logo = Text("R RareSkill").scale(0.2).to_corner(UR)
        title = Text("Collateral Loan", font_size=48).next_to(logo, DOWN, buff=0.5)
        self.add(logo, title)

        # Create the bars and the labels
        collateral = Rectangle(width=6, height=1, color=WHITE, fill_opacity=1).next_to(title, DOWN, buff=1)
        loan = Rectangle(width=4.5, height=1, color=WHITE, fill_opacity=1).next_to(collateral, DOWN, buff=0.5)
        collateral_label = MathTex("Collateral", color=BLACK).next_to(collateral, UP, buff=0.1)
        loan_label = MathTex("Loan", color=BLACK).next_to(loan, UP, buff=0.1)
        
        self.play(
            Create(collateral),
            Create(loan),
            Write(collateral_label),
            Write(loan_label)
        )

        # Create the factor and the equation
        factor = DecimalNumber(0.9, num_decimal_places=2, color=WHITE).next_to(loan, RIGHT, buff=1)
        factor_label = MathTex("\\text{Collateral Factor}", color=WHITE).next_to(factor, DOWN, buff=0.1)
        equation = MathTex("\\text{Loan} = \\text{Collateral} \\times \\text{Collateral Factor}", color=WHITE).next_to(factor, RIGHT, buff=1)
        self.play(
            Write(factor),
            Write(factor_label),
            Write(equation)
        )

        # Animate the change of the factor and the loan
        self.play(
            factor.animate.set_value(0.8),
            loan.animate.stretch_to_fit_width(3.6),
            run_time=2
        )
        self.wait()
        
class CollateralLoanScene(Scene):
    def construct(self):
        # Create text labels
        collateral_label = Text("Collateral", color=WHITE).to_edge(UP)
        loan_label = Text("Loan", color=WHITE).next_to(collateral_label, DOWN, buff=1.5)

        # Create the bars
        collateral_bar = Rectangle(width=5, height=0.5, color=WHITE).next_to(collateral_label, DOWN)
        loan_bar = Rectangle(width=4.5, height=0.5, color=WHITE).next_to(loan_label, DOWN)

        # Create the percentage text
        percentage_label = Text("Collateral_Factor = 90%", color=WHITE).to_edge(DOWN)

        # Create the brand text
        brand_label = Text("RareSkills", color=WHITE).next_to(percentage_label, DOWN)

        # Group everything together
        self.add(collateral_label, loan_label, collateral_bar, loan_bar, percentage_label, brand_label)

        # Animate the bars
        self.play(
            collateral_bar.animate.set_width(9, stretch=True),
            loan_bar.animate.set_width(8.1, stretch=True),
            run_time=2
        )

        # Hold the final state for a brief moment
        self.wait(2)

class QuickPercentDecreaseScene(Scene):
    def construct(self):
        # Create a Tex object to display the initial percentage
        percentage = Tex("100%").scale(2)
        self.add(percentage)

        # Animate the percentage decreasing from 100% to 60%
        for i in range(100, 59, -1):
            self.play(Transform(percentage, Tex(f"{i}%").scale(2)), run_time=0.1, rate_func=linear)

        # Hold the final state for a brief moment
        self.wait(1)

# To render the scene, use the following command in the terminal:
# manim -pql your_script_name.py QuickPercentDecreaseScene

    
