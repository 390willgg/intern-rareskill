from manim import *

class InnerProductTableModel(Scene):
  def construct(self):
    x1 = np.array([['a', 'b', 'c', 'd']])
    x2 = np.array([['p', 'q', 'r', 's']])

    text_x1 = MarkupText("v<sub>1</sub>")
    text_x2 = MarkupText("v<sub>2</sub>")

    equal_x1 = MathTex('=')
    equal_x2 = MathTex('=')

    matrix_tempX1 = Matrix(x1)
    matrix_tempX2 = Matrix(x2)

    tempFunction_x1 = VGroup(matrix_tempX1, equal_x1, text_x1.scale(0.8)).arrange_submobjects(buff=0.1)
    tempFunction_x2 = VGroup(matrix_tempX2, equal_x2, text_x2.scale(0.8)).arrange_submobjects(buff=0.1)

    tempGroup = VGroup(tempFunction_x1, tempFunction_x2).arrange_submobjects(buff=0.5, direction = DOWN)
    temp_x1 = tempGroup[0]
    temp_x2 = tempGroup[1]

    vertical_areaData_x1 = UP * 3
    vertical_areaData_x2 = UP * 2

    row_labels = [Text("a"), Text("b"), Text("c")]
    column_labels = [Text("p"), Text("q"), Text("r")]

    tablePoint = Table(
            [['', '', ''],
              ['', '', ''],
              ['', '', '']],
            row_labels=row_labels,
            col_labels=column_labels,
            include_outer_lines=True, h_buff=1).scale(0.5).shift(DOWN*1.4)
    tablePoint.get_rows()[0].set_opacity(0)
    tablePoint.get_columns()[0].set_opacity(0)

    self.play(Write(temp_x1))
    self.play(Write(temp_x2))

    self.play(temp_x1.animate.move_to(vertical_areaData_x1).scale(0.7), temp_x2.animate.move_to(vertical_areaData_x2).scale(0.7))

    dataRow = [matrix_tempX1.get_entries()[i] for i in range(4)]
    dataColumn = [matrix_tempX2.get_entries()[i] for i in range(4)]

    groupRowTitle = VGroup(*dataRow)
    groupColumnTitle = VGroup(*dataColumn)
    self.play(groupRowTitle.animate.arrange(buff=0.5, direction=DOWN).next_to(tablePoint, LEFT*1.2))
    self.play(groupColumnTitle.animate.arrange(buff=0.5).next_to(tablePoint, UP*1.2))
    self.add(tablePoint)

    row_brace = Brace(groupRowTitle, direction = LEFT*2.2)
    self.play(text_x1.animate.next_to(row_brace, LEFT))
    self.play(FadeOut(equal_x1))

    column_brace = Brace(groupColumnTitle, direction = UP * 2.2)
    self.play(text_x2.animate.next_to(column_brace, UP))
    self.play(FadeOut(equal_x2))
    self.play(FadeOut(matrix_tempX1.get_brackets()))
    self.play(FadeOut(matrix_tempX2.get_brackets()))

    self.play(FadeIn(row_brace))
    self.play(FadeIn(column_brace))

    for i in range(4):
      print(f'hasil index: {i}')
      highlight = tablePoint.get_highlighted_cell((i+1,i+1), color=GREEN)
      self.play(FadeIn(highlight, run_time=0.5))
