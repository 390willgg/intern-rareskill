from manim import *

class overFold(Scene):
    def construct(self):
        temp_Operation_1 = MathTex(r'\text{Fold}(v_1)\hspace{0.5em}.\hspace{0.5em}\text{Fold}(v_2)')
        temp_Operation_2 = MathTex(r'V_1.\text{low}\hspace{0.5em}.\hspace{0.5em} V_2.\text{high} \hspace{0.5em} + \\V_1.\text{high}\hspace{0.5em}.\hspace{0.5em} V_2.\text{low}')
        
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
            temp_Operation_1,
            Text('-'),
            temp_Operation_2,
            tablePoint,
            tablePoint.copy()
        ]
        tempData1 = VGroup(temp[0], temp[3]).arrange(direction=DOWN, buff=1.65)
        tempData2 = VGroup(temp[2], temp[4]).arrange(direction=DOWN, buff=1)
        tempGroup1 = VGroup(tempData1, temp[1], tempData2).arrange(buff=0.5)
        self.play(Write(tempGroup1[0][0]), Write(tempGroup1[1].move_to(UP*2)), Write(tempGroup1[2][0]))
        self.play(Create(tempGroup1[0][1]), Create(tempGroup1[2][1]))
        
        tempAnimation = [
            # cross area of table
            temp[3].get_highlighted_cell((1,1), color=GREEN),
            temp[3].get_highlighted_cell((2,2), color=GREEN),
            temp[3].get_highlighted_cell((3,3), color=GREEN),
            temp[3].get_highlighted_cell((4,4), color=GREEN),
            
            # 
            temp[3].get_highlighted_cell((3,1), color=RED),
            temp[3].get_highlighted_cell((4,2), color=RED),
            
            temp[3].get_highlighted_cell((1,3), color=RED),
            temp[3].get_highlighted_cell((2,4), color=RED),

            temp[4].get_highlighted_cell((3,1), color=RED),
            temp[4].get_highlighted_cell((4,2), color=RED),
            
            temp[4].get_highlighted_cell((1,3), color=RED),
            temp[4].get_highlighted_cell((2,4), color=RED),    
        ]
        
        
        self.play(FadeIn(tempAnimation[0], tempAnimation[1], tempAnimation[2], tempAnimation[3]), FadeIn(tempAnimation[4], tempAnimation[5]), FadeIn(tempAnimation[6], tempAnimation[7]))
        self.play(FadeIn(tempAnimation[8], tempAnimation[9]), FadeIn(tempAnimation[10], tempAnimation[11]))
        positionScaleDown = VGroup(tempGroup1, VGroup(tempAnimation[0], tempAnimation[1], tempAnimation[2], tempAnimation[3], tempAnimation[4], tempAnimation[5], tempAnimation[6], tempAnimation[7]), VGroup(tempAnimation[8], tempAnimation[9], tempAnimation[10], tempAnimation[11]))
        self.play(positionScaleDown.animate.move_to(LEFT*2).scale(0.7))
        
        equalSymbol = Text('=').next_to(positionScaleDown, RIGHT*3 + UP)
        self.play(Create(equalSymbol))
        tempData3 = VGroup(MathTex(r'Inner Product').scale(0.7), tempData2[1].copy()).arrange(direction=DOWN, buff=1.4).next_to(positionScaleDown, RIGHT*3.5)
        
        animationTemp = [
            tempData3[1].get_highlighted_cell((1,1), color=GREEN),
            tempData3[1].get_highlighted_cell((2,2), color=GREEN),
            tempData3[1].get_highlighted_cell((3,3), color=GREEN),
            tempData3[1].get_highlighted_cell((4,4), color=GREEN),
        ]
        self.play(Create(tempData3))
        self.play(FadeIn(animationTemp[0], animationTemp[1], animationTemp[2], animationTemp[3]))
        
        
        
        
        
            
        