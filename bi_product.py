from manim import *

class BiProduct(Scene):
    def construct(self):  
        textWelcome = VGroup(Text('How To Calculate', should_center=True),Text('For The', should_center=True), Text('Bi-Product', should_center=True)).arrange_submobjects(direction=DOWN, buff=0.7)  
        self.play(Create(textWelcome))
        self.play(FadeOut(textWelcome))
        
        x1 = np.array([['a', 'b', 'c', 'd']])
        x2 = np.array([['p', 'q', 'r', 's']])
        
        matrix_tempX1 = Matrix(x1)
        matrix_tempX2 = Matrix(x2)
        
        dataRow = [matrix_tempX1.get_entries()[i] for i in range(4)]
        dataColumn = [matrix_tempX2.get_entries()[i] for i in range(4)]
        
        groupRowTitle = VGroup(*dataRow)
        groupColumnTitle = VGroup(*dataColumn)
        
        row_labels = [Text("a"), Text("b"), Text("c")]
        column_labels = [Text("p"), Text("q"), Text("r")]

        tablePoint = Table(
                [['', '', ''],
                ['', '', ''],
                ['', '', '']],
                row_labels=row_labels,
                col_labels=column_labels,
                include_outer_lines=True, h_buff=1).scale(0.75)
        tablePoint.get_rows()[0].set_opacity(0)
        tablePoint.get_columns()[0].set_opacity(0)
        
        temp = [
            tablePoint,
            tablePoint.copy()
        ]

        tempAnimation = [
            temp[0].get_highlighted_cell((1,1), color=YELLOW),
            temp[0].get_highlighted_cell((2,2), color=YELLOW),
            temp[0].get_highlighted_cell((3,3), color=YELLOW),
            temp[0].get_highlighted_cell((4,4), color=YELLOW),
            
            temp[1].get_highlighted_cell((3,1), color=RED),
            temp[1].get_highlighted_cell((4,2), color=RED),
            
            temp[1].get_highlighted_cell((1,3), color=BLUE),
            temp[1].get_highlighted_cell((2,4), color=BLUE),
        ]
        
        tempTitle = [
            groupRowTitle,
            groupColumnTitle,
            groupRowTitle.copy(),
            groupColumnTitle.copy()
        ]
        self.play(tempTitle[0].animate.arrange(buff=0.5, direction=DOWN).next_to(temp[0], LEFT*1.2))
        self.play(tempTitle[1].animate.arrange(buff=0.8).next_to(temp[0], UP*1.2))
        tempTitle[2].arrange(buff=0.5, direction=DOWN).next_to(temp[1], LEFT*1.2)
        self.add(tempTitle[2])
        tempTitle[3].arrange(buff=0.8).next_to(temp[1], UP*1.2)
        self.add(tempTitle[3])
        
        self.play(Create(tablePoint))
        self.play(FadeIn(tempAnimation[0], tempAnimation[1], tempAnimation[2], tempAnimation[3]), FadeIn(tempAnimation[4], tempAnimation[5]), FadeIn(tempAnimation[6], tempAnimation[7]))
        
        tempGroupData = [
            VGroup(VGroup(temp[0], tempAnimation[0], tempAnimation[1], tempAnimation[2], tempAnimation[3], tempTitle[0], tempTitle[1]), Text("Inner Product")),
            VGroup(VGroup(temp[1], tempAnimation[4], tempAnimation[5], tempAnimation[6], tempAnimation[7], tempTitle[2], tempTitle[3]), Text("Bi-Product"))
        ]
        
        self.play(tempGroupData[0].animate.arrange(direction=DOWN, buff=0.7).move_to(LEFT*2.5), tempGroupData[1].animate.arrange(direction=DOWN, buff=0.7).move_to(RIGHT*2.5))
        self.play(FadeOut(tempGroupData[0]), tempGroupData[1].animate.move_to(LEFT*3.2))
        
        textEquestion = [
            Text("ar", color=RED),
            Text("+", color=RED),
            Text("bs", color=RED),
            
            Text("+"),
            
            Text("cp", color=BLUE),
            Text("+", color=BLUE),
            Text("dq", color=BLUE)
        ]
        
        equestion_part01 = VGroup(textEquestion[0], textEquestion[1], textEquestion[2]).arrange()
        equestion_part02 = VGroup(textEquestion[4], textEquestion[5], textEquestion[6]).arrange()
        equestion = VGroup(equestion_part01, textEquestion[3], equestion_part02).arrange().move_to(UP*3 + RIGHT*2.5).scale(0.75)
        
        self.play(FadeIn(textEquestion[0].move_to(equestion[0][0]), target_position=tempGroupData[1][0][1]))
        self.play(Create(textEquestion[1].move_to(equestion[0][1])))
        self.play(FadeIn(textEquestion[2].move_to(equestion[0][2]), target_position=tempGroupData[1][0][2]))

        self.play(Create(textEquestion[3].move_to(equestion[1])))
        
        self.play(FadeIn(textEquestion[4].move_to(equestion[2][0]), target_position=tempGroupData[1][0][3]))
        self.play(Create(textEquestion[5].move_to(equestion[2][1])))
        self.play(FadeIn(textEquestion[6].move_to(equestion[2][2]), target_position=tempGroupData[1][0][4]))
        
        tempGroupCell = [
            VGroup(tempGroupData[1][0][5][0], tempGroupData[1][0][5][1]), 
            VGroup(tempGroupData[1][0][5][2], tempGroupData[1][0][5][3]), 
            VGroup(tempGroupData[1][0][6][0], tempGroupData[1][0][6][1]), 
            VGroup(tempGroupData[1][0][6][2], tempGroupData[1][0][6][3])
        ]
        
        tempBrace = [
            # AB
            VGroup(MathTex(r'v_2.low', font_size=25), Brace(tempGroupCell[0], direction=LEFT, sharpness=1)).arrange(),
            # CD
            VGroup(MathTex(r'v_2.high', font_size=25), Brace(tempGroupCell[1], direction=LEFT, sharpness=1)).arrange(),
            # PQ
            VGroup(MathTex(r'v_1.low', font_size=25), Brace(tempGroupCell[2], direction=UP, sharpness=1)).arrange(direction=DOWN),
            #RS
            VGroup(MathTex(r'v_1.high', font_size=25), Brace(tempGroupCell[3], direction=UP, sharpness=1)).arrange(direction=DOWN),
        ]
        
        self.play(Create(tempBrace[0].next_to(tempGroupCell[0], LEFT*1)))
        self.play(Create(tempBrace[1].next_to(tempGroupCell[1], LEFT*1)))
        self.play(Create(tempBrace[2].next_to(tempGroupCell[2], UP*1)))
        self.play(Create(tempBrace[3].next_to(tempGroupCell[3], UP*1)))
        
        equestion_01 = VGroup(MathTex(r"v_{1low}.v_{2.high}"), MathTex(r"+"), MathTex(r"v_{1high}.v_{2low}")).arrange().next_to(equestion, DOWN*2).scale(0.75)
        equestion_02 = VGroup(MathTex(r"\left[ a, b \right] \left[ r, s \right]"), MathTex(r"+"), MathTex(r"\left[ c, d \right] \left[ p, q \right]")).arrange().next_to(equestion_01, DOWN).scale(0.75)
        equestion_03 = VGroup(MathTex(r"ar + bs"), MathTex(r"+"),MathTex(r"cp + dq")).arrange().next_to(equestion_02, DOWN).scale(0.75)
    
        self.play(Write(equestion_01))
        self.play(Create(equestion_02))
        self.play(Create(equestion_03))
        
