from manim import *
import numpy as np

class AreaResultOfFold(Scene):
    def construct(self):
      text_x1 = MarkupText("v<sub>1</sub>")
      text_x2 = MarkupText("v<sub>2</sub>")

      fold_v1 = VGroup(Text('Fold('), text_x1, Text(')')).arrange()
      fold_v2 = VGroup(Text('Fold('), text_x2, Text(')')).arrange()

      x1 = np.array([['a', 'b', 'c', 'd']])
      x2 = np.array([['p', 'q', 'r', 's']])

      array_tempX1 = Matrix(x1, h_buff=0.8)
      array_tempX2 = Matrix(x2, h_buff=0.8)

      dot = Dot()

      temp_fold = VGroup(fold_v1,dot, fold_v2).arrange_submobjects(buff=1, direction=RIGHT)
      temp_fold1 = temp_fold[0]
      temp_fold2 = temp_fold[2]

      self.play(Write(temp_fold1))
      self.play(Write(temp_fold2))
      self.play(temp_fold.animate.move_to(UP*2.5).scale(0.7))

      temp_array = VGroup(array_tempX1, array_tempX2)
      self.play(temp_array.animate.arrange_submobjects(buff=1, direction=RIGHT).scale(0.9).next_to(temp_fold, DOWN*4))

      text_x1Copy = text_x1.copy()
      text_x2Copy = text_x2.copy()
      self.play(text_x1Copy.animate.next_to(temp_array[0], UP*1.5), text_x2Copy.animate.next_to(temp_array[1], UP*1.5))
      
      def sliceArray(array, size, position, arrayData, equation, text_function):
        copy_arrayTemp = array.copy()

        first_half = VGroup(copy_arrayTemp.get_brackets()[0], *copy_arrayTemp.get_mob_matrix()[0][:size])
        second_half = VGroup(*copy_arrayTemp.get_mob_matrix()[0][size:], copy_arrayTemp.get_brackets()[1])
        self.play(first_half.animate.next_to(temp_array[position], DOWN*1), second_half.animate.next_to(first_half, DOWN*4+RIGHT*0.15))
        
        a, b, c, d = arrayData[0]
        
        matrix = Matrix([
            [f'{a} + {c}', f'{b} + {d}']
        ], h_buff=1.6)
        
        self.play(Write(matrix.get_brackets().next_to(array, DOWN*8)))
        matrix.get_entries().next_to(array, DOWN*9)
        
        first_half_elements = first_half
        second_half_elements = second_half
        
        for i in range(2):
          animations = [
              FadeIn(matrix.get_entries()[i][0][0], target_position=first_half_elements[i+1]),
              FadeIn(matrix.get_entries()[i][0][2], target_position=second_half_elements[i]),
              Write(matrix.get_entries()[i][0][1]),
          ]
          self.play(AnimationGroup(*animations, lag_ratio=0.5))

        self.play(FadeOut(first_half_elements, second_half_elements, array, text_function))
        
        self.play(matrix.get_brackets().animate.next_to(equation, DOWN*2))
        self.play(matrix.get_entries().animate.next_to(equation, DOWN*2.7))
        return matrix

      temp_arrayAdded1 = sliceArray(array_tempX1, 2, 0, x1, temp_fold1, text_x1Copy)
      temp_arrayAdded2 = sliceArray(array_tempX2, 2, 1, x2, temp_fold2, text_x2Copy)
      
      temp_1 = temp_arrayAdded1.copy()
      temp_2 = temp_arrayAdded2.copy()
      
      tempA1 = VGroup(MathTex('('), temp_1.get_entries()[0], MathTex(')')).arrange()
      tempA2 = VGroup(MathTex('('), temp_2.get_entries()[0], MathTex(')')).arrange()
      tempB1 = VGroup(MathTex('('), temp_1.get_entries()[1], MathTex(')')).arrange()
      tempB2 = VGroup(MathTex('('), temp_2.get_entries()[1], MathTex(')')).arrange()
      group_1 = VGroup(tempA1, tempA2).arrange()
      group_2 = VGroup(tempB1, tempB2).arrange()
      group_3 = VGroup(group_1, group_2).arrange(buff=1.5)
      
    #   Scene 6
      group_3.next_to(dot, DOWN*8)
      dot_multiple = Dot()
      
      tempMultipleA1 = VGroup(MathTex('a'),MathTex('p')).arrange()
      tempMultipleA2 = VGroup(MathTex('c'),MathTex('r')).arrange()
      tempMultipleB1 = VGroup(MathTex('c'),MathTex('p')).arrange()
      tempMultipleB2 = VGroup(MathTex('c'),MathTex('r')).arrange()
      tempMultipleC1 = VGroup(MathTex('b'),MathTex('q')).arrange()
      tempMultipleC2 = VGroup(MathTex('b'),MathTex('s')).arrange()
      tempMultipleD1 = VGroup(MathTex('d'),MathTex('q')).arrange()
      tempMultipleD2 = VGroup(MathTex('d'),MathTex('s')).arrange()
      
      groupMultiple_1 = VGroup(VGroup(tempMultipleA1, MathTex('+'), tempMultipleA2).arrange(), VGroup(tempMultipleB1, MathTex('+'), tempMultipleB2).arrange()).arrange(buff=0.5)
      groupMultiple_2 = VGroup(VGroup(tempMultipleC1, MathTex('+'), tempMultipleC2).arrange(), VGroup(tempMultipleD1, MathTex('+'), tempMultipleD2).arrange()).arrange(buff=0.5)
      
      groupMultiple_result = VGroup(groupMultiple_1, MathTex('+'), groupMultiple_2).arrange(buff=0.5)
      groupMultiple_result.next_to(dot_multiple, DOWN*3)
      
      temp_valueOfTranform = [
          temp_arrayAdded1.get_entries()[0].copy(),
          temp_arrayAdded2.get_entries()[0].copy(),
          dot_multiple,
          temp_arrayAdded1.get_entries()[1].copy(),
          temp_arrayAdded2.get_entries()[1].copy()
      ]
      animationTransform = [
          Transform(temp_valueOfTranform[0], tempA1),
          Transform(temp_valueOfTranform[1], tempA2),
          Create(temp_valueOfTranform[2]),
          Transform(temp_valueOfTranform[3], tempB1),
          Transform(temp_valueOfTranform[4], tempB2)
      ]
      self.play(AnimationGroup(*animationTransform, lag_ratio=0.5))
      
      temp_multipleData = [
        #   yellow
          temp_1.get_entries()[0][0][0].copy(),
          temp_2.get_entries()[0][0][0].copy(),
          
          groupMultiple_1[0][1],
          
          temp_1.get_entries()[0][0][2].copy(),
          temp_2.get_entries()[0][0][2].copy(),
          
        #   Blue 5
          temp_1.get_entries()[0][0][2].copy(),
          temp_2.get_entries()[0][0][0].copy(),
          
          groupMultiple_1[1][1],
          
          temp_1.get_entries()[0][0][2].copy(),
          temp_2.get_entries()[0][0][2].copy(),
          
        #   yellow - 10
          temp_1.get_entries()[1][0][0].copy(),
          temp_2.get_entries()[1][0][0].copy(),
          
          groupMultiple_2[0][1],
          
          temp_1.get_entries()[1][0][2].copy(),
          temp_2.get_entries()[1][0][2].copy(),
          
        #   red 15
          temp_1.get_entries()[1][0][2].copy(),
          temp_2.get_entries()[1][0][0].copy(),
          
          groupMultiple_2[1][1],
          
          temp_1.get_entries()[1][0][2].copy(),
          temp_2.get_entries()[1][0][2].copy(),
          
          SurroundingRectangle(groupMultiple_1[0], color=YELLOW),
          SurroundingRectangle(groupMultiple_2[0], color=YELLOW),
          SurroundingRectangle(groupMultiple_1[1], color=BLUE),
          SurroundingRectangle(groupMultiple_2[1], color=RED)
      ]
      
      self.play(temp_multipleData[0].animate(rate_func=linear, run_time=1).move_to(tempMultipleA1[0]), temp_multipleData[1].animate(rate_func=linear, run_time=1).move_to(tempMultipleA1[1]))
      self.play(Create(temp_multipleData[2]))
      self.play(temp_multipleData[3].animate(rate_func=linear, run_time=1).move_to(tempMultipleA2[0]), temp_multipleData[4].animate(rate_func=linear, run_time=1).move_to(tempMultipleA2[1]))
      
      self.play(temp_multipleData[5].animate(rate_func=linear, run_time=1).move_to(tempMultipleB1[0]), temp_multipleData[6].animate(rate_func=linear, run_time=1).move_to(tempMultipleB1[1]))
      self.play(Create(temp_multipleData[7]))
      self.play(temp_multipleData[8].animate(rate_func=linear, run_time=1).move_to(tempMultipleB2[0]), temp_multipleData[9].animate(rate_func=linear, run_time=1).move_to(tempMultipleB2[1]))
      
      
      self.play(temp_multipleData[10].animate(rate_func=linear, run_time=1).move_to(tempMultipleC1[0]), temp_multipleData[11].animate(rate_func=linear, run_time=1).move_to(tempMultipleC1[1]))
      self.play(Create(temp_multipleData[12]))
      self.play(temp_multipleData[13].animate(rate_func=linear, run_time=1).move_to(tempMultipleC2[0]), temp_multipleData[14].animate(rate_func=linear, run_time=1).move_to(tempMultipleC2[1]))
      
      self.play(temp_multipleData[15].animate(rate_func=linear, run_time=1).move_to(tempMultipleD1[0]), temp_multipleData[16].animate(rate_func=linear, run_time=1).move_to(tempMultipleD1[1]))
      self.play(Create(temp_multipleData[17]))
      self.play(temp_multipleData[18].animate(rate_func=linear, run_time=1).move_to(tempMultipleD2[0]), temp_multipleData[19].animate(rate_func=linear, run_time=1).move_to(tempMultipleD2[1]))
     
      self.play(Create(temp_multipleData[20]), Create(temp_multipleData[21]), Create(temp_multipleData[22]), Create(temp_multipleData[23]))
      
      group_element = VGroup(temp_fold, VGroup(temp_arrayAdded1, temp_arrayAdded2), VGroup(*temp_valueOfTranform), VGroup(*temp_multipleData))
      self.play(group_element.animate.arrange_submobjects(direction=DOWN).move_to(LEFT*3).scale(0.6))
      
      row_labels = [Text("a"), Text("b"), Text("c"), Text("d"), Text('e')]
      column_labels = [Text("p"), Text("q"), Text("r"), Text('s'), Text('t')]
      
      table = Table(
            [['c', 'd', '1', '4', '5'],
              ['11', '10', '9', '8', '3'],
              ['12', '13', '14', '15', '2'],
              ['21', '20', '19', '7', '16'],
              ['22', '24', '23', '25', '26']], 
            row_labels=row_labels,
            col_labels=column_labels,
            h_buff=0.8
        ).scale(0.6)
      for i in range(len(table.get_rows())):
        table.get_rows()[i].set_opacity(0)
      
      table.next_to(group_element, RIGHT*3)
      self.play(Create(table))
      
      temp_higlightTable = [
          table.get_highlighted_cell((2,2), color=YELLOW),
          table.get_highlighted_cell((3,3), color=YELLOW),
          table.get_highlighted_cell((4,4), color=YELLOW),
          table.get_highlighted_cell((5,5), color=YELLOW),
          
          table.get_highlighted_cell((2,4), color=BLUE),
          table.get_highlighted_cell((3,5), color=BLUE),
          
          table.get_highlighted_cell((4,2), color=RED),
          table.get_highlighted_cell((5,3), color=RED),
      ]
      
    #   YellOW
      self.play(VGroup(temp_multipleData[0], temp_multipleData[1]).copy().animate(run_time=1.5).move_to(table.get_rows()[1][1]).set_color(BLACK))
      self.play(FadeIn(temp_higlightTable[0], run_time=0.5))
      
      self.play(VGroup(temp_multipleData[3], temp_multipleData[4]).copy().animate(run_time=1.5).move_to(table.get_rows()[2][2]).set_color(BLACK))
      self.play(FadeIn(temp_higlightTable[1], run_time=0.5))
      
      self.play(VGroup(temp_multipleData[10], temp_multipleData[11]).copy().animate(run_time=1.5).move_to(table.get_rows()[3][3]).set_color(BLACK))
      self.play(FadeIn(temp_higlightTable[2], run_time=0.5))
      
      self.play(VGroup(temp_multipleData[13], temp_multipleData[14]).copy().animate(run_time=1.5).move_to(table.get_rows()[4][4]).set_color(BLACK))
      self.play(FadeIn(temp_higlightTable[3], run_time=0.5))
      
    #   BlUE
      self.play(VGroup(temp_multipleData[5], temp_multipleData[6]).copy().animate(run_time=1.5).move_to(table.get_rows()[1][3]).set_color(BLACK))
      self.play(FadeIn(temp_higlightTable[4], run_time=0.5))
      
      self.play(VGroup(temp_multipleData[8], temp_multipleData[9]).copy().animate(run_time=1.5).move_to(table.get_rows()[2][4]).set_color(BLACK))
      self.play(FadeIn(temp_higlightTable[5], run_time=0.5))
      
    #   RED
      self.play(VGroup(temp_multipleData[15], temp_multipleData[16]).copy().animate(run_time=1.5).move_to(table.get_rows()[3][1]).set_color(BLACK))
      self.play(FadeIn(temp_higlightTable[6], run_time=0.5))
      
      self.play(VGroup(temp_multipleData[18], temp_multipleData[19]).copy().animate(run_time=1.5).move_to(table.get_rows()[4][2]).set_color(BLACK))
      self.play(FadeIn(temp_higlightTable[7], run_time=0.5))